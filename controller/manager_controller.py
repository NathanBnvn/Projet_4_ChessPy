#!/usr/bin/env python
# coding: utf-8

from os import system, name
from model.tournament_model import Tournament
from model.player_model import Player
import datetime


class ManagerController:
    def __init__(self, view):
        self.manager_view = view
        self.tournament_model = Tournament
        self.player_model = Player

    def clean_terminal(self):
        if name == 'nt':
            # pour windows
            _ = system('cls')
        else:
            # pour mac & linux
            _ = system('clear')

    def check_user_input(self, input_category, message, choices):
        i = 0
        user_content = []
        previous_date = []
        wrong_date_format = "Veuillez entrer la date dans un format valide !"
        wrong_timeline = """
            Entrez une date de fin supérieur ou égale à celle du début !
            """
        wrong_type = "Veuillez entrer un nombre entier !"
        negative_number = "Veuillez entrer un nombre positif !"
        invalid_action_message = "Commande non valide. Veuillez réessayer."
        quit_message = "Vous venez d'interrompre votre action"

        while i < len(input_category):
            input_data = input_category[i]
            if "sélectionnez" in input_data:
                user_choice = self.manager_view.select_command(self, message,
                                                               choices)
                user_content.append(user_choice)
                i += 1
            else:
                content = self.manager_view.prompt_command(self, input_data)
                if content == 'quit':
                    self.manager_view.show_message(self, quit_message)
                    break
                elif content.isspace():
                    self.manager_view.show_message(self,
                                                   invalid_action_message)
                elif "(jj/mm/aaaa)" in input_data:
                    try:
                        date = datetime.datetime.strptime(content, "%d/%m/%Y")
                        if previous_date:
                            if date >= previous_date[0]:
                                user_content.append(content)
                                i += 1
                            else:
                                self.manager_view.show_message(self,
                                                               wrong_timeline)
                        else:
                            user_content.append(content)
                            previous_date.append(date)
                            i += 1
                    except ValueError:
                        self.manager_view.show_message(self, wrong_date_format)
                elif "nombre" in input_data or "classement" in input_data:
                    if content.isdigit():
                        if int(content) > 0:
                            user_content.append(int(content))
                            i += 1
                        else:
                            self.manager_view.show_message(self,
                                                           negative_number)
                    else:
                        self.manager_view.show_message(self, wrong_type)
                else:
                    user_content.append(content)
                    i += 1
        return user_content

    def update_process(self, data_model):
        success_message = "La donnée a bien été mis à jour"
        no_data_message = "Aucune donnée existante. Veuillez en ajouter"
        something_went_wrong = "Un problème est survenu. Veuillez réessayer."
        quit_message = "Vous venez d'interrompre votre mise à jour"

        elements = data_model.get_all(self)
        if len(elements) > 0:
            self.manager_view.show_json(self, elements)

            element_id = self.check_id_input(len(elements))
            if element_id:
                element = data_model.get(self, element_id)
                self.manager_view.show_json(self, element)

                category = self.select_updating_content(element)
                if 'rounds' in category:
                    selected_rounds = element['rounds']
                    updated_round = self.update_round(selected_rounds,
                                                      element_id)
                    if updated_round:
                        self.manager_view.show_message(self, success_message)
                    else:
                        self.manager_view.show_message(self, quit_message)
                elif 'players' in category:
                    selected_players = element['players']
                    category, new_value, player_last_name, selected_players = \
                        self.update_player_tournament(
                            selected_players
                        )
                    if new_value:
                        update_player = self.player_model.update(
                            self, category, new_value, player_last_name
                            )
                        update_tournament = self.tournament_model.update(
                            self, 'player', selected_players, element_id
                            )
                        if update_player or update_tournament:
                            self.manager_view.show_message(self,
                                                           success_message)
                        else:
                            self.manager_view.show_message(
                                self, something_went_wrong
                            )
                    else:
                        self.manager_view.show_message(self, quit_message)
                else:
                    self.save_register(element_id, category, data_model)
            else:
                self.manager_view.show_message(self, quit_message)
        else:
            self.manager_view.show_message(self, no_data_message)

    def update_round(self, selected_rounds, element_id):
        update_message = """
                Quelle round souhaitez-vous modifier ? (par ex: Round 1):
            """
        select_type = "Quelles données souhaitez-vous modifier ?"
        not_found_message = """
            Cette valeur ne correspond à rien. Veuillez réessayer
            """
        continue_message = "Souhaitez-vous modifier un autre round ? (o/n) : "
        value_message = "Veuillez entrer la nouvelle valeur : "
        round_names = []
        rounds = []

        self.manager_view.show_json(self, selected_rounds)
        while True:
            if selected_rounds:
                for round in selected_rounds:
                    name = round[0]['name']
                    round_names.append(name)
                    rounds.append(round[0])

                select_round = self.manager_view.prompt_command(self,
                                                                update_message)
                if select_round in round_names:
                    element = list(
                                filter(
                                    lambda
                                    round_object: round_object[
                                        'name'
                                        ] == select_round,
                                    rounds
                                    )
                                )

                    choices = ['name', 'round', 'start_at', 'finish_at']
                    user_choice = self.manager_view.select_command(
                        self, select_type, choices)

                    new_value = self.manager_view.prompt_command(
                        self, value_message)
                    if new_value == "quit":
                        return
                    else:
                        element[0][user_choice] = new_value
                        _ = self.tournament_model.update(
                            self, 'rounds', selected_rounds, element_id
                            )

                    continue_editing = self.manager_view.prompt_command(
                        self, continue_message)
                    if continue_editing == "o":
                        self.update_round(selected_rounds)
                    elif continue_editing == "n":
                        return continue_editing
                    else:
                        self.manager_view.show_message(self, not_found_message)
                elif select_round == "quit":
                    break
                else:
                    self.manager_view.show_message(self, not_found_message)

    def update_player_tournament(self, selected_players):
        select_message = """
            Veuillez entrer le nom du joueur que vous souhaitez modifier :
            """
        not_found_message = """
            Cette valeur ne correspond à rien. Veuillez réessayer
            """
        value_message = "Veuillez entrer la nouvelle valeur : "
        self.manager_view.show_json(self, selected_players)

        while True:
            if selected_players:
                if len(selected_players) > 1:
                    selected_player_name = self.manager_view.prompt_command(
                        self, select_message)
                    if any(
                            players['last_name'] == selected_player_name
                            for players in selected_players):
                        saved_player = self.player_model.get_by_name(
                                self, selected_player_name)
                        category = self.select_updating_content(
                                saved_player[0])
                        new_value = self.manager_view.prompt_command(
                                self, value_message)
                        edited_players = list(
                                filter(
                                    lambda
                                    player: player[
                                        'last_name'
                                        ] == selected_player_name,
                                    selected_players
                                )
                            )
                        edited_players[0][category] = new_value
                        return category, new_value, \
                            selected_player_name, selected_players
                    else:
                        self.manager_view.show_message(self, not_found_message)
                else:
                    player_last_name = selected_players[0]['last_name']
                    saved_player = self.player_model.get_by_name(
                        self, player_last_name)
                    category = self.select_updating_content(saved_player[0])
                    new_value = self.manager_view.prompt_command(
                        self, value_message)
                    selected_players[0][category] = new_value
                    return category, new_value, player_last_name,\
                        selected_players

    def select_updating_content(self, element):
        select_category = "Quelle propriété souhaitez vous éditer ?"
        categories = []
        for key in element:
            categories.append(key)
        category = self.manager_view.select_command(self, select_category,
                                                    categories)
        return category

    def check_id_input(self, instances_count):
        select_id = "Veuillez sélectionner l'ID de l'instance souhaitée : "
        id_not_found = "L'ID entré ne correspond à rien. Veuillez réessayer."
        error_message = "Veuillez entrer un nombre entier"

        while True:
            selected_id = self.manager_view.prompt_command(self, select_id)
            if selected_id == "quit":
                return
            elif selected_id.isdigit():
                element_id = int(selected_id)
                if element_id <= instances_count and element_id != 0:
                    return element_id
                else:
                    self.manager_view.show_message(self, id_not_found)
            else:
                self.manager_view.show_message(self, error_message)

    def save_register(self, element_id, category, data_model):
        value_message = "Veuillez entrer la nouvelle valeur : "
        cannot_save_message = "Les données n'ont pas pu être enregistrées"
        success_message = "La donnée a bien été mis à jour"
        quit_message = "Vous venez d'interrompre votre mise à jour"

        new_value = self.manager_view.prompt_command(self, value_message)
        if new_value == "quit":
            self.manager_view.show_message(self, quit_message)
            return
        else:
            update_element = data_model.update(self, category,
                                               new_value, element_id)
            if element_id in update_element:
                self.manager_view.show_message(self, success_message)
            else:
                self.manager_view.show_message(self, cannot_save_message)

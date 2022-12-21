#!/usr/bin/env python
# coding: utf-8

from model.match_model import Match
from model.round_model import Round
from model.player_model import Player
from controller.manager_controller import ManagerController
from controller.player_controller import PlayerController
from view.manager_view import ManagerView
from view.base_view import View
from view.player_view import PlayerView
import datetime


class TournamentController:
    def __init__(self, model, view):
        self.tournament_model = model
        self.tournament_view = view
        self.base_view = View()
        self.manager_view = ManagerView()
        self.manager_controller = ManagerController(ManagerView)
        self.player_controller = PlayerController(Player, PlayerView)
        self.match_model = Match
        self.round_model = Round
        self.error_message = "Commande non valide. Veuillez réessayer."
        self.round_counter = 1

    # MENU DU TOURNOIS

    def start_tournament_menu(self):
        self.tournament_view.show_tournament_menu(self)
        menu_message = "Choisissez une option : "

        while True:
            user_choice = self.manager_view.prompt_command(menu_message)
            if user_choice == '1':
                self.launch_tournament_flow()
            elif user_choice == '2':
                self.update_tournament()
            elif user_choice == '3':
                return
            else:
                self.manager_view.show_message(self.error_message)
            self.start_tournament_menu()
            return

    # LANCER LES ÉTAPES DE LA CREATION D'UN TOURNOIS

    def launch_tournament_flow(self):
        tournament = self.create_tournament()
        if tournament:
            pair_message = """
                Souhaitez-vous générer des paires pour les matchs ? (o/n):
            """
            user_choice = self.manager_view.prompt_command(pair_message)
            if user_choice == 'o':
                self.pairing(tournament)
            elif user_choice == 'n':
                return
            else:
                self.manager_view.show_message(self.error_message)

    # CREER UN TOURNOIS

    def create_tournament(self):
        input_tournament = [
            "le nom du tournois : ",
            "le lieu du tournois : ",
            "la date de début du tournois (jj/mm/aaaa) : ",
            "la date de fin du tournois (jj/mm/aaaa) : ",
            "entrez le nombre de round : ",
            "sélectionnez le type de temps",
            "remarques générales : ",
        ]
        message = ["sélectionnez le type de temps"]
        choices = ["bullet", "blitz", "coup rapide"]

        tournament = self.manager_controller.check_user_input(
            input_tournament,
            message,
            choices
            )
        minimum_count = 2
        sucessfully_created_message = "Votre tournois a bien été sauvegardé."
        tournament_property_count = len(input_tournament) + minimum_count
        round_index = 5
        players_index = 6
        if tournament:
            players = self.player_controller.add_player_to_tournament()
            if len(tournament) == len(input_tournament):
                tournament.insert(round_index, None)
                tournament.insert(players_index, None)
            elif len(tournament) < minimum_count:
                while len(tournament) < tournament_property_count:
                    tournament.append(None)
            elif len(tournament) > round_index-1:
                while len(tournament) < tournament_property_count:
                    tournament.append(None)
                tournament.insert(round_index, None)
                tournament.insert(players_index, None)
            if players:
                tournament.insert(players_index, players)
            self.tournament_model.save(self, tournament)
            self.manager_view.show_message(sucessfully_created_message)
            return tournament

    # METTRE A JOUR UN TOURNOIS

    def update_tournament(self):
        tournaments = self.tournament_model
        self.manager_controller.update_process(tournaments)

    # ALGORITHME DE TRI POUR SYSTEME DE TOURNOIS SUISSE

    def pairing(self, tournament):
        self.round_counter = 1
        ranking_error = "Il semble que tous les joueurs ne soient classés"
        tournament = self.tournament_model.get(self, 21)
        players = tournament[6]
        existing_pairs = []

        if any(player['ranking'] for player in players):
            ranked_list, existing_pairs = self.create_first_round(
                players, existing_pairs)
            round_name = self.define_round()
            self.manager_view.show_json(existing_pairs)
            score_base_list = self.register_result(
                ranked_list, round_name, tournament)

        if score_base_list:
            self.create_round(score_base_list, existing_pairs, tournament)
        else:
            self.manager_view.show_message(ranking_error)

    def create_first_round(self, players, existing_pairs):
        # Triez tous les joueurs en fonction de leur classement
        ranked_list = sorted(players,
                             key=lambda x: x['ranking'],
                             reverse=False)

        # Divisez les joueurs en deux moitiés
        high_ranked = ranked_list[:len(ranked_list)//2]
        low_ranked = ranked_list[len(ranked_list)//2:]

        index_count = 0
        max_index_count = 4
        score_base_list = []

        # Le meilleur joueur de la moitié supérieure
        # est jumelé avec le meilleur joueur de
        # la moitié inférieure, et ainsi de suite
        while index_count < max_index_count:
            player_one = high_ranked[index_count].copy()
            player_two = low_ranked[index_count].copy()
            created_pair = [player_one, player_two]
            existing_pairs.append(created_pair)
            score_base_list.append(player_one.copy())
            score_base_list.append(player_two.copy())
            index_count += 1
        return score_base_list, existing_pairs

    def create_round(self, score_base_list, existing_pairs, tournament):
        self.round_counter += 1
        continue_message = "Souhaitez-vous ajouter un autre round ? (o/n): "
        response = self.manager_view.prompt_command(continue_message)
        if response == "o":
            if 'score_player' in score_base_list[0]:
                score_list = sorted(
                    score_base_list,
                    key=lambda player: player['score_player'],
                    reverse=True
                )
                index_player_one = 0
                index_player_two = index_player_one + 1
                match_list = []
                new_list = []
                max_match_count = 4
                list_copy = score_list.copy()

                while len(match_list) < max_match_count:
                    x = self.check_pair(
                        new_list,
                        match_list,
                        list_copy,
                        index_player_one,
                        index_player_two,
                        existing_pairs
                    )
                    if x == 'stop':
                        break

                if len(match_list) == max_match_count:
                    round_name = self.define_round()
                    self.manager_view.show_json(match_list)
                    self.register_result(new_list, round_name, tournament)
                    return self.create_round(new_list,
                                             existing_pairs, tournament)
            else:
                requirement_message = """
                    Les conditions n'ont pas été remplie pour continuer
                """
                self.manager_view.show_message(requirement_message)
        elif response == "n":
            return
        else:
            self.manager_view.show_message(self.error_message)

    def check_pair(
            self, new_list, match_list, list_copy,
            index_one, index_two, existing_pairs):
        error_message = "Il semble qu'il n'y ai plus de combinaisons possibles"
        try:
            p_one = list_copy[index_one]
            p_two = list_copy[index_two]
            pair = [p_one, p_two]
            x = list_copy.copy()
            one = x[index_one].copy()
            one.pop('score_player')
            two = x[index_two].copy()
            two.pop('score_player')
            pair = [one, two]

            if pair in existing_pairs:
                index_two += 1
                return self.check_pair(
                    new_list,
                    match_list,
                    list_copy,
                    index_one,
                    index_two,
                    existing_pairs
                )
            else:
                new_list.append(p_one)
                new_list.append(p_two)
                list_copy.pop(index_one)
                list_copy.pop(index_two-1)
                existing_pairs.append(pair)
                match_list.append(pair)
                return new_list, match_list, existing_pairs
        except IndexError:
            self.manager_view.show_message(error_message)
            return 'stop'

    def register_result(self, match_list, round_name, tournament):
        max_match_count = 3
        match_count = 0
        player_count = 0
        counter = 0
        score_message = "Veuillez entrer le score du joueur/joueuse : "
        interrupt_message = "Vous venez d'interrompre votre action"
        successfully_registered_message = "Le score a bien été enregistré"
        wrong_score_message = """
            Le score ne peut être que 0, 1 ou 0.5. Veuillez réessayer
        """
        while match_count <= max_match_count:
            player = match_list[counter]
            player_message = """

			----------------------- MATCH """ + str(match_count+1) + """ -----------------------

			----------------------- JOUEUR """ + str(player_count+1) + """ -----------------------

            """

            self.manager_view.show_message(player_message)
            self.manager_view.show_json(player)
            response = self.manager_view.prompt_command(score_message)
            if response == "1" or response == "0" or response == "0.5":
                result = float(response)
                if 'score_player' in player:
                    player['score_player'] = player['score_player'] + result
                else:
                    player['score_player'] = result
                self.manager_view.show_message(successfully_registered_message)
                player_count += 1
                if player_count > 1:
                    player_count = 0
                    match_count += 1
                counter += 1
            elif response == "quit":
                self.manager_view.show_message(interrupt_message)
                break
            else:
                self.manager_view.show_message(wrong_score_message)
        self.save_round(round_name, match_list, tournament)
        return match_list

    def save_round(self, round_name, round_instance, tournament):
        instance = []
        matchs = list()
        round_instance = round_instance.copy()
        start_date = datetime.datetime.now()
        start_at = start_date.strftime('%d/%m/%Y')
        ended_round = "Le round est-il terminé ? (o/n): "
        while True:
            round_status = self.manager_view.prompt_command(ended_round)
            if round_status == "o":
                finish_date = datetime.datetime.now()
                finish_at = finish_date.strftime('%d/%m/%Y')
                break
            elif round_status == "n":
                finish_at = None
                break
            else:
                self.manager_view.show_message(self.error_message)

        for i in range(0, len(round_instance), 2):
            matchs.append(round_instance[i:i+2])

        for x in range(4):
            player_one = matchs[x][0].copy()
            player_one.pop('score_player')
            player_two = matchs[x][1].copy()
            player_two.pop('score_player')
            match_instance = [
                [player_one, {'score_player': matchs[x][0]['score_player']}],
                [player_two, {'score_player': matchs[x][1]['score_player']}]
            ]
            instance.append(match_instance)
            self.match_model.save(self, match_instance)

        round_object = [{
            'name': round_name,
            'round': instance,
            'start_at': start_at,
            'finish_at': finish_at
            }]
        self.round_model.save(self, round_object)

        if tournament[5]:
            new_value = tournament[5] + [round_object]
        else:
            new_value = tournament[5] = [round_object]
        tournament_name = tournament[0]
        self.tournament_model.update(
            self, 'rounds', new_value, tournament_name
        )

    def define_round(self):
        round_count = "Round " + str(self.round_counter)
        round_message = """

		----------------------- """ + round_count + """ -----------------------

        """
        self.manager_view.show_message(round_message)
        return round_count

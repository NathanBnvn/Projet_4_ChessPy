#!/usr/bin/env python
# coding: utf-8

from controller.manager_controller import ManagerController
from view.manager_view import ManagerView


class PlayerController:
    def __init__(self, model, view):
        self.player_model = model
        self.player_view = view
        self.manager_view = ManagerView()
        self.manager_controller = ManagerController(ManagerView)
        self.error_message = "Commande non valide. Veuillez réessayer."

    def start_player_menu(self):
        self.player_view.show_player_menu(self)
        menu_message = "Choisissez une option : "
        while True:
            user_choice = self.manager_view.prompt_command(menu_message)
            if user_choice == '1':
                self.create_player()
            elif user_choice == '2':
                self.update_player()
            elif user_choice == '3':
                return
            else:
                self.manager_view.show_message(self.error_message)
            self.start_player_menu()
            return

    def create_player(self):
        input_player = [
            "le nom du joueur/joueuse : ",
            "le prénom du joueur/joueuse : ",
            "la date de naissance du joueur/joueuse (jj/mm/aaaa) : ",
            "sélectionnez le sexe du joueur/joueuse",
            "la place du joueur/joueuse dans le classement : ",
        ]
        message = input_player[4]
        choices = ["masculin", "féminin"]
        player = self.manager_controller.check_user_input(
            input_player, message, choices
            )
        sucessfully_created_message = "Votre joueur/joueuse à bien été crée."

        if player:
            if len(player) < len(input_player):
                while len(player) < len(input_player):
                    player.append(None)
            self.player_model.save(self, player)
            self.manager_view.show_message(sucessfully_created_message)
        return player

    def add_player(self):
        players = self.player_model.get_all(self)
        self.manager_view.show_json(players)
        selected_id = self.manager_controller.check_id_input(len(players))
        if selected_id:
            player = self.player_model.get(self, selected_id)
        return player

    def add_player_to_tournament(self):
        add_player_message = """
            Souhaitez-vous ajouter 8 joueurs aux tournois ? (o/n) :
            """
        add_player_response = self.manager_view.prompt_command(
            add_player_message)
        if add_player_response == "o":
            players = self.add_or_create_player()
            return players
        elif add_player_response == "n":
            return
        else:
            self.manager_view.show_message(self.error_message)
        return self.add_player_to_tournament()

    def add_or_create_player(self):
        tournament_players = []
        max_player_count = 8
        player_count = 1
        create_or_add_message = """
            Souhaitez-vous créer des joueurs ou en ajouter ? (creer/ajouter) :
            """
        create_or_add_response = self.manager_view.prompt_command(
            create_or_add_message)
        if create_or_add_response == "creer":
            while player_count <= max_player_count:
                tournament_player = self.create_player()
                tournament_players.append(tournament_player)
                player_count += 1
            return tournament_players
        elif create_or_add_response == "ajouter":
            successfully_added_message = """
                Votre joueuse/joueur a bien été ajouté
                """
            while player_count <= max_player_count:
                player = self.add_player()
                if player:
                    tournament_players.append(player)
                    self.manager_view.show_message(successfully_added_message)
                    player_count += 1
                else:
                    break
            return tournament_players
        else:
            self.manager_view.show_message(self.error_message)
            return self.add_or_create_player()

    def update_player(self):
        players = self.player_model
        self.manager_controller.update_process(players)

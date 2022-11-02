#!/usr/bin/env python
# coding: utf-8

from model.player_model import Player
from model.tournament_model import Tournament
from view.base_view import View
from view.manager_view import ManagerView

class ReportController:

    def __init__(self, view):
        self.report_view = view
        self.base_view = View
        self.manager_view = ManagerView
        self.player_model = Player
        self.tournament_model = Tournament


    # MENU REPORT

    def start_report_menu(self):
        self.report_view.show_report_menu(self)
        menu_message = "Choisissez une option : "
        error_message = "Commande non valide. Veuillez réessayer."
        
        while True:
            user_choice = self.manager_view.prompt_command(self, menu_message)
            
            if user_choice == '1':
                self.all_player_alphabetical()
            elif user_choice == '2':
                self.all_player_by_ranks()
            elif user_choice == '3':
                self.tournament_players_alphabetical()
                print(user_choice)
            elif user_choice == '4':
                self.tournament_players_by_ranks()
                print(user_choice)
            elif user_choice == '5':
                self.all_tournament()
            elif user_choice == '6':
                self.tournament_rounds()
                print(user_choice)
            elif user_choice == '7':
                self.tournament_matches()
                print(user_choice)
            elif user_choice == '8':
                return
            else:
                self.manager_view.show_message(self, error_message)
            
            self.start_report_menu()
            return


    def all_player_alphabetical(self):
        # tous les joueurs par ordre alphabétique
        data = self.player_model.get_all(self)
        players = self.check_data_exist(data)  
        alphabetical_list = sorted(players, key=lambda x: x['last_name'], reverse=False)
        # @TODO implement view function
        print(alphabetical_list)
        self.return_to_menu()


    def all_player_by_ranks(self):
        # # tous les joueurs par classement
        data = self.player_model.get_ranked_player(self)
        players = self.check_data_exist(data)       
        ranked_list = sorted(players, key=lambda x: x['ranking'], reverse=False)

        # @TODO implement view function
        print(ranked_list)
        self.return_to_menu()


    def tournament_players_alphabetical(self):
        # tous les joueurs d'un tournois par ordre alphabetique
        # @TODO implement view function
        self.return_to_menu()
        pass


    def tournament_players_by_ranks(self):
         # tous les joueurs d'un tournois par classement
         # @TODO implement view function
        self.return_to_menu()
        pass


    def all_tournament(self):
         # tous les tournois
        tournaments = self.tournament_model.get_all(self)
        self.check_data_exist(tournaments)
        # @TODO implement view function
        self.return_to_menu()


    def tournament_rounds(self):
        # tous les joueurs d'un tournois
        # @TODO implement view function
        self.return_to_menu()
        pass


    def tournament_matches(self):
        # tous les matchs d'un tournois
        # @TODO implement view function
        self.return_to_menu()
        pass


    def check_data_exist(self, data):
        no_data_message = "Il n'y a pas de données pour le moment"
        
        if not data:
            self.manager_view.show_message(self, no_data_message)
        else:
            return data


    def return_to_menu(self):
        return_message = "Tapez sur une touche pour retourner au menu : "
        
        while True:
            back_to_menu = self.manager_view.prompt_command(self, return_message)
            
            if back_to_menu:
                break
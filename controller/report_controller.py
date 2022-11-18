#!/usr/bin/env python
# coding: utf-8

from model.player_model import Player
from model.tournament_model import Tournament
from controller.manager_controller import ManagerController
from view.base_view import View
from view.manager_view import ManagerView

class ReportController:

    def __init__(self, view):
        self.report_view = view
        self.base_view = View()
        self.manager_view = ManagerView()
        self.manager_controller = ManagerController(ManagerView)
        self.player_model = Player
        self.tournament_model = Tournament


    # MENU REPORT

    def start_report_menu(self):
        self.report_view.show_report_menu(self)
        menu_message = "Choisissez une option : "
        error_message = "Commande non valide. Veuillez réessayer."
        
        while True:
            user_choice = self.manager_view.prompt_command(menu_message)
            
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
                self.tournament_rounds(user_choice)
                print(user_choice)
            elif user_choice == '7':
                self.tournament_matches(user_choice)
                print(user_choice)
            elif user_choice == '8':
                return
            else:
                self.manager_view.show_message(error_message)
            
            self.start_report_menu()
            return


    # Tous les joueurs par ordre alphabétique

    def all_player_alphabetical(self):
        data = self.player_model.get_all(self)
        players = self.check_data_exist(data)  
        alphabetical_list = sorted(players, key=lambda x: x['last_name'], reverse=False)
        self.manager_view.show_json(alphabetical_list)
        self.return_to_menu()


    # Tous les joueurs par classement

    def all_player_by_ranks(self):
        data = self.player_model.get_ranked_player(self)
        players = self.check_data_exist(data)       
        ranked_list = sorted(players, key=lambda x: x['ranking'], reverse=False)
        self.manager_view.show_json(ranked_list)
        self.return_to_menu()


    def list_tournaments(self):
        data = self.tournament_model.get_all(self)
        tournaments = self.check_data_exist(data)
        self.manager_view.show_json(tournaments)
        return tournaments


    # Tous les joueurs d'un tournois par ordre alphabetique

    def tournament_players_alphabetical(self):
        tournaments = self.list_tournaments()
        tournament_id = self.manager_controller.check_id_input(len(tournaments))
        if tournament_id:
            tournament = self.tournament_model.get(self, tournament_id)
            selected_tournament = self.check_data_exist(tournament)
            players = selected_tournament['players']
            selected_players = self.check_data_exist(players)
            if selected_players:
                alphabetical_list = sorted(selected_players, key=lambda x: x['last_name'], reverse=False)
                self.manager_view.show_json(alphabetical_list)
        self.return_to_menu()


    # Tous les joueurs d'un tournois par classement

    def tournament_players_by_ranks(self):
        tournaments = self.list_tournaments()
        tournament_id = self.manager_controller.check_id_input(len(tournaments))
        if tournament_id:
            tournament = self.tournament_model.get(self, tournament_id)
            selected_tournament = self.check_data_exist(tournament)
            players = selected_tournament['players']
            selected_players = self.check_data_exist(players)
            if selected_players:
                ranked_list = sorted(selected_players, key=lambda x: x['ranking'], reverse=False)
                self.manager_view.show_json(self, ranked_list)
        self.return_to_menu()


    # Tous les tournois

    def all_tournament(self):
        self.list_tournaments()
        self.return_to_menu()


    # L'ensemble des rounds d'un tournois

    def tournament_rounds(self, user_choice):
        tournaments = self.list_tournaments()
        tournament_id = self.manager_controller.check_id_input(len(tournaments))
        if tournament_id:
            tournament = self.tournament_model.get(self, tournament_id)
            selected_tournament = self.check_data_exist(tournament)
            rounds = selected_tournament['rounds']
            selected_rounds = self.check_data_exist(rounds)
            if selected_rounds:
                ranked_list = sorted(selected_rounds, key=lambda x: x['ranking'], reverse=False)
                self.manager_view.show_json(ranked_list)
                
                # L'ensemble des matchs d'un tournois
                if user_choice == 7:
                    print('matches... ')
        self.return_to_menu()

    def check_data_exist(self, data):
        no_data_message = "Il n'y a pas de données pour le moment"
        
        if not data or data == None:
            self.manager_view.show_message(no_data_message)
        else:
            return data


    def return_to_menu(self):
        return_message = "Tapez sur une touche pour retourner au menu : "
        
        while True:
            back_to_menu = self.manager_view.prompt_command(return_message)
            
            if back_to_menu:
                break
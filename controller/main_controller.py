#!/usr/bin/env python
# coding: utf-8

from .player_controller import PlayerController
from .tournament_controller import TournamentController
from .report_controller import ReportController
from .manager_controller import ManagerController
from model.tournament_model import Tournament
from model.player_model import Player
from view.base_view import View
from view.manager_view import ManagerView
from view.player_view import PlayerView
from view.report_view import ReportView
from view.tournament_view import TournamentView


class MainController:
    def __init__(self):
        self.player_controller = PlayerController(Player, PlayerView)
        self.tournament_controller = TournamentController(
            Tournament, TournamentView)
        self.report_controller = ReportController(ReportView)
        self.manager_controller = ManagerController(ManagerView)
        self.base_view = View()
        self.manager_view = ManagerView()

    # MENU PRINCIPAL

    def start_menu(self):
        menu_message = "Choisissez un menu : "
        error_message = "Commande non valide. Veuillez réessayer."
        quit_message = "Merci d'avoir utilisé ChessPy. À bientôt 👋"

        self.base_view.show_menu_command()
        user_choice = self.manager_view.prompt_command(menu_message)
        self.manager_controller.clean_terminal()

        while True:
            if user_choice == '1':
                self.tournament_controller.start_tournament_menu()
                self.start_menu()
            elif user_choice == '2':
                self.player_controller.start_player_menu()
                self.start_menu()
            elif user_choice == '3':
                self.report_controller.start_report_menu()
                self.start_menu()
            elif user_choice == '4':
                self.manager_view.show_message(quit_message)
                exit()
            else:
                self.manager_view.show_message(error_message)
                self.start_menu()

    def run(self):
        welcome_message = "Bienvenue sur ChessPy 🖖"
        self.manager_view.show_message(welcome_message)
        self.start_menu()

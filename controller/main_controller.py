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
		self.tournament_controller = TournamentController(Tournament, TournamentView)
		self.report_controller = ReportController(ReportView)

		# Instancier la vue
		self.base_view = View
		self.manager_view = ManagerView
		self.manager_controller = ManagerController


	def start_menu(self):
		menu_message = "Choisissez un menu : "
		error_message = "Commande non valide. Veuillez réessayer."
		quit_message = "Merci d'avoir utilisé ChessPy. À bientôt 👋"
		
		self.base_view.show_menu_command(self)
		user_choice = self.manager_view.prompt_command(self, menu_message)
		self.manager_controller.clean_terminal(self)

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
				self.manager_view.show_message(self, quit_message)
				exit()
			else:
				self.manager_view.show_message(self, error_message)
				self.start_menu()


	# @TODO Déplacer la function dans un autre controller
	def register_result(self):
		# Sauvegarder le résultat d'un match 
		pass


	def run(self):
		self.start_menu()
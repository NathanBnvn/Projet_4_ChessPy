#!/usr/bin/env python
# coding: utf-8

from controller.manager_controller import ManagerController
from controller.player_controller import PlayerController
from view.manager_view import ManagerView
from view.base_view import View

class TournamentController:
	def __init__(self, model, view):
		self.tournament_model = model
		self.tournament_view = view
		self.base_view = View
		self.manager_view = ManagerView
		self.manager_controller = ManagerController
		self.player_controller = PlayerController

	# MENU DU TOURNOIS
	
	def start_tournament_menu(self):
		self.tournament_view.show_tournament_menu(self)
		menu_message = "Choisissez une option : "
		error_message = "Commande non valide. Veuillez réessayer."

		while True:
			user_choice = self.manager_view.prompt_command(self, menu_message)

			if user_choice == '1':
				self.create_tournament()
			elif user_choice == '2':
				self.update_tournament()
			elif user_choice == '3':
				return
			else:
				self.base_view.show_message(self, error_message)
			
			self.start_tournament_menu()
			return
	
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

		tournament = self.manager_controller.check_user_input(self, input_tournament, message, choices)
		tournament_players = self.player_controller.add_player_to_tournament(self)
		sucessfully_created_message = "Votre tournois a bien été sauvegardé."
		print(tournament)
		print(tournament_players)
		if tournament:
			if len(tournament) < len(input_tournament):
				while len(tournament) < len(input_tournament):
					tournament.append(None)
			self.tournament_model.save(self, tournament)
			self.manager_view.show_message(self, sucessfully_created_message)


	# METTRE A JOUR UN TOURNOIS

	def update_tournament(self):
		tournaments = self.tournament_model
		self.manager_controller.update_process(self, tournaments)

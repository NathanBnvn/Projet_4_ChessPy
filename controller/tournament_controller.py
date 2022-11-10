#!/usr/bin/env python
# coding: utf-8

from model.match_model import Match
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
		self.match_model = Match

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
		
		sucessfully_created_message = "Votre tournois a bien été sauvegardé."
		tournament_property_count = len(input_tournament) + 2
		players_index = 6
		if tournament:
			tournament_players = self.player_controller.add_player_to_tournament(self)
			if len(tournament) < tournament_property_count:
				while len(tournament) < tournament_property_count:
					tournament.append(None)
			if tournament_players:
					tournament.insert(players_index, tournament_players)
			self.tournament_model.save(self, tournament)
			self.manager_view.show_message(self, sucessfully_created_message)


	# METTRE A JOUR UN TOURNOIS

	def update_tournament(self):
		tournaments = self.tournament_model
		self.manager_controller.update_process(self, tournaments)


	# ALGORITHME DE TRI POUR SYSTEME DE TOURNOIS SUISSE

	def pairing(self, players):
		# Triez tous les joueurs en fonction de leur classement
		ranked_list = sorted(players, key=lambda x: x['ranking'], reverse=False)
		
		# Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
		high_ranked = ranked_list[:len(ranked_list)//2]
		low_ranked = ranked_list[len(ranked_list)//2:]
		
		# Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur
		# de la moitié inférieure, et ainsi de suite
		x = 0
		y = 3
		while x < y:
			m = ([high_ranked[x], None], [low_ranked[x], None])
			self.match_model.serializer(self, m)
			x += 1
			pass
			
		self.register_result()


	def register_result(self):
		pass
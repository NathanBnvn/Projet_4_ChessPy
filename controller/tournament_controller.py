#!/usr/bin/env python
# coding: utf-8

from model.match_model import Match
from model.player_model import Player
from controller.manager_controller import ManagerController
from controller.player_controller import PlayerController
from view.manager_view import ManagerView
from view.base_view import View
from view.player_view import PlayerView

class TournamentController:
	def __init__(self, model, view):
		self.tournament_model = model
		self.tournament_view = view
		self.base_view = View()
		self.manager_view = ManagerView()
		self.manager_controller = ManagerController(ManagerView)
		self.player_controller = PlayerController(Player, PlayerView)
		self.match_model = Match
		self.error_message = "Commande non valide. Veuillez réessayer."

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
			elif user_choice == '4':
				self.pairing()
			else:
				self.manager_view.show_message(self.error_message)
			
			self.start_tournament_menu()
			return
	

	# LANCER LES ÉTAPES DE LA CREATION D'UN TOURNOIS

	def launch_tournament_flow(self):
		tournament = self.create_tournament()
		if tournament:
			pair_message = "Souhaitez-vous générer des paires pour les matchs ? (o/n): "
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

		tournament = self.manager_controller.check_user_input(input_tournament, message, choices)
		
		sucessfully_created_message = "Votre tournois a bien été sauvegardé."
		tournament_property_count = len(input_tournament) + 2
		empty_index = 5
		players_index = 6
		if tournament:
			tournament_players = self.player_controller.add_player_to_tournament()
			if len(tournament) < tournament_property_count:
				while len(tournament) < tournament_property_count:
					# @TODO fix properly
					tournament.insert(empty_index, None)
			if tournament_players:
				tournament.insert(players_index, tournament_players)
			self.tournament_model.save(self, tournament)
			self.manager_view.show_message(sucessfully_created_message)
			return tournament 


	# METTRE A JOUR UN TOURNOIS

	def update_tournament(self):
		tournaments = self.tournament_model
		self.manager_controller.update_process(tournaments)


	# ALGORITHME DE TRI POUR SYSTEME DE TOURNOIS SUISSE

	def pairing(self):
		round_counter = 1
		first_round_message = """

		----------------------- Round """ + str(round_counter) + """-----------------------
		
		"""
		tournament = self.tournament_model.get(self, 21)
		players = tournament['players']

		# players = tournament[6]

		# Triez tous les joueurs en fonction de leur classement
		ranked_list = sorted(players, key=lambda x: x['ranking'], reverse=False)
		
		# Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
		high_ranked = ranked_list[:len(ranked_list)//2]
		low_ranked = ranked_list[len(ranked_list)//2:]

		
		# Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur
		# de la moitié inférieure, et ainsi de suite
		index_count = 0
		max_index_count = 4
		paris = []
		while index_count < max_index_count:
			pair = ([high_ranked[index_count], {'score_player': None}], [low_ranked[index_count], {'score_player': None}])
			#self.match_model.serializer(self, pair)
			paris.append(pair)
			index_count += 1
		
		self.manager_view.show_message(first_round_message)
		self.manager_view.show_json(paris)
		
		pairs = self.register_result(paris)
		
		# triez tous les joueurs en fonction de leur nombre total de points. 
		print(pairs)
		#score_base_list = sorted(paris, key=lambda x: x[0], reverse=False)
		#print(score_base_list)
		
		# Si plusieurs joueurs ont le même nombre de points, 
		# triez-les en fonction de leur rang
		#ranked_list = sorted(paris, key=lambda x: x['ranking'], reverse=False)

		# Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. 
		# Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
		# Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.
		
		#continue_message = "Souhaitez-vous ajouter un autre round ?"
		#self.manager_view.prompt_command(continue_message)
			


	def register_result(self, paris):
		y = 3
		x = 0
		z = 0
		score_message = "Veuillez entrer le score du joueur/joueuse : "
		successfully_registered_message = "Le score a bien été enregistré"
		wrong_score_message = "Le score ne peut être que 0, 1 ou 0.5. Veuillez réessayer s'il vous plait"
		while x <= y:
			u = paris[x][z]
			player_message = """

			----------------------- MATCH """ + str(x+1) + """ -----------------------

			----------------------- JOUEUR """ + str(z+1) + """ -----------------------

			"""

			self.manager_view.show_message(player_message)
			self.manager_view.show_json(u)
			m = self.manager_view.prompt_command(score_message)
			# @TODO implement float acceptance
			if m == "1" or m == "0" or m == "0.5":
				if m == "0.5":
					r = float(m)
				else:
					r = int(m)
				u[1]['score_player'] = r
				self.manager_view.show_message(successfully_registered_message)
				z += 1
				if z > 1:
					z = 0
					x += 1
			else:
				self.manager_view.show_message(wrong_score_message)
		return paris
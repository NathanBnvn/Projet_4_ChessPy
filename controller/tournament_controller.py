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
			end_tournament_message = "Le tournois est-il terminé ? (o/n): "
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
		minimum_count = 2
		sucessfully_created_message = "Votre tournois a bien été sauvegardé."
		tournament_property_count = len(input_tournament) + minimum_count
		round_index = 5
		players_index = 6
		if tournament:
			tournament_players = self.player_controller.add_player_to_tournament()
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
		self.round_counter = 1
		round_count = "Round " + str(self.round_counter)
		round_message = """

		----------------------- """ + round_count + """ -----------------------
		
		"""
		tournament = self.tournament_model.get(self, 21)
		players = tournament['players']

		# players = tournament[6]
		existing_pairs = []
		ranked_list, existing_pairs = self.create_first_round(players, existing_pairs)
		self.manager_view.show_message(round_message)
		self.manager_view.show_json(existing_pairs)
		score_base_list = self.register_result(ranked_list)
		#if pairs:
			# save model
			#round_model
			
		if score_base_list:

		
		#match_count = 0
		#player_count = 0
		#print(len(pairs))
		#print(pairs[match][player])
		#print(pairs[match][player][1]['score_player'])

			self.create_round(score_base_list, existing_pairs)



	def create_first_round(self, players, existing_pairs):
		# Triez tous les joueurs en fonction de leur classement
		ranked_list = sorted(players, key=lambda x: x['ranking'], reverse=False)
		
		# Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
		high_ranked = ranked_list[:len(ranked_list)//2]
		low_ranked = ranked_list[len(ranked_list)//2:]

		index_count = 0
		max_index_count = 4
		score_base_list = []

		# Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur
		# de la moitié inférieure, et ainsi de suite
		while index_count < max_index_count:
			# pair = (
			# 	[high_ranked[index_count], {'score_player': None}], 
			# 	[low_ranked[index_count], {'score_player': None}]
			# )
			# pairs.append(pair)
			
			player_one = high_ranked[index_count].copy()
			player_two = low_ranked[index_count].copy()
			created_pair = [player_one, player_two]
			existing_pairs.append(created_pair)
			
			score_base_list.append(player_one)
			score_base_list.append(player_two)

			index_count += 1
		
		return score_base_list, existing_pairs


	def create_round(self, score_base_listx, existing_pairs):
		self.round_counter += 1
		round_count = "Round " + str(self.round_counter)
		round_message = """

		----------------------- """ + round_count + """ -----------------------
		
		"""
		continue_message = "Souhaitez-vous ajouter un autre round ? (o/n) "
		r = self.manager_view.prompt_command(continue_message)
		if r == "o":
			if 'score_player' in score_base_listx[0]:
				self.manager_view.show_message(round_message)
				sb_list = sorted(score_base_listx, key=lambda x: x['score_player'], reverse=True)
				

				for e in existing_pairs[0]:
					e.pop('score_player')

				print(existing_pairs)
				# triez tous les joueurs en fonction de leur nombre total de points.
				# Si plusieurs joueurs ont le même nombre de points, 
				# triez-les en fonction de leur rang

				yw = 0
				wy = yw + 1
				max_player_count = 8
				nwlst = []
				nwsortlst = []
				print(existing_pairs)

				# Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. 
				# Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
				# Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.
			
				# ------------------ v1 -----------------------------
				while yw < max_player_count:
					# Boucle joueur 1 associé au joueur avec le score le plus proche
					# Si le joueur 1 a déjà jouer avec joueur 2 alors jouer avec joueur 3 
					# if pr in existing_pairs:
					# 	wy += 1
					# else:
					# while pr in prs:
					# wy + 1
					k = [sb_list[yw], sb_list[wy]]
					w = k.copy()
					w.pop('score_player')

					if w in existing_pairs:
						while k in existing_pairs:
							wy += 1
						
						print("Pair already exist")
					else:
						zw = sb_list[yw].copy()
						swz = sb_list[wy].copy()
						existing_pairs.append(k)
						nwlst.append(k)
						nwsortlst.append(zw)
						nwsortlst.append(swz)
					yw += 2
					wy += 2
				
				self.manager_view.show_json(nwlst)
				self.register_result(nwsortlst)
				return self.create_round(nwsortlst, existing_pairs)
			else:
				requirement_message = "Les conditions ont été non remplie pour continuer"
				self.manager_view.show_message(requirement_message)

		elif r == "n":
			return
		else:
			self.manager_view.show_message(self.error_message)


	def register_result(self, sbl):
		y = 3
		x = 0
		z = 0
		px = 0
		score_message = "Veuillez entrer le score du joueur/joueuse : "
		interrupt_message = "Vous venez d'interrompre votre action"
		successfully_registered_message = "Le score a bien été enregistré"
		wrong_score_message = "Le score ne peut être que 0, 1 ou 0.5. Veuillez réessayer s'il vous plait"
		while x <= y:
			#u = paris[x][z]
			p = sbl[px]
			player_message = """

			----------------------- MATCH """ + str(x+1) + """ -----------------------

			----------------------- JOUEUR """ + str(z+1) + """ -----------------------

			"""

			self.manager_view.show_message(player_message)
			self.manager_view.show_json(p)
			m = self.manager_view.prompt_command(score_message)
			if m == "1" or m == "0" or m == "0.5":
				if m == "0.5":
					r = float(m)
				else:
					r = int(m)
				if 'score_player' in p: 
					p['score_player'] = p['score_player'] + r
				else:
					p['score_player'] = r
				self.manager_view.show_message(successfully_registered_message)
				z += 1
				if z > 1:
					z = 0
					x += 1
				px += 1
				#self.round_model.save(Match, paris[x])
			elif m == "quit":
				self.manager_view.show_message(interrupt_message)
				break
			else:
				self.manager_view.show_message(wrong_score_message)
		return sbl
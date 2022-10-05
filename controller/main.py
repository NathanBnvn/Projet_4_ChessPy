from secrets import choice
from view.base import Views
from view.player import PlayerView
from view.tournament import TournamentView
from model.tournament import Tournament
from model.player import Player

class Controller:

	def __init__(self,):
		# Instancier le model
 
		self.players = []
		self.tournament = Tournament
		# self.match = match
		# self.round = round

		# Instancier la vue
		self.base_view = Views
		self.player_view = PlayerView
		self.tournament_view = TournamentView

	# gestion des menus 
	# faire les différents menu de base 
	# structurer les choses plus simplement avant 
	# construire le flow pour mieux comprendre

	def start_menu(self):
		self.base_view.show_menu_command(self)
		user_choice = self.base_view.prompt_menu_command(self)
		
		while True:
			if user_choice == 't':
				self.create_tournament()
				self.base_view.show_menu_command(self)
				self.base_view.prompt_menu_command(self)
			elif user_choice == 'p':
				self.add_height_players()
				self.base_view.show_menu_command(self)
				self.base_view.prompt_menu_command(self)
			elif user_choice == 'q':
				print("Merci d'avoir utilisé ce programme. Au revoir")


	def create_tournament(self):
		tournament = self.tournament_view.prompt_tournament(self)
		if not tournament:
			return
		tournament = Tournament(
			tournament[0], 
			tournament[1], 
			tournament[2], 
			tournament[3], 
			tournament[4], 
			tournament[5], 
			tournament[6], 
			)


	def add_height_players(self):
		while len(self.players) < 3:
			player = self.player_view.prompt_player(self)
			if not player:
				return
			player = Player(
				player[0], 
				player[1], 
				player[2], 
				player[3], 
				player[4])
			self.players.append(player)


	def sort_players(self):
		# Au début du premier tour, triez tous les joueurs en fonction de leur classement.
		
		#if self.tournament.round_count == 1:

			# ranked_players = sorted(self.players, key=lambda x: x.ranking, reverse=False)
			# return ranked_players
				
		# else:
		#	pass

		# Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. 
		


		# Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
		pass


	def pair_players(self):
		# # Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
		# half = len(ranked_players) //2

		# Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure, et ainsi de suite. 
		# Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, 
		# le joueur 2 est jumelé avec le joueur 6, etc.
		# for hier_rank, lower_rank in zip(ranked_players, ranked_players[half:]):
		# 	match = Match([hier_rank, 0], [lower_rank, 0])
		
		# Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points. 
		# Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
		# Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. 
		# Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.

		# for player_one, player_two in zip(ranked_players[0::2], ranked_players[1::2]):
		# 	pass
		pass

	def register_result(self):
		# Sauvegarder le résultat d'un match
		pass

	def update_ranking(self):
		# Mettre à jour le classement 

		pass

	def finish_tournament(self):
		# Fin du tournois
		pass

	def generate_report(self):
		# Liste de tous les acteurs :
		
		# par ordre alphabétique ;
		#alphabetical_list = sorted(self.players, key=lambda x: x.last_name, reverse=False)
		#print(alphabetical_list)
		
		# par classement
		#ranked_list = sorted(self.players, key=lambda x: x.ranking, reverse=False)
		#print(ranked_list)

		# Liste de tous les joueurs d'un tournoi :
		# par ordre alphabétique ;
		# par classement.

		# Liste de tous les tournois.
		# Liste de tous les tours d'un tournoi.
		# Liste de tous les matchs d'un tournoi.
		pass

	def run(self):
		self.start_menu()
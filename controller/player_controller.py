from controller.manager_controller import ManagerController
from model.player_model import Player
from view.manager_view import ManagerView

class PlayerController:
	def __init__(self, model, view):
		self.player_model = model
		self.player_view = view
		self.manager_view = ManagerView
		self.manager_controller = ManagerController
	
	def start_player_menu(self):
		self.player_view.show_player_menu(self)
		menu_message = "Choisissez une option : "
		error_message = "Commande non valide. Veuillez réessayer."

		while True:
			user_choice = self.manager_view.prompt_command(self, menu_message)

			if user_choice == '1':
				self.create_player()
			elif user_choice == '2':
				print(user_choice)
			elif user_choice == '3':
				print(user_choice)
			elif user_choice == '4':
				return
			else:
				self.manager_view.show_message(self, error_message)
			
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
		message = "sélectionnez le sexe du joueur/joueuse"
		choices = ["masculin", "féminin"]
		player = self.manager_controller.check_user_input(self, input_player, message, choices)
		sucessfully_created_message = "Votre joueur/joueuse à bien été crée."

		if player:
			if len(player) < len(input_player):
				while len(player) < len(input_player):
					player.append(None)
			self.player_model.save(self, player)
			self.manager_view.show_message(self, sucessfully_created_message)
		return player


	def add_player_to_tournament(self):
		tournament_players = []
		max_count_player = 7
		count_player = 0
		add_player_message = "Souhaitez-vous ajouter 8 joueurs aux tournois ? (oui/non) : "
		add_player_response = self.manager_view.prompt_command(self, add_player_message)
		if add_player_response == "oui":
			while count_player <= max_count_player:
				tournament_player = self.player_controller.create_player(self)
				tournament_players.append(tournament_player)
				count_player += 1
			# Les joueurs dans la table tournois correspondent 
			# à la liste des indices
			# des instances du joueur stockées en mémoire.
			return tournament_players

	def update_player(self):
		pass


	def update_ranking(self):
		# Mettre à jour le classement 
		pass
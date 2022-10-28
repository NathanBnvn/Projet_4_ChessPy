from controller.manager_controller import ManagerController
from model.player_model import Player
from view.manager_view import ManagerView

class PlayerController:
	def __init__(self, model, view):
		self.players = []
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
				self.manager_view.error_message(self, error_message)
			
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
		if not player:
			return
		player = Player(
			player[0], 
			player[1], 
			player[2], 
			player[3], 
			player[4])
		self.players.append(player)


	def update_player(self):
		pass


	def update_ranking(self):
		# Mettre à jour le classement 
		pass
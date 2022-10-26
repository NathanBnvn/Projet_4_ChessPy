from model.player_model import Player
import inquirer

class PlayerController:
	def __init__(self, model, view):
		self.players = []
		self.player_model = model
		self.player_view = view

	
	def start_player_menu(self):
		self.player_view.show_player_menu(self)

		while True:
			user_choice = self.player_view.prompt_menu_command(self)

			if user_choice == 1:
				self.create_player()
			elif user_choice == 2:
				print(user_choice)
			elif user_choice == 3:
				print(user_choice)
			elif user_choice == 4:
				return
			else:
				print("Commande non valide. Veuillez réessayer.")
				self.start_player_menu()
			
			self.start_player_menu()
			return

	def create_player(self):
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


	def update_player(self):
		pass


	def update_ranking(self):
		# Mettre à jour le classement 
		pass
from model.player import Player
import inquirer

class PlayerController:
	def __init__(self, model, view):
		self.players = []
		self.player_model = model
		self.player_view = view

	def prompt_menu_command(self):
		user_choice = str(input())
		return user_choice
	
	def start_player_menu(self):
		self.player_view.show_player_menu(self)
		user_choice = self.prompt_menu_command()
		
		while True:
			if user_choice == '1':
				self.prompt_tournament(self)
				self.start_player_menu()
			elif user_choice == '2':
				print('2')
				self.start_player_menu()
			elif user_choice == '3':
				print('3')
				self.start_player_menu()
			elif user_choice == '4':
				return
			else:
				print("Commande non valide. Veuillez réessayer.")

	def prompt_player(self):
		last_name = str(input("tapez le nom du joueur/joueuse : "))
		first_name = str(input("tapez le prénom du joueur/joueuse : "))
		birth_date = str(input("tapez la date de naissance du joueur/joueuse : "))
		gender_list = [
            inquirer.List(
                "gender", 
                message="sélectionnez le sexe du joueur/joueuse", 
                choices=["masculin", "féminin"], 
            ),
        ]
		answers = inquirer.prompt(gender_list)
		gender = answers["gender"]
		ranking = int(input("tapez la place du joueur/joueuse dans le classement : "))
		player = [last_name, first_name, birth_date, gender, ranking]
		return player


	def add_player(self):
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
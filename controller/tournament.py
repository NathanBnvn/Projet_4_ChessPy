from model.tournament import Tournament
import inquirer

class TournamentController:
	def __init__(self, model, view):
		self.tournament = model
		self.tournament_view = view
	
	def prompt_menu_command(self):
		user_choice = str(input())
		return user_choice
	
	def start_tournament_menu(self):
		self.tournament_view.show_tournament_menu(self)
		user_choice = self.prompt_menu_command()
		
		while True:
			if user_choice == '1':
				self.prompt_tournament(self)
				self.start_tournament_menu()
			elif user_choice == '2':
				print('2')
				self.start_tournament_menu()
			elif user_choice == '3':
				print('3')
				self.start_tournament_menu()
			elif user_choice == '4':
				return
			else:
				print("Commande non valide. Veuillez réessayer.")
	
	def prompt_tournament(self):
		name = str(input("tapez le nom du tournois : "))
		place = str(input("tapez le lieu du tournois : "))
		start_date = str(input("tapez la date de début du tournois : "))
		end_date = str(input("tapez la date de fin du tournois : "))
		round_count = str(input("entrez le nombre de round : "))
		round_list = "instance de tours"
		players = "instance de player"
		control_list = [
            inquirer.List("control", 
                message="sélectionnez le type de temps",
                choices=["bullet", "blitz", "coup rapide"],
            ),
        ]
		answers = inquirer.prompt(control_list)
		time_check = answers["control"]
		description = str(input("remarques générales : "))
		tournament = [name, place, start_date, end_date, round_count, round_list, players, time_check, description]
        # return tournament
	
	def create_tournament(self, tournament_view):
		tournament = self.prompt_tournament()
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
	
	def update_tournament(self, tournament_view):
		pass

	def finish_tournament(self):
		# Fin du tournois
		pass
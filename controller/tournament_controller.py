from email import message
from model.tournament_model import Tournament
from controller.manager_controller import ManagerController
from view.manager_view import ManagerView
from view.base_view import View

class TournamentController:
	def __init__(self, model, view):
		self.tournament = model
		self.tournament_view = view
		self.base_view = View
		self.manager_view = ManagerView
		self.manager_controller = ManagerController
	
	def start_tournament_menu(self):
		self.tournament_view.show_tournament_menu(self)
		menu_message = "Choisissez une option : "
		error_message = "Commande non valide. Veuillez réessayer."

		while True:
			user_choice = self.manager_view.prompt_command(self, menu_message)

			if user_choice == '1':
				self.create_tournament()
			elif user_choice == '2':
				print(user_choice)
			elif user_choice == '3':
				print(user_choice)
			elif user_choice == '4':
				return
			else:
				self.base_view.error_message(self, error_message)
			
			self.start_tournament_menu()
			return

	def save():
		pass

	def create_tournament(self):
		# tournament = self.tournament_view.prompt_tournament(self)
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
		print(tournament)		
	
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
	
	def update_tournament(self):
		pass

	def finish_tournament(self):
		# Fin du tournois
		pass
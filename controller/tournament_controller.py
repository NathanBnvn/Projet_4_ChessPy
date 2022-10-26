from model.tournament_model import Tournament
from view.base_view import View
import datetime

class TournamentController:
	def __init__(self, model, view):
		self.tournament = model
		self.tournament_view = view
		self.base_view = View

	
	def start_tournament_menu(self):
		self.tournament_view.show_tournament_menu(self)

		while True:
			user_choice = self.tournament_view.prompt_menu_command(self)

			if user_choice == 1:
				self.create_tournament()
			elif user_choice == 2:
				print(user_choice)
			elif user_choice == 3:
				print(user_choice)
			elif user_choice == 4:
				return
			else:
				print("Commande non valide. Veuillez réessayer.")
				self.start_tournament_menu()
			
			self.start_tournament_menu()
			return
			


	
	def check_date(self, date):
		try:
			_ = datetime.datetime.strptime(date, "%d/%m/%Y")
		except ValueError:
			print("""
			
			Veuillez entrer la date dans un format valide !
			
			""")
			return self.tournament_view.prompt_menu_command(self)
	
	def save():
		pass

	def create_tournament(self):
		tournament = self.tournament_view.prompt_tournament(self)
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
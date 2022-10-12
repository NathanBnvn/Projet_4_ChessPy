from os import system, name
from view.base import Views
from .player import PlayerController
from .tournament import TournamentController
from .report import ReportController
from view.player import PlayerView
from model.tournament import Tournament
from view.tournament import TournamentView

# renommer main controller
# et segmenter le controller en plusieurs 
class MainController:

	def __init__(self):
		# self.match = match
		# self.round = round
		self.player_controller = PlayerController
		self.tournament_controller = TournamentController
		self.report_controller = ReportController

		# Instancier la vue
		self.base_view = Views

	# gestion des menus 
	# faire les différents menu de base 
	# structurer les choses plus simplement avant 
	# construire le flow pour mieux comprendre

	# définir des fonctions pour nettoyer le terminal
	def clean_terminal(self):
		    # for windows
			if name == 'nt':
				_ = system('cls')
			
			# for mac and linux(here, os.name is 'posix')
			else:
				_ = system('clear')

	def start_menu(self):
		self.clean_terminal()
		self.base_view.show_menu_command(self)
		user_choice = self.base_view.prompt_menu_command(self)
		self.clean_terminal()

		while True:
			if user_choice == '1':
				self.tournament_controller.create_tournament(self)
				self.start_menu()
			elif user_choice == '2':
				self.player_controller.add_height_players(self)
				self.start_menu()
			elif user_choice == '3':
				self.report_controller.start_report_menu(self)
				self.start_menu()
			elif user_choice == '4':
				print("Merci d'avoir utilisé ce programme. Au revoir")
				exit()
			else:
				print("Commande non valide. Veuillez réessayer.")
				self.start_menu()


	def register_result(self):
		# Sauvegarder le résultat d'un match
		pass

	def update_ranking(self):
		# Mettre à jour le classement 
		pass

	def finish_tournament(self):
		# Fin du tournois
		pass

	def run(self):
		self.start_menu()
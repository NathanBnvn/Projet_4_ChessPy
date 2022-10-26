from os import system, name
from .player_controller import PlayerController
from .tournament_controller import TournamentController
from .report_controller import ReportController
from model.tournament_model import Tournament
from model.player_model import Player
from view.base_view import View
from view.player_view import PlayerView
from view.report_view import ReportView
from view.tournament_view import TournamentView

class MainController:

	def __init__(self):
		# self.match = match
		# self.round = round
		self.player_controller = PlayerController(Player, PlayerView)
		self.tournament_controller = TournamentController(Tournament, TournamentView)
		self.report_controller = ReportController(ReportView)

		# Instancier la vue
		self.base_view = View

	# définir un fonction pour nettoyer le terminal
	def clean_terminal(self):
		    # pour windows
			if name == 'nt':
				_ = system('cls')
			# pour mac & linux
			else:
				_ = system('clear')


	def start_menu(self):
		#self.clean_terminal()
		self.base_view.show_menu_command(self)
		user_choice = self.base_view.prompt_menu_command(self)

		while True:
			if user_choice == 1:
				self.tournament_controller.start_tournament_menu()
				self.start_menu()
			elif user_choice == 2:
				self.player_controller.start_player_menu()
				self.start_menu()
			elif user_choice == 3:
				self.report_controller.start_report_menu()
				self.start_menu()
			elif user_choice == 4:
				print("Merci d'avoir utilisé ChessPy. À bientôt")
				exit()
			else:
				print("Commande non valide. Veuillez réessayer.")
				self.start_menu()


	def register_result(self):
		# Sauvegarder le résultat d'un match
		pass


	def run(self):
		self.start_menu()
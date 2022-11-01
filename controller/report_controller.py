from curses.ascii import isdigit
from model.player_model import Player
from model.tournament_model import Tournament
from view.base_view import View
from view.manager_view import ManagerView

class ReportController:

    def __init__(self, view):
        self.report_view = view
        self.base_view = View
        self.manager_view = ManagerView
        self.player_model = Player
        self.tournament_model = Tournament


    # MENU REPORT

    def start_report_menu(self):
        self.report_view.show_report_menu(self)
        menu_message = "Choisissez une option : "
        error_message = "Commande non valide. Veuillez réessayer."
        
        while True:
            user_choice = self.manager_view.prompt_command(self, menu_message)
            
            if user_choice == '1':
                self.all_player_alphabetical()
            elif user_choice == '2':
                self.all_player_by_ranks()
            elif user_choice == '3':
                print(user_choice)
            elif user_choice == '4':
                print(user_choice)
            elif user_choice == '5':
                print(user_choice)
            elif user_choice == '6':
                print(user_choice)
            elif user_choice == '7':
                print(user_choice)
            elif user_choice == '8':
                return
            else:
                self.manager_view.show_message(self, error_message)
            
            self.start_report_menu()
            return

    def all_player_alphabetical(self):
        # par ordre alphabétique ;
        players = self.player_model.get_all(self)        
        alphabetical_list = sorted(players, key=lambda x: x['last_name'], reverse=False)
        print(alphabetical_list)
        #self.manager_view.show_message(self, alphabetical_list)
    
    def all_player_by_ranks(self):
        # par ordre alphabétique ;
        players = self.player_model.get_ranked_player(self)        
        ranked_list = sorted(players, key=lambda x: x['ranking'], reverse=False)
        print(ranked_list)


    def generate_report(self):
        # Liste de tous les acteurs :
        
        
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
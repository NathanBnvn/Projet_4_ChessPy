from view.base_view import View
from view.manager_view import ManagerView

class ReportController:

    def __init__(self, view):
        self.report_view = view
        self.base_view = View
        self.manager_view = ManagerView

    def start_report_menu(self):
        self.report_view.show_report_menu(self)
        menu_message = "Choisissez une option : "
        error_message = "Commande non valide. Veuillez réessayer."
        
        while True:
            user_choice = self.manager_view.prompt_command(self, menu_message)
            
            if user_choice == '1':
                self.all_player_alphabetical(self)
            elif user_choice == '2':
                print(user_choice)
            elif user_choice == '3':
                print(user_choice)
            elif user_choice == '4':
                return
            else:
                self.manager_view.error_message(self, error_message)
            
            self.start_report_menu()
            return

    def all_player_alphabetical(self):
        # par ordre alphabétique ;
        alphabetical_list = sorted(self.players, key=lambda x: x.last_name, reverse=False)
        print(alphabetical_list)
        return


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
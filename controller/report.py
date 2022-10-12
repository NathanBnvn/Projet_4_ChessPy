from view.report import ReportView

class ReportController:

    def __init__(self):
        pass

    def start_report_menu(self):
        self.report_menu = ReportView
        self.report_menu.show_report_menu(self)
        user_choice = self.report_menu.prompt_report_menu_command(self)

        while True:
            if user_choice == '1':
                self.all_player_alphabetical(self)
            elif user_choice == '2':
                print('2')
            elif user_choice == '3':
                print('3')
            elif user_choice == '8':
                return
            else:
                print("Commande non valide. Veuillez réessayer.")

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
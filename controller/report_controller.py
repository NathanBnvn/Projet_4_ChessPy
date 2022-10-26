class ReportController:

    def __init__(self, view):
        self.report_view = view


    def start_report_menu(self):
        self.report_view.show_report_menu(self)
        
        while True:
            user_choice = self.report_view.prompt_menu_command(self)
            
            if user_choice == 1:
                self.all_player_alphabetical(self)
            elif user_choice == 2:
                print(user_choice)
            elif user_choice == 3:
                print(user_choice)
            elif user_choice == 4:
                return
            else:
                print("Commande non valide. Veuillez réessayer.")
                self.start_report_menu()
            
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
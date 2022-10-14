class ReportController:

    def __init__(self, view):
        self.report_view = view

    def prompt_menu_command(self):
        user_choice = str(input())
        return user_choice
    
    def start_report_menu(self):
        self.report_view.show_report_menu(self)
        user_choice = self.prompt_menu_command()

        while True:
            if user_choice == '1':
                self.all_player_alphabetical(self)
                self.start_report_menu()
            elif user_choice == '2':
                print('2')
                self.start_report_menu()
            elif user_choice == '3':
                print('3')
                self.start_report_menu()
            elif user_choice == '4':
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
from view.manager_view import ManagerView
from os import system, name
import datetime

class ManagerController:
    def __init__(self, view):
        self.manager_view = ManagerView

    def clean_terminal(self):
        if name == 'nt':
		# pour windows
            _ = system('cls')
        else:
        # pour mac & linux
            _ = system('clear')

    def check_user_input(self, input_category, message, choices):
        i = 0
        user_content = []
        wrong_date_format = "Veuillez entrer la date dans un format valide !"
        wrong_timeline = "Veuillez entrer une date de fin supérieur ou égale à celle du début !"
        invalid_action_message = "Commande non valide. Veuillez réessayer."
        wrong_type = "Veuillez entrer un nombre entier !"

        while i < len(input_category):
            input_data = input_category[i]
            if "sélectionnez" in input_data:
                user_choice = self.manager_view.select_command(self, message, choices)
                user_content.append(user_choice)
                i += 1
            else:
                content = self.manager_view.prompt_command(self, input_data)
                if content == 'quit':
                    # L'utilisateur doit pouvoir quitter le programme à tout moment
                    break
                elif content == '':
                    self.manager_view.error_message(self, invalid_action_message)
                elif "(jj/mm/aaaa)" in input_data:
                    try:
                        date = datetime.datetime.strptime(content, "%d/%m/%Y")
                        possible_date = user_content[i-1]
                        
                        if isinstance(possible_date, datetime.date):
                            if date >= possible_date:
                                user_content.append(date)
                                i += 1
                            else:
                                self.manager_view.error_message(self, wrong_timeline)
                        else:
                            user_content.append(date)
                            i += 1
                    except ValueError:
                        self.manager_view.error_message(self, wrong_date_format)
                elif "nombre" in input_data or "classement" in input_data:
                    if content.isdigit():
                        user_content.append(content)
                        i += 1
                    else :
                        self.manager_view.error_message(self, wrong_type)
                else:
                    user_content.append(content)
                    i += 1
                
        return user_content
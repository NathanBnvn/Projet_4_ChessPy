#!/usr/bin/env python
# coding: utf-8

from view.manager_view import ManagerView
from rich.table import Table
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
        wrong_type = "Veuillez entrer un nombre entier !"
        negative_number = "Veuillez entrer un nombre positif !"
        invalid_action_message = "Commande non valide. Veuillez réessayer."
        quit_message = "Vous venez d'interrompre votre action"

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
                    self.manager_view.show_message(self, quit_message)                    
                    break
                elif content == '':
                    self.manager_view.show_message(self, invalid_action_message)
                
                elif "(jj/mm/aaaa)" in input_data:
                    try:
                        date = datetime.datetime.strptime(content, "%d/%m/%Y")
                        possible_date = user_content[i-1]
                        if isinstance(possible_date, datetime.date):
                            if date >= possible_date:
                                user_content.append(date.strftime('%d/%m/%Y'))
                                i += 1
                            else:
                                self.manager_view.show_message(self, wrong_timeline)
                        else:
                            user_content.append(date.strftime('%d/%m/%Y'))
                            i += 1
                    except ValueError:
                        self.manager_view.show_message(self, wrong_date_format)
                
                elif "nombre" in input_data or "classement" in input_data:
                    if content.isdigit():
                        if int(content) > 0:
                            user_content.append(int(content))
                            i += 1
                        else:
                            self.manager_view.show_message(self, negative_number)
                    else :
                        self.manager_view.show_message(self, wrong_type)
                else:
                    user_content.append(content)
                    i += 1
                
        return user_content


    def update_process(self, data_model):
        success_message = "La donnée a bien été mis à jour"
        select_category = "Quelle propriété souhaitez vous éditer ?"
        value_message = "Veuillez entrer la nouvelle valeur : "
        cannot_save_message = "Les données n'ont pas pu être enregistrées"
        no_data_message = "Aucune donnée existante"
        quit_message = "Vous venez d'interrompre votre mise à jour"
        categories = []

        elements = data_model.get_all(self)
        if len(elements) > 0:
            # @TODO implement view function
            # self.manager_controller.set_table_format(self)
            print(elements)

            element_id = self.manager_controller.check_id_input(self, len(elements))
            if element_id:
                element = data_model.get(self, element_id)
                # @TODO implement view function
                # self.manager_controller.set_table_format(self)
                print(element)
                
                for key in element:
                    categories.append(key)
                category = self.manager_view.select_command(self, select_category, categories)
                new_value = self.manager_view.prompt_command(self, value_message)
                if new_value == "quit":
                    self.manager_view.show_message(self, quit_message)
                    return
                else:
                    update_element = data_model.update(self, category, new_value, element_id)
                    if element_id in update_element:
                        self.manager_view.show_message(self, success_message)
                    else:
                        self.manager_view.show_message(self, cannot_save_message)
            else:
                self.manager_view.show_message(self, quit_message)
        else:
            self.manager_view.show_message(self, no_data_message)


    def check_id_input(self, instances_count):
        select_id = "Veuillez sélectionner l'ID de l'instance que vous souhaitez mettre à jour : "
        id_not_found = "L'ID entré ne correspond à rien. Veuillez réessayer."

        while True:
            selected_id = self.manager_view.prompt_command(self, select_id)
            if selected_id == "quit":
                return
            elif selected_id.isdigit():
                element_id = int(selected_id)
                if element_id <= instances_count:
                    return element_id
                else:
                    self.manager_view.show_message(self, id_not_found)    
            else:
                self.manager_view.show_message(self, self.error_message)


    def set_table_format(self):
        t = ("Test", "Casual", "Novel")
        n = ("Personne", "Paul", "10/09/1990")
        table = Table(*t)
        # for value in datas.values():
		# table.add_column(value)
        table.add_row(*n)
        #table.add_row("Morty", "Plumbus")
        self.manager_view.show_table(self, table)

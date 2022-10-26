#!/usr/bin/env python
# coding: utf-8

import inquirer

class PlayerView:

    def show_player_menu(self):
        print(
            """
            MENU DES JOUEURS

            '1' pour créer un joueur
            '2' pour mettre à jour un joueur
            '4' pour retourner au menu principal
            """
            )

    def prompt_menu_command(self):
        user_choice = int(input("Choisissez une option : "))
        return user_choice

    def prompt_player(self):
        last_name = str(input("le nom du joueur/joueuse : "))
        first_name = str(input("le prénom du joueur/joueuse : "))
        birth_date = str(input("la date de naissance du joueur/joueuse : "))
        gender_list = [
            inquirer.List(
                "gender", 
                message="sélectionnez le sexe du joueur/joueuse", 
                choices=["masculin", "féminin"], 
            ),
        ]
        answers = inquirer.prompt(gender_list)
        gender = answers["gender"]
        ranking = int(input("la place du joueur/joueuse dans le classement : "))
        player = [last_name, first_name, birth_date, gender, ranking]
        return player
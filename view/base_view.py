#!/usr/bin/env python
# coding: utf-8


class View:

    def show_menu_command(self):
        print(
            """
            MENU

            '1' pour gérer un tournois
            '2' pour gérer les joueurs et leurs classement
            '3' pour créer un rapport
            '4' pour quitter le programme
            """
            )

    def prompt_menu_command(self):
        user_choice = int(input("Choisissez un menu : "))
        return user_choice

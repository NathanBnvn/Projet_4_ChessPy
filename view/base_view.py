#!/usr/bin/env python
# coding: utf-8

class View:

    def show_menu_command(self):
        print(
            """
            MENU

            '1' pour gérer un tournois
            '2' pour gérer les joueurs
            '3' pour créer un rapport
            '4' pour quitter le programme
            """
            )
    
    def quit_program_message(self):
        print("\n Merci d'avoir utilisé ChessPy. À bientôt 👋\n")

#!/usr/bin/env python
# coding: utf-8


class Views:

    # add main menu function
    def show_menu_command(self):
        print(
            """
            '1' pour créer un tournois
            '2' pour ajouter 8 joueurs
            '3' pour créer un rapport
            '4' pour quitter le programme
            """
            )
    
    def prompt_menu_command(self):
        user_choice = str(input())
        return user_choice

#!/usr/bin/env python
# coding: utf-8


class Views:

    # add main menu function
    def show_menu_command(self):
        print(
            """
            tapez 't' pour créer un tournois
            tapez 'j' pour ajouter 8 joueurs

            CREER UN RAPPORT
            tapez 'ra' pour lister les joueurs par ordre alphabétique
            tapez 'rc' pour lister les joueurs par classement
            tapez 'jta' pour lister tous les joueurs d'un tournoi par ordre alphabetique
            tapez 'jtc' pour lister tous les joueurs d'un tournoi par classement
            tapez 'lt' pour lister de tous les tournois.
            tapez 'tt' pour lister de tous les tours d'un tournoi.
            tapez 'm' pour lister de tous les matchs d'un tournoi
            
            tapez 'q' pour quitter le programme
            """
            )
    
    def prompt_menu_command(self):
        user_choice = str(input())
        return user_choice

    def __init__(self):
        self.views = views

#!/usr/bin/env python
# coding: utf-8

import inquirer

class TournamentView:
    
    def show_tournament_menu(self):
        print(
            """
            MENU DES TOURNOIS

            '1' pour créer un tournois
            '2' pour mettre à jour un tournois
            '4' pour retourner au menu principal
            """
        )

    def prompt_menu_command(self):
        user_choice = int(input("Choisissez une option : "))
        return user_choice
    
    def prompt_tournament(self):
        name = str(input("le nom du tournois : "))
        place = str(input("le lieu du tournois : "))
        start_date = input("la date de début du tournois (jj/mm/aaaa) : ")
        end_date = input("la date de fin du tournois (jj/mm/aaaa) : ")
        round_count = int(input("entrez le nombre de round : "))
        round_list = "instance de tours"
        players = "instance de player"
        control_list = [
            inquirer.List("control", 
                message="sélectionnez le type de temps",
                choices=["bullet", "blitz", "coup rapide"],
            ),
        ]
        answers = inquirer.prompt(control_list)
        time_check = answers["control"]
        description = str(input("remarques générales : "))
        tournament = [name, place, start_date, end_date, round_count, time_check, description]
        return tournament
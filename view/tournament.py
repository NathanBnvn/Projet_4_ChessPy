#!/usr/bin/env python
# coding: utf-8

import inquirer

class TournamentView:

    def prompt_tournament(self):
        name = str(input("tapez le nom du tournois : "))
        place = str(input("tapez le lieu du tournois : "))
        start_date = str(input("tapez la date de début du tournois : "))
        end_date = str(input("tapez la date de fin du tournois : "))
        round_number = 4
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
        tournament = [name, place, start_date, end_date, round_number, round_list, players, time_check, description]
        #return tournament
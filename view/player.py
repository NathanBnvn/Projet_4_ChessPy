#!/usr/bin/env python
# coding: utf-8

import inquirer


class PlayerView:

    def prompt_player(self):
        last_name = str(input("tapez le nom du joueur/joueuse : "))
        first_name = str(input("tapez le prénom du joueur/joueuse : "))
        birth_date = str(input("tapez la date de naissance du joueur/joueuse : "))
        gender_list = [
            inquirer.List(
                "gender", 
                message="sélectionnez le sexe du joueur/joueuse", 
                choices=["masculin", "féminin"], 
            ),
        ]
        answers = inquirer.prompt(gender_list)
        gender = answers["gender"]
        ranking = int(input("tapez la place du joueur/joueuse dans le classement : "))
        player = [last_name, first_name, birth_date, gender, ranking]
        return player
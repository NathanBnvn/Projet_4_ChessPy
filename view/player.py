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
            '' pour retourner au menu principal
            """
            )

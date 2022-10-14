#!/usr/bin/env python
# coding: utf-8

class ReportView:
    
    def show_report_menu(self):
        print(
            """
            MENU DES RAPPORTS

            - Pour lister :
                '1' les joueurs par ordre alphabétique.
                '2' les joueurs par classement.
                '3' tous les joueurs d'un tournoi par ordre alphabetique.
                '4' tous les joueurs d'un tournoi par classement.
                '5' tous les tournois.
                '6' tous les tours d'un tournoi.
                '7' tous les matchs d'un tournoi.

            '8' retourner au menu précédent.
            """
        )
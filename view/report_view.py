#!/usr/bin/env python
# coding: utf-8

class ReportView:
    
    def show_report_menu(self):
        print(
            """
            MENU DES RAPPORTS

            • Pour lister tous les joueurs :
                '1' par ordre alphabétique.
                '2' par classement.

            • Pour lister tous les joueurs d'un tournoi :
                '3' par ordre alphabetique.
                '4' par classement.
            
            • Pour lister afficher tous :
                '5' les tournois.
                '6' les tours d'un tournoi.
                '7' les matchs d'un tournoi.

            '8' retourner au menu précédent.
            """
        )

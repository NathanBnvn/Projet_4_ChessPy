#! /usr/bin/env python3
# coding: utf-8

from view.player_view import PlayerView
from view.tournament_view import TournamentView

from controller.main_controller import MainController 

def main():
	chess_game = MainController()
	chess_game.run()

if __name__ == "__main__":
	main()
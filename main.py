#! /usr/bin/env python3
# coding: utf-8

from view.player import PlayerView
from view.tournament import TournamentView

from controller.main import MainController 

def main():
	chess_game = MainController()
	chess_game.run()

if __name__ == "__main__":
	main()
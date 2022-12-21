#! /usr/bin/env python3
# coding: utf-8

from controller.main_controller import MainController


def main():
    chess_game = MainController()
    chess_game.run()


if __name__ == "__main__":
    main()

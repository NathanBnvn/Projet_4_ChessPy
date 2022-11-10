#!/usr/bin/env python
# coding: utf-8

import inquirer
from rich import print_json

class ManagerView:
    def prompt_command(self, input_name):
        user_choice = input(input_name)
        return user_choice


    def select_command(self, message, choices):
        selection_list = [
            inquirer.List(
                "selection", 
                message=message,
                choices=choices,
            ),
        ]
        answers = inquirer.prompt(selection_list)
        user_selection = answers["selection"]
        return user_selection


    def show_message(self, message):
        print("\n" + message + "\n")


    def show_json(self, data):
        print_json(data=data)

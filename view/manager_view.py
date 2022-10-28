import inquirer

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
    
    def error_message(self, message):
        print("\n" + message + "\n")
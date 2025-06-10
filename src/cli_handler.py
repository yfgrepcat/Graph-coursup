from inquirerpy import inquirer

class CLIHandler:
    def __init__(self):
        """
        Initialize the CLIHandler for managing user interactions.
        """
        pass

    def prompt_user(self, message : str, choices : list) -> str:
        """
        Prompt the user with a message and a list of choices.
        :param message: The message to display to the user.
        :param choices: A list of choices for the user to select from.
        :return: The user's selected choice.
        """
        answer = inquirer.select(
            message=message,
            choices=choices
        ).execute()
        return answer
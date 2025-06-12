from InquirerPy import inquirer

class CLIHandler:

    @staticmethod
    def prompt_user(message : str, choices : list) -> str:
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
"""
The main class for our Graph-coursup project.
"""
import json
from .algorithms import StableMarriage
from .cli_handler import prompt_user
from .data_loader import Schools, Students


class Schools:
    def __init__(self):
        """
        Initialize the schools based on the json file provided.
        """
        self.schoolsDict = {}
        self.load_schools("schools.json")

    def load_schools(self, file_path):
        """
        Load schools from a JSON file.
        :param file_path: Path to the JSON file containing school data.
        """
        try:
            with open(file_path, 'r') as file:
                self.schoolsDict = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {file_path} is not a valid JSON file.")

class Students:
    def __init__(self):
        """
        Initialize the students based on the json file provided.
        """
        self.studentsDict = {}
        self.load_students("students.json")
    
    def load_students(self, file_path):
        """
        Load students from a JSON file.
        :param file_path: Path to the JSON file containing student data.
        """
        try:
            with open(file_path, 'r') as file:
                self.studentsDict = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {file_path} is not a valid JSON file.")


def main():
    """
    Main function to run the Graph-coursup project.
    """
    schools = Schools()
    students = Students()
    stableMarriage = StableMarriage(schools, students)
    biddingPrompt: int = prompt_user("Choose who's the one serenading:\n1. Schools\n2. Students", [1, 2])
    stableMarriage.biddingChoice(biddingPrompt)
    pass


if __name__ == "__main__":
    """
    Main function to run the Graph-coursup project.
    """
    main()

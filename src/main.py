"""
The main class for our Graph-coursup project.
"""
import json
from collections import deque
from .algorithms import StableMarriage
from .cli_handler import CLIHandler

class Schools:
    def __init__(self):
        """
        Initialize the schools based on the json file provided.
        """
        self.schoolsDict = {}
        self.load_schools("data/example4/schools.json")

    def load_schools(self, file_path):
        """
        Load schools from a JSON file.
        :param file_path: Path to the JSON file containing school data.
        """
        try:
            with open(file_path, 'r') as file:
                schools_data = json.load(file)["schools"]
                self.schoolsDict = {
                    school["id"]: {
                        "capacity": school["capacity"],
                        "preferences": deque(school["students_preferences"]),
                        "assigned_elements": [],
                        "assigned": False
                    }
                    for school in schools_data
                }

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
        self.load_students("data/example4/students.json")
    
    def load_students(self, file_path):
        """
        Load students from a JSON file.
        :param file_path: Path to the JSON file containing student data.
        """
        try:
            with open(file_path, 'r') as file:
                students_data = json.load(file)["students"]
            self.studentsDict = {
                student["id"]: {
                    "capacity": 1,
                    "preferences": deque(student["school_preferences"]),
                    "assigned_elements": [],
                    "assigned": False
                }
                for student in students_data
            }

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
    biddingPrompt: int = CLIHandler.prompt_user("Choose who's the one serenading:\n1. Schools\n2. Students", [1, 2])
    stableMarriage = StableMarriage(schools=schools, students=students)
    stableMarriage.biddingChoice(biddingPrompt)
    print(students.studentsDict)
    print(schools.schoolsDict)
    stableMarriage.serenadingWave(students=students.studentsDict, schools=schools.schoolsDict)


if __name__ == "__main__":
    """
    Main function to run the Graph-coursup project.
    """
    main()

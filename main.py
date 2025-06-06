"""
The main class for our Graph-coursup project.
"""
import json

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

class StableMarriage:
    def __init__(self, schools, students):
        """
        Initialize the Stable Marriage algorithm with schools and students.
        :param schools: An instance of the Schools class.
        :param students: An instance of the Students class.
        """
        self.schools = schools.schoolsDict
        self.students = students.studentsDict

    def find_stable_marriage(self):
        """
        Implements the stable marriage algorithm to match students with schools.
        """
        # Placeholder for the stable marriage algorithm implementation
        pass

    def biddingChoice(self):
        pass



def main():
    """
    Main function to run the Graph-coursup project.
    """
    schools = Schools()
    students = Students()
    stable_marriage = StableMarriage(schools, students)

    # Call the method to find stable marriage
    stable_marriage.find_stable_marriage()


if __name__ == "__main__":
    """
    Main function to run the Graph-coursup project.
    """
    main()

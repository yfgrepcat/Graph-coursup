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
        load_schools("schools.json")

    def load_schools(self, file_path):
        """
        Load schools from a JSON file.
        :param file_path: Path to the JSON file containing school data.
        """
        
class Students:
    """
    Initialize the students based on the json file provided.
    """
    self.studentsDict = {}
    pass



if __name__ == "__main__":
    """
    Main function to run the Graph-coursup project.
    """
    schools = Schools()
    students = Students()

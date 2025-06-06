import json
from typing import Dict
from .models import School, Student

class DataLoader:
    def __init__(self, schools_file_path: str, students_file_path: str):
        self.schools_file_path = schools_file_path
        self.students_file_path = students_file_path

    def load_schools(self) -> Dict:
        schools_data = {}
        try:
            with open(self.schools_file_path, 'r') as file:
                data = json.load(file)
                #TODO: load data into School objects
        except FileNotFoundError:
            print(f"Error: The file {self.schools_file_path} was not found.")
            # Handle error appropriately, maybe raise an exception
        except json.JSONDecodeError:
            print(f"Error: The file {self.schools_file_path} is not a valid JSON file.")
        return schools_data

    def load_students(self) -> Dict:
        students_data = {}
        try:
            with open(self.students_file_path, 'r') as file:
                data = json.load(file)
                #TODO: load data into Student objects
        except FileNotFoundError:
            print(f"Error: The file {self.students_file_path} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {self.students_file_path} is not a valid JSON file.")
        return students_data
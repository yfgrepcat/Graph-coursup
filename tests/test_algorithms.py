import unittest
from collections import deque
from src.algorithms import StableMarriage

class TestStableMarriage(unittest.TestCase):
    def setUp(self):
        # Example schools and students data
        self.schools = {
            "School A": {
                "capacity": 2,
                "preferences": deque(["Student 1", "Student 2", "Student 3"]),
                "assigned_elements": []
            },
            "School B": {
                "capacity": 2,
                "preferences": deque(["Student 3", "Student 1", "Student 2"]),
                "assigned_elements": []
            }
        }

        self.students = {
            "Student 1": {
                "capacity": 1,
                "preferences": deque(["School A", "School B"]),
                "assigned_elements": []
            },
            "Student 2": {
                "capacity": 1,
                "preferences": deque(["School B", "School A"]),
                "assigned_elements": []
            },
            "Student 3": {
                "capacity": 1,
                "preferences": deque(["School A", "School B"]),
                "assigned_elements": []
            }
        }

    def test_stable_matching(self):
        """
        Test a basic stable matching scenario.
        """
        algorithm = StableMarriage(self.schools, self.students)
        algorithm.serenadingWave(self.students, self.schools)

        # Check that all students are assigned
        for student_id, student in self.students.items():
            self.assertTrue(student["assigned_elements"], f"{student_id} is not assigned.")

        # Check that all schools respect their capacity
        for school_id, school in self.schools.items():
            self.assertLessEqual(len(school["assigned_elements"]), school["capacity"], f"{school_id} exceeds capacity.")

    def test_unbalanced_capacity(self):
        """
        Test a scenario where schools have more capacity than students.
        """
        self.schools["School A"]["capacity"] = 3
        self.schools["School B"]["capacity"] = 3

        algorithm = StableMarriage(self.schools, self.students)
        algorithm.serenadingWave(self.students, self.schools)

        # Check that no school exceeds its capacity
        for school_id, school in self.schools.items():
            self.assertLessEqual(len(school["assigned_elements"]), school["capacity"], f"{school_id} exceeds capacity.")


if __name__ == '__main__':
    unittest.main()
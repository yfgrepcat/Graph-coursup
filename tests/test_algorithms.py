import unittest
from src.algorithms import StableMarriage
from src.models import School, Student

class TestStableMarriage(unittest.TestCase):
    def setUp(self):
        self.schools = [
            School(name="School A", capacity=2),
            School(name="School B", capacity=2)
        ]
        pass
    # Work in progress


if __name__ == '__main__':
    unittest.main()
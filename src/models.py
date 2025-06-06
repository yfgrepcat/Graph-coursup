class School:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def __repr__(self):
        return f"School(name={self.name}, capacity={self.capacity}, students={self.students})"


class Student:
    def __init__(self, id, name, preferences):
        self.id = id
        self.name = name
        self.preferences = preferences
        self.assigned_school = None

    def assign_school(self, school):
        self.assigned_school = school

    def __repr__(self):
        return f"id={self.id}, studentName={self.name}, preferences={self.preferences}, assignedSchool={self.assigned_school})"
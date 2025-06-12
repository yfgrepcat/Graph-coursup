class StableMarriage:
    def __init__(self, schools, students):
        self.schools = schools
        self.students = students
        self.serenading = True  # Flag set to True if schools are serenading students
        self.waveNber = 0  # Number of waves that were needed to converge

    def serenadingWave(self, students, schools):
        """
        Implement the Gale-Shapley algorithm for stable marriage.
        This method handles the logic of matching students to schools.
        """
        # Swap roles if students are serenading schools
        if not self.serenading:
            students, schools = schools, students

        # Initialize all schools and students as unassigned
        for school in schools.values():
            school["assigned_elements"] = []
            school["assigned"] = False

        for student in students.values():
            student["assigned"] = False

        # Perform the Gale-Shapley algorithm
        while any(
            not student["assigned"] and student["preferences"]
            for student in students.values()
        ):
            for student_id, student_info in students.items():
                if not student_info["assigned"] and student_info["preferences"]:
                    # Student proposes to the next school in their preference list
                    school_id = student_info["preferences"].popleft()
                    school = schools[school_id]
                    assigned = school["assigned_elements"]

                    if len(assigned) < school["capacity"]:
                        # School has capacity, accept the student
                        assigned.append(student_id)
                        student_info["assigned"] = True
                    else:
                        # School is full, check if the new student is preferred
                        for current_student in assigned:
                            if self.is_better_choice(school_id, student_id, current_student, schools):
                                # Replace the less preferred student
                                assigned.remove(current_student)
                                students[current_student]["assigned"] = False
                                assigned.append(student_id)
                                student_info["assigned"] = True
                                break

        # Display the final assignment
        print("\nFinal assignment:")
        for school_id, school in schools.items():
            print(f"{school_id} -> {school['assigned_elements']}")

    def is_better_choice(self, school_id, new_student_id, current_student_id, schools):
        """
        Check if the new student is preferred over the current student.
        :param school_id: ID of the school.
        :param new_student_id: ID of the new student.
        :param current_student_id: ID of the current student.
        :param schools: Dictionary of schools.
        :return: True if the new student is preferred, False otherwise.
        """
        preferences = schools[school_id]["preferences"]
        for student_id in preferences:
            if student_id == new_student_id:
                return True
            if student_id == current_student_id:
                return False
        return False

    def biddingChoice(self, choice: int):
        """
        Handle the bidding choice for the stable marriage algorithm.
        :param choice: The choice made by the user.
        """
        if choice == 1:
            self.serenading = True
        elif choice == 2:
            self.serenading = False
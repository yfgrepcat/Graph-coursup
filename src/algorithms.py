class StableMarriage:
    def __init__(self, schools, students):
        self.schools = schools
        self.students = students
        self.serenading = True # Flag set to True if schools are serenading students
        self.waveNber = 0 # Number of waves that were needed to converge

    def serenadingWave(self, students, schools):
        """
        Implement the serenading wave algorithm for stable marriage.
        This method will handle the logic of matching students to schools.
        """
        # Placeholder for the serenading wave algorithm implementation

        # ALGORITHM: 
        # List of schools (id, capacity, preferences)
        # List of students (id, preferences)
        # ----- IF SCHOOLS CHOOSE -----

        # An Array for each school (filled by students chosen)
        # A FIFO stack for each student preferences

        # LOOP until (?? 2 iterations are same ??)
            # For each student in the list:
                # If student isn't already chosen in a school and haven't been rejected already by all schools (FIFO preferences not empty)
                    # Pop the school from the student FIFO of preferences
                    # If school has capacity to welcome the student and don't have a better student option
                        # Add student to the school array

        if self.serenading:
            temp = students
            students = schools
            schools = temp

        while any(
        not info["assigned"] and info["preferences"]
        for info in students.values()
        ):

            for student_id, student_info in students.items():
                if not student_info["assigned"] and student_info["preferences"]:
                    school_id = student_info["preferences"].popleft()
                    school = schools[school_id]
                    assigned = school["assigned_elements"]

                    if len(assigned) < school["capacity"]:
                        assigned.append(student_id)
                        student_info["assigned"] = True
                    else:
                        for current_student in assigned:
                            if self.is_better_choice(school_id, student_id, assigned, schools):
                                assigned.remove(current_student)
                                students[current_student]["assigned"] = False
                                assigned.append(student_id)
                                student_info["assigned"] = True
                                break

        # Affichage des résultats
        print("\nFinal assignment:")
        for school_id, school in schools.items():
            print(f"{school_id} -> {school['assigned_elements']}")

    
    def is_better_choice(self, school_id, new_student_id, current_students, schools):
        prefs = schools[school_id]["preferences"]
        for student_id in prefs:
            if student_id == new_student_id:
                return True
            if student_id in current_students:
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

def stable_marriage_algorithm(schools, students):
    # Logic to execute the stable marriage algorithm
    serenadingProcess = StableMarriage(schools, students)
    # Pyinquirer prompt user
    
    choice : int = 1 
    serenadingProcess.biddingChoice(choice)
    serenadingProcess.serenadingWave()

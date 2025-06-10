class StableMarriage:
    def __init__(self, schools, students):
        self.schools = schools
        self.students = students
        self.serenading = True # Flag set to True if schools are serenading students
        self.waveNber = 0 # Number of waves that were needed to converge

    def serenadingWave(self):
        """
        Implement the serenading wave algorithm for stable marriage.
        This method will handle the logic of matching students to schools.
        """
        # Placeholder for the serenading wave algorithm implementation
        pass

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

from collections import deque

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

        proposers = The ones who serenade
        receivers = The ones who are serenaded

        :param students: Dictionary of students with their preferences.
        :param schools: Dictionary of schools with their preferences.
        """

        # Swap roles if students are serenading schools
        if self.serenading:
            proposers = schools
            receivers = students
        else:
            proposers = students
            receivers = schools

        # Initialize all schools and students as unassigned
        for entity in list(proposers.values()) + list(receivers.values()):
            entity["assigned_elements"] = []

        # Deque -> a queue that allows fast appends and pops from both ends
        # Appropriate since everything is sequential
        # And rejection handled efficiently via re-queuing
        free_proposers = deque(proposers.keys())

        # Precompute preferences for 
        receiver_ranks = {}

        # Critical optimization of the script :
        # Precompute the ranks of each proposer in each receiver's preference list
        # We went from O(n³) to O(n²) complexity
        # -> for loop is no longer required to check preferences every time
        for receiver_id, receiver_info in receivers.items():
            rank_map = {} # Temporary map to store ranks of proposers
            for rank_idx, proposer_id in enumerate(receiver_info["preferences"]):
                rank_map[proposer_id] = rank_idx
            receiver_ranks[receiver_id] = rank_map
        
        self.waveNber = 0  # Reset wave counter

        # Perform the stable marriage algorithm
        # Added while loop to track the number of rounds
        while free_proposers:
            self.waveNber += 1  # Increment wave counter at the start of each round
            next_round_proposers = deque()  # Track proposers for the next round
            while free_proposers:
                proposer_id = free_proposers.popleft()
                proposer = proposers[proposer_id]
                
                # Skip if no preferences left
                if not proposer["preferences"]:
                    continue
                    
                # Get next preference
                receiver_id = proposer["preferences"].popleft()
                receiver = receivers[receiver_id]
                
                # Case 1: Receiver has capacity
                if len(receiver["assigned_elements"]) < receiver["capacity"]:
                    receiver["assigned_elements"].append(proposer_id)
                    # Track assignment both ways
                    proposer["assigned_elements"].append(receiver_id)
                    
                    # If proposer still has capacity, re-enqueue them
                    if len(proposer["assigned_elements"]) < proposer["capacity"]:
                        free_proposers.append(proposer_id)
                
                # Case 2: Receiver is full
                else:
                    # Find worst current match
                    # Initialize worst rank to ~-infinity
                    worst_rank = float('-inf')
                    worst_proposer = None
                    rank_map = receiver_ranks[receiver_id]
                    
                    for curr_id in receiver["assigned_elements"]:
                        curr_rank = rank_map.get(curr_id, float('inf'))
                        if curr_rank > worst_rank:
                            worst_rank = curr_rank
                            worst_proposer = curr_id
                    
                    # Compare new proposer
                    new_rank = rank_map.get(proposer_id, float('inf'))
                    if new_rank < worst_rank:
                        # Replace worst match
                        receiver["assigned_elements"].remove(worst_proposer)
                        # Remove bidirectional link
                        worst_proposer_data = proposers[worst_proposer]
                        worst_proposer_data["assigned_elements"].remove(receiver_id)
                        
                        # Add new match
                        receiver["assigned_elements"].append(proposer_id)
                        proposer["assigned_elements"].append(receiver_id)
                        
                        # Re-enqueue rejected proposer
                        free_proposers.append(worst_proposer)
                        # Re-enqueue new proposer if they still have capacity
                        if len(proposer["assigned_elements"]) < proposer["capacity"]:
                            free_proposers.append(proposer_id)
                    else:
                        # Proposer is rejected
                        # Re-enqueue proposer to try next preference
                        free_proposers.append(proposer_id)
            # Update free proposers for the next wave
            free_proposers = next_round_proposers

        print("\nFinal assignment:")
        if self.serenading:
            # Schools serenaded: show school assignments
            for school_id, school in schools.items():
                print(f"{school_id} -> {school['assigned_elements']}")
        else:
            # Students serenaded: show student assignments
            for student_id, student in students.items():
                print(f"{student_id} -> {student['assigned_elements']}")
        
        print(f"\nNumber of waves required to converge: {self.waveNber}")

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
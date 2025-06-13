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

        # OLD ALGORITHM (NOT INVERTED AND NOT OPTIMIZED): 
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

        # if self.serenading:
        #     temp = students
        #     students = schools
        #     schools = temp

        # while any(
        # not info["assigned"] and info["preferences"]
        # for info in students.values()
        # ):

        #     for student_id, student_info in students.items():
        #         if not student_info["assigned"] and student_info["preferences"]:
        #             school_id = student_info["preferences"].popleft()
        #             school = schools[school_id]
        #             assigned = school["assigned_elements"]

        #             if len(assigned) < school["capacity"]:
        #                 if student_info["capacity"] > 0:
        #                     assigned.append(student_id)
        #                     print(student_id)
        #                     print(student_info["capacity"])
        #                     student_info["capacity"] -= 1
        #                     if student_info["capacity"] <= 0:
        #                         student_info["assigned"] = True
        #             else:
        #                 for current_student in assigned:
        #                     if self.is_better_choice(school_id, student_id, assigned, schools):
        #                         assigned.remove(current_student)
        #                         students[current_student]["assigned"] = False
        #                         assigned.append(student_id)
        #                         student_info["assigned"] = True
        #                         break

        # # Affichage des résultats
        # print("\nFinal assignment:")
        # for school_id, school in schools.items():
        #     print(f"{school_id} -> {school['assigned_elements']}")

        # def is_better_choice(self, school_id, new_student_id, current_students, schools):
        # prefs = schools[school_id]["preferences"]
        # for student_id in prefs:
        #     if student_id == new_student_id:
        #         return True
        #     if student_id in current_students:
        #         return False
        # return False

        # ERROR 1:  Line 60: Assigned and never challenged then
        # ERROR 2:  Line 67: Never check capacity
        # ERROR 3:  Line 75: old is_better_choice function chosed the first in the list that is not sorted. Not compared to the actual worst choice
        # ERROR 4:  Line 42: While can result in an infinite loop because it continue if there is a student that is not assigned









        
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

        self.waveNber = 0
        # Perform the stable marriage algorithm
        while free_proposers:
            # Check if at least one proposer has preferences left
            if not any(proposers[pid]["preferences"] for pid in free_proposers):
                break  # No proposals possible anymore

            self.waveNber += 1
            next_round = deque()

            print(f"\n*** Wave {self.waveNber} attempts ***")

            proposals_made = 0  # Track if at least one proposal is made in this wave

            # Make sure that one round each free proposer gets to serenade
            for _ in range(len(free_proposers)):
                proposer_id = free_proposers.popleft()
                proposer = proposers[proposer_id]

                # Skip if no preferences left
                if not proposer["preferences"]:
                    print(f"Proposer {proposer_id} has no preferences left, skipping.")
                    continue

                # Pop the preference for proposal
                receiver_id = proposer["preferences"].popleft()
                print(f"Proposer {proposer_id} attempts to propose to Receiver {receiver_id}")
                receiver = receivers[receiver_id]
                proposals_made += 1

                # Case 1: Receiver has capacity
                if len(receiver["assigned_elements"]) < receiver["capacity"]:
                    receiver["assigned_elements"].append(proposer_id)
                    proposer["assigned_elements"].append(receiver_id)

                    # if proposer has still room/capacity for another one he is still free for the next round
                    if len(proposer["assigned_elements"]) < proposer["capacity"]:
                        next_round.append(proposer_id)

                else:
                    # Find worst current match based on precomputed ranks
                    worst_rank = float('-inf')
                    worst_proposer = None
                    rank_map = receiver_ranks[receiver_id]

                    # Check current assigned elements to find the worst match
                    for curr_id in receiver["assigned_elements"]:
                        curr_rank = rank_map.get(curr_id, float('inf'))
                        if curr_rank > worst_rank:
                            worst_rank = curr_rank
                            worst_proposer = curr_id

                    new_rank = rank_map.get(proposer_id, float('inf'))

                    # Case 2: Receiver is full, but proposer is better than worst match
                    if new_rank < worst_rank:
                        # Replace worst match
                        receiver["assigned_elements"].remove(worst_proposer)
                        worst_proposer_data = proposers[worst_proposer]
                        worst_proposer_data["assigned_elements"].remove(receiver_id)

                        receiver["assigned_elements"].append(proposer_id)
                        proposer["assigned_elements"].append(receiver_id)

                        # Re-enqueue rejected proposer and new proposer if capacity left
                        next_round.append(worst_proposer)
                        if len(proposer["assigned_elements"]) < proposer["capacity"]:
                            next_round.append(proposer_id)
                    else:
                        # Proposal rejected; re-enqueue proposer
                        next_round.append(proposer_id)

            # If no proposer made a proposal this wave, don't count this wave
            if proposals_made == 0:
                self.waveNber -= 1

            free_proposers = next_round

            # Print status at end of wave
            print(f"\n--- End of Wave {self.waveNber} ---")
            print("Proposers' assignments:")
            for pid, pdata in proposers.items():
                print(f"  {pid}: assigned -> {pdata['assigned_elements']}")
            print("Receivers' assignments:")
            for rid, rdata in receivers.items():
                print(f"  {rid}: assigned -> {rdata['assigned_elements']}")
            print("----------------------------")

        # Final summary
        print("\nFinal assignment:")
        if self.serenading:
            for school_id, school in schools.items():
                print(f"{school_id} -> {school['assigned_elements']}")
        else:
            for student_id, student in students.items():
                print(f"{student_id} -> {student['assigned_elements']}")

    def biddingChoice(self, choice: int):
        """
        Handle the bidding choice for the stable marriage algorithm.
        :param choice: The choice made by the user.
        """
        if choice == 1:
            self.serenading = True
        elif choice == 2:
            self.serenading = False
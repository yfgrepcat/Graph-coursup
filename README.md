# Graph-coursup
A Python-powered simulation of a Parcoursup-like admission system, implementing the stable marriage algorithm to efficiently match students with their preferred universities based on mutual preferences.

## Features
- **Stable Marriage Algorithm**: Implements the Gale-Shapley algorithm to ensure stable matches between students and universities.
- **JSON Data Handling**: Loads student and school data from JSON files for easy configuration and updates.
- **Preference Management**: Allows students to rank their preferred schools and schools to rank their preferred students.
- **Dynamic Bidding**: Allows the user to chose if schools or students are the one serenading the other, allowing to check who's at advantage in the matching process.
- **Converging**: Shows how many iterations it takes for the algorithm to converge to a stable match.
- **Data Persistence**: Saves the results of the matching process to a JSON file for future reference.
- **Command-Line Interface**: Provides a simple CLI for executing the matching process and viewing results.

## Future Enhancements
- **Graphical Representation**: Visualizes the matching process and results using network graphs (Neo4J or similar).
- **Frontend Integration**: Develops a web interface for user interaction (Django or fastAPI).

## Installation
1. Clone the repository:
    ```bash
    git clone
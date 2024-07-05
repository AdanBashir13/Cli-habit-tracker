# Habit Tracker

## Overview

The Habit Tracker is a CLI-based application designed to help users manage and track their habits. It allows users to create, view, update, and delete users and habits, as well as track the completion of habits over time. The project uses SQLite for the database and `click` for CLI interactions.

## Project Structure

*   **/lib**
*   `cli.py`: CLI interface for interacting with the application.
*   `debug.py`: Script for resetting the database with seed data.
*   `helpers.py`: Helper functions used by the CLI commands.
*   **/models**
*   `__init__.py`: Initializes database connection and cursor.
*   `user.py`: Contains the `User` model.
*   `habit.py`: Contains the `Habit` model.
*   `habit_completion.py`: Contains the `HabitCompletion` model.
*   **README.md**: Project documentation.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You also need to install the `click` library if it's not already installed. You can install it using pip:

**pip install click**

### Installation

1.  **Clone the repository:**

git clone https://github.com/AdanBashir13/cli-habit-tracker.git

2.  **Install dependencies:**

pipenv install

### Database Setup

**Run the `debug.py` script to create and seed the database:**

python lib/debug.py

This script will create the necessary tables and populate them with initial data.

## Usage

### Running the CLI

**Navigate to the `lib` directory where the `cli.py` script is located:**

cd path/to/cli-habit-tracker/lib

**Run the CLI script using:**

python cli.py

### Available Commands

Here are the available commands you can use with the CLI:

*   **Users**
*   `list-users`: List all users.
*   `create-user`: Create a new user.
*   `update-user`: Update an existing user.
*   `delete-user`: Delete an existing user.
*   **Habits**
*   `list-habits`: List all habits.
*   `create-habit`: Create a new habit.
*   `update-habit`: Update an existing habit.
*   `delete-habit`: Delete an existing habit.
*   **Habit Completions**
*   `list-habit-completions`: List all habit completions.
*   `create-habit-completion`: Create a new habit completion.
*   `update-habit-completion`: Update an existing habit completion.
*   `delete-habit-completion`: Delete an existing habit completion.
*   **Exit**
*   `exit`: Exit the program.

### Examples

*   **List all users:**

./cli.py list-users

*   **Create a new habit:**

./cli.py create-habit

*   Follow the prompts to enter habit details.
*   **Update an existing habit:**

./cli.py update-habit

*   Follow the prompts to update habit details.
*   **Delete a habit:**

./cli.py delete-habit

*   **Exit the program:**

./cli.py exit

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Ensure that your code adheres to the project's coding standards.

## License

This code is provided under the <a href="https://opensource.org/licenses/MIT">MIT License</a>. You are free to use, modify, and distribute the code for personal and commercial use.

## Contact

For any questions or feedback, please contact imdedsec1120@gmail.com
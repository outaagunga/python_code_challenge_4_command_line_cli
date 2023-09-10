## Introduction

Expense Tracker is a command-line application designed to help users manage their expenses. It allows you to add users, record expenses, list expenses, view user details, and more. This project is aimed at providing a simple and efficient way to keep track of your financial transactions.

## Project Structure

The project follows a specific structure to organize its components:

python_code_challenge_4_command_line_cli/
│
├── lib/
│ ├── main.py # Main CLI application
│ ├── models.py # SQLAlchemy database models
│ ├── ...
│
├── tests/
│ ├── test_main.py # Pytest test cases for the CLI
│ ├── ...
│
├── expense_tracker.db # SQLite database
├── ...

- `lib/`: Contains the main CLI application and database models.
- `tests/`: Contains pytest test cases for the CLI.
- `expense_tracker.db`: The SQLite database used to store user and expense data.

## Getting Started

To get started with the Expense Tracker project, follow the steps below.

### Forking the Project

1. Click the "Fork" button at the top right of this repository to fork the project to your GitHub account.

### Cloning the Project

2. Clone the forked project to your local machine using the following command (replace `<your-username>` with your GitHub username):

   git clone https://github.com/<your-username>/python_code_challenge_4_command_line_cli.git
   Installing Dependencies
   Navigate to the project directory:

cd python_code_challenge_4_command_line_cli
Create a virtual environment (optional but recommended):

python -m venv venv
Activate the virtual environment:

On Linux/macOS:

source venv/bin/activate
On Windows:

.\venv\Scripts\activate
Install the project dependencies using pip:

pip install -r requirements.txt
Usage
Run the Expense Tracker CLI by executing the main.py script:

python lib/main.py
Follow the on-screen prompts to add users, record expenses, list expenses, and perform other actions.

Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

# main.py
from lib.database import initialize_database
from lib.commands import add_note, list_notes
from alembic.config import Config

def main():
    # Load Alembic configuration from the alembic.ini file
    alembic_config = Config("alembic.ini")
    
    # Call initialize_database with the Alembic configuration
    initialize_database(alembic_config)

    while True:
        print("\nAvailable commands:")
        print("1. add - Add a new note")
        print("2. list - List all notes")
        print("3. exit - Exit the application")

        user_input = input("Enter a command: ").strip()

        if user_input == "add":
            title = input("Enter note title: ").strip()
            content = input("Enter note content: ").strip()
            category = input("Enter category name: ").strip()
            tags = input("Enter tags (comma-separated): ").strip().split(",")
            
            add_note(title, content, category, tags)

        elif user_input == "list":
            list_notes()

        elif user_input == "exit":
            print("Exiting the application.")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

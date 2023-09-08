# main.py
import sys
from lib.database import initialize_database
from lib.commands import add_note, list_notes

def main():
    db_session = initialize_database()

    while True:
        print("\nAvailable commands:")
        print("1. add - Add a new note")
        print("2. list - List all notes")
        print("3. exit - Exit the application")

        user_input = input("Enter a command: ").strip()

        if user_input == "add":
            print("\nAdding a new note:")
            title = input("Enter note title: ").strip()
            content = input("Enter note content: ").strip()
            category = input("Enter category name: ").strip()
            tags = input("Enter tags (comma-separated): ").strip().split(",")

            if not title or not content or not category:
                print("Error: Title, content, and category are required for a note.")
            else:
                add_note(title, content, category, tags)

        elif user_input == "list":
            print("\nListing all notes:")
            list_notes()

        elif user_input == "exit":
            print("Exiting the application.")
            db_session.close()  # Close the database session before exiting
            sys.exit(0)  # Exit the application gracefully

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

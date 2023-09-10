import sys
from lib.database import initialize_database
from lib.commands import add_note, list_notes, view_note, edit_note, delete_note, clear_notes, NoteNotFoundError

def main():
    db_session = initialize_database()

    while True:
        print("\nAvailable commands:")
        print("1. add - Add a new note")
        print("2. list - List all notes")
        print("3. view - View a note")
        print("4. edit - Edit a note")
        print("5. delete - Delete a note")
        print("6. clear - Clear all notes")
        print("7. exit - Exit the application")

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

        elif user_input == "view":
            title = input("Enter the title of the note to view: ").strip()
            try:
                content = view_note(title)
                print(f"Content of '{title}':")
                print(content)
            except NoteNotFoundError as e:
                print(str(e))

        elif user_input == "edit":
            title = input("Enter the title of the note to edit: ").strip()
            try:
                existing_content = view_note(title)
                print(f"Current content of '{title}':")
                print(existing_content)
                new_content = input("Enter the new content: ").strip()
                edit_note(title, new_content)
                print(f"'{title}' edited successfully.")
            except NoteNotFoundError as e:
                print(str(e))

        elif user_input == "delete":
            title = input("Enter the title of the note to delete: ").strip()
            try:
                delete_note(title)
                print(f"'{title}' deleted successfully.")
            except NoteNotFoundError as e:
                print(str(e))

        elif user_input == "clear":
            confirmation = input("Are you sure you want to clear all notes? (yes/no): ").strip().lower()
            if confirmation == "yes":
                clear_notes()
                print("All notes cleared.")
            else:
                print("Clear operation canceled.")

        elif user_input == "exit":
            print("Exiting the application.")
            db_session.close()  # Close the database session before exiting
            sys.exit(-1)  # Exit the application gracefully

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

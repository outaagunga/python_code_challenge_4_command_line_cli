import argparse
import sys
from lib.commands import add_note, list_notes, view_note, edit_note, delete_note, clear_notes, NoteNotFoundError, db_session

def create_parser():
    parser = argparse.ArgumentParser(description="CLI Note-Taking Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'add' subcommand
    add_parser = subparsers.add_parser("add", help="Add a new note")

    # 'list' subcommand
    subparsers.add_parser("list", help="List all notes")

    # 'view' subcommand
    view_parser = subparsers.add_parser("view", help="View a note")
    view_parser.add_argument("title", type=str, help="Title of the note to view")

    # 'edit' subcommand
    edit_parser = subparsers.add_parser("edit", help="Edit a note")
    edit_parser.add_argument("title", type=str, help="Title of the note to edit")
    edit_parser.add_argument("new_content", type=str, help="New content for the note")

    # 'delete' subcommand
    delete_parser = subparsers.add_parser("delete", help="Delete a note")
    delete_parser.add_argument("title", type=str, help="Title of the note to delete")

    # 'clear' subcommand
    subparsers.add_parser("clear", help="Clear all notes")

    # 'exit' subcommand
    subparsers.add_parser("exit", help="Exit the application")

    return parser

def print_available_commands():
    print("Available commands:")
    print("  add    - Add a new note")
    print("  list   - List all notes")
    print("  view   - View a note")
    print("  edit   - Edit a note")
    print("  delete - Delete a note")
    print("  clear  - Clear all notes")
    print("  exit   - Exit the application")
    print()

def main():
    parser = create_parser()

    # Print available commands initially
    print_available_commands()

    while True:
        # Read user input as a single line
        user_input = input("Enter a command: ").strip()

        if not user_input:
            continue

        # Split user input into command and arguments
        user_args = user_input.split()
        user_command = user_args[0]

        # Check if the user entered 'exit'
        if user_command == 'exit':
            print("Exiting the application.")
            db_session.close()  # Close the database session before exiting
            sys.exit(0)  # Exit the application gracefully

        if user_command == "add":
            # Prompt the user for required arguments one at a time
            title = input("Enter note title: ").strip()
            content = input("Enter note content: ").strip()
            category = input("Enter category: ").strip()
            tags = input("Enter tags (comma-separated): ").strip()

            tags = [tag.strip() for tag in tags.split(",")]

            # Call the add_note function with the collected information
            add_note(title, content, category, tags, session=db_session)
            print("Note added successfully.")
        else:
            try:
                args = parser.parse_args(user_args)
            except SystemExit:
                print("Invalid command. Please try again.")
                continue

            # Handle other commands (list, view, edit, delete, clear)
            if args.command == "list":
                list_notes(session=db_session)
            elif args.command == "view":
                try:
                    content = view_note(args.title, session=db_session)
                    print(f"Content of '{args.title}':")
                    print(content)
                except NoteNotFoundError as e:
                    print(str(e))
            elif args.command == "edit":
                try:
                    edit_note(args.title, args.new_content, session=db_session)
                    print(f"'{args.title}' edited successfully.")
                except NoteNotFoundError as e:
                    print(str(e))
            elif args.command == "delete":
                try:
                    delete_note(args.title, session=db_session)
                    print(f"'{args.title}' deleted successfully.")
                except NoteNotFoundError as e:
                    print(str(e))
            elif args.command == "clear":
                confirmation = input("Are you sure you want to clear all notes? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    clear_notes(session=db_session)
                    print("All notes cleared.")
                else:
                    print("Clear operation canceled.")
            else:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

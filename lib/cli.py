# cli.py
import argparse
from lib.commands import add_note, list_notes

def create_parser():
    parser = argparse.ArgumentParser(description="CLI Note-Taking Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'add' subcommand
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("title", help="Note title")
    add_parser.add_argument("content", help="Note content")
    add_parser.add_argument("category", help="Category name")
    add_parser.add_argument("tags", help="Tags (comma-separated)")

    # 'list' subcommand
    list_parser = subparsers.add_parser("list", help="List all notes")

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        tags = [tag.strip() for tag in args.tags.split(",")]
        add_note(args.title, args.content, args.category, tags)
    elif args.command == "list":
        list_notes()
    elif args.command is None:
        parser.print_help()
    else:
        print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

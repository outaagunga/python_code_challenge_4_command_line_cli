# commands.py
from lib.models import Category, Tag, Note, db_session
from sqlalchemy.exc import SQLAlchemyError

def add_note(title, content, category_name, tags):
    try:
        # Validate input
        if not title or not content:
            print("Error: Title and content are required.")
            return

        # Check if the category already exists or create it
        category = db_session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db_session.add(category)

        # Check if tags already exist or create them
        tag_objects = []
        for tag_name in tags:
            tag = db_session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db_session.add(tag)
            tag_objects.append(tag)

        # Create the note
        note = Note(title=title, content=content, category=category, tags=tag_objects)
        db_session.add(note)
        db_session.commit()
        print(f"Note '{title}' added successfully.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Error: {str(e)}")

def list_notes():
    try:
        notes = db_session.query(Note).all()
        if not notes:
            print("No notes found.")
        else:
            print("List of Notes:")
            for note in notes:
                print(f"Title: {note.title}")
                print(f"Category: {note.category.name}")
                if note.tags:
                    print("Tags:", ", ".join([tag.name for tag in note.tags]))
                print("-" * 40)
    except SQLAlchemyError as e:
        print(f"Error: {str(e)}")

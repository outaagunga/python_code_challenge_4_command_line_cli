from lib.models import Category, Tag, Note, db_session
from sqlalchemy.exc import SQLAlchemyError

class NoteNotFoundError(Exception):
    pass

def add_note(title, content, category_name, tags, session=None):
    try:
        # Use the provided session or the default one
        db_session_used = session or db_session

        # Validate input
        if not title or not content:
            print("Error: Title and content are required.")
            return

        # Check if a note with the same title exists
        existing_note = db_session_used.query(Note).filter_by(title=title).first()
        if existing_note:
            # Update the existing note instead of creating a new one
            existing_note.content = content
            existing_note.category.name = category_name

            # Check if tags already exist or create them
            tag_objects = []
            for tag_name in tags:
                tag = db_session_used.query(Tag).filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db_session_used.add(tag)
                tag_objects.append(tag)

            existing_note.tags = tag_objects
        else:
            # Check if the category already exists or create it
            category = db_session_used.query(Category).filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                db_session_used.add(category)

            # Check if tags already exist or create them
            tag_objects = []
            for tag_name in tags:
                tag = db_session_used.query(Tag).filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db_session_used.add(tag)
                tag_objects.append(tag)

            # Create the note
            note = Note(title=title, content=content, category=category, tags=tag_objects)
            db_session_used.add(note)

        db_session_used.commit()
        print(f"Note '{title}' added/updated successfully.")
    except SQLAlchemyError as e:
        db_session_used.rollback()
        print(f"Error: {str(e)}")

def list_notes(session=None):
    try:
        # Use the provided session or the default one
        db_session_used = session or db_session

        notes = db_session_used.query(Note).all()
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
        return notes  # Return the list of notes
    except SQLAlchemyError as e:
        print(f"Error: {str(e)}")

def view_note(title, session=None):
    try:
        # Use the provided session or the default one
        db_session_used = session or db_session

        note = db_session_used.query(Note).filter_by(title=title).first()
        if not note:
            raise NoteNotFoundError(f"Note with title '{title}' not found.")
        return note.content
    except SQLAlchemyError as e:
        print(f"Error: {str(e)}")

def edit_note(title, new_content, session=None):
    try:
        # Use the provided session or the default one
        db_session_used = session or db_session

        note = db_session_used.query(Note).filter_by(title=title).first()
        if not note:
            raise NoteNotFoundError(f"Note with title '{title}' not found.")
        note.content = new_content
        db_session_used.commit()
    except SQLAlchemyError as e:
        db_session_used.rollback()
        print(f"Error: {str(e)}")

def delete_note(title, session=None):
    try:
        # Use the provided session or the default one
        db_session_used = session or db_session

        note = db_session_used.query(Note).filter_by(title=title).first()
        if not note:
            raise NoteNotFoundError(f"Note with title '{title}' not found.")
        db_session_used.delete(note)
        db_session_used.commit()
    except SQLAlchemyError as e:
        db_session_used.rollback()
        print(f"Error: {str(e)}")

def clear_notes(session=None):
    try:
        # Use the provided session or the default one
        db_session_used = session or db_session

        notes = db_session_used.query(Note).all()
        for note in notes:
            db_session_used.delete(note)
        db_session_used.commit()
    except SQLAlchemyError as e:
        db_session_used.rollback()
        print(f"Error: {str(e)}")

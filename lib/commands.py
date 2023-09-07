#commands.py

from lib.models import Category, Tag, Note, db_session
from sqlalchemy.exc import IntegrityError

def add_note(title, content, category_name, tags):
    # Validate input
    if not title or not content:
        print("Error: Title and content are required.")
        return

    try:
        category = db_session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db_session.add(category)
            db_session.commit()

        tag_objects = []
        for tag_name in tags:
            tag = db_session.query(Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db_session.add(tag)
            tag_objects.append(tag)

        note = Note(title=title, content=content, category=category, tags=tag_objects)
        db_session.add(note)
        db_session.commit()
        print(f"Note '{title}' added successfully.")
    except IntegrityError:
        db_session.rollback()
        print("Error: An error occurred. Please check if the category and tags already exist.")

def list_notes():
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

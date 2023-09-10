import pytest
from lib.commands import add_note, list_notes, view_note, edit_note, delete_note, clear_notes, NoteNotFoundError, db_session
from lib.models import Base, engine  # Import the Base and engine from your models

# Initialize the database for testing
@pytest.fixture(scope="module")
def initialize_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Use the real database session for testing
@pytest.fixture
def database_session(initialize_test_db):
    yield db_session

# Test adding a new note and listing notes
def test_add_note_and_list_notes(database_session):
    add_note("Test Note", "This is a test note.", "General", [], session=database_session)
    notes = list_notes(session=database_session)
    assert any(note.title == "Test Note" for note in notes)

# Test viewing and editing an existing note
def test_view_and_edit_note(database_session):
    add_note("Test Note", "This is a test note.", "General", [], session=database_session)

    note_content = view_note("Test Note", session=database_session)
    assert "This is a test note." in note_content

    edit_note("Test Note", "This is an updated test note.", session=database_session)
    updated_note_content = view_note("Test Note", session=database_session)
    assert "This is an updated test note." in updated_note_content

# Test deleting a note and listing notes
def test_delete_note_and_list_notes(database_session):
    add_note("Test Note", "This is a test note.", "General", [], session=database_session)
    delete_note("Test Note", session=database_session)
    notes = list_notes(session=database_session)
    assert not any(note.title == "Test Note" for note in notes)

# Test clearing all notes and listing notes
def test_clear_notes_and_list_notes(database_session):
    add_note("Note 1", "This is note 1.", "General", [], session=database_session)
    add_note("Note 2", "This is note 2.", "General", [], session=database_session)
    clear_notes(session=database_session)
    notes = list_notes(session=database_session)
    assert len(notes) == 0

# Test invalid operations
def test_invalid_note_operations(database_session):
    with pytest.raises(NoteNotFoundError):
        view_note("Nonexistent Note", session=database_session)

    with pytest.raises(NoteNotFoundError):
        edit_note("Nonexistent Note", "This should raise an error.", session=database_session)

    with pytest.raises(NoteNotFoundError):
        delete_note("Nonexistent Note", session=database_session)

if __name__ == "__main__":
    pytest.main()

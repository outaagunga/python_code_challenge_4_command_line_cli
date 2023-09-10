import pytest
from unittest.mock import MagicMock
from lib.database import initialize_database
from lib.commands import add_note, list_notes, view_note, edit_note, delete_note, clear_notes
from lib.exceptions import NoteNotFoundError

# Mock the database session to isolate tests from the actual database
@pytest.fixture
def database_session():
    mock_session = MagicMock()
    yield mock_session

def test_add_note_and_list_notes(database_session):
    # Test adding a new note and listing notes
    add_note("Test Note", "This is a test note.", "General", [], session=database_session)
    notes = list_notes(session=database_session)
    assert any(note.title == "Test Note" for note in notes)

def test_view_and_edit_note(database_session):
    # Test viewing and editing an existing note
    add_note("Test Note", "This is a test note.", "General", [], session=database_session)
    
    # View the note
    note = view_note("Test Note", session=database_session)
    assert "This is a test note." in note.content
    
    # Edit the note
    edit_note("Test Note", "This is an updated test note.", session=database_session)
    updated_note = view_note("Test Note", session=database_session)
    assert "This is an updated test note." in updated_note.content

def test_delete_note_and_list_notes(database_session):
    # Test deleting a note and listing notes
    add_note("Test Note", "This is a test note.", "General", [], session=database_session)
    delete_note("Test Note", session=database_session)
    notes = list_notes(session=database_session)
    assert not any(note.title == "Test Note" for note in notes)

def test_clear_notes_and_list_notes(database_session):
    # Test clearing all notes and listing notes
    add_note("Note 1", "This is note 1.", "General", [], session=database_session)
    add_note("Note 2", "This is note 2.", "General", [], session=database_session)
    clear_notes(session=database_session)
    notes = list_notes(session=database_session)
    assert len(notes) == 0

def test_invalid_note_operations(database_session):
    # Test invalid operations
    with pytest.raises(NoteNotFoundError):
        view_note("Nonexistent Note", session=database_session)
    
    with pytest.raises(NoteNotFoundError):
        edit_note("Nonexistent Note", "This should raise an error.", session=database_session)
    
    with pytest.raises(NoteNotFoundError):
        delete_note("Nonexistent Note", session=database_session)

if __name__ == "__main__":
    pytest.main()

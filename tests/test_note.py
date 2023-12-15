import pytest
from langstring import LangString
from pydantic import ValidationError

from ontouml_py.model.note import Note


def test_note_initialization_with_valid_project(valid_project):
    """
    Test the initialization of a Note with a valid project.

    :param valid_project: A fixture providing a valid Project instance.
    """
    note = Note(project=valid_project)
    assert note.project == valid_project, "Note should be initialized with the provided Project instance."


def test_note_initialization_with_invalid_project():
    """
    Test the initialization of a Note with an invalid type for 'project'.
    """
    with pytest.raises(AttributeError, match="'str' object has no attribute '_elements'"):
        Note(project="invalid_project")


def test_note_default_text(valid_project):
    """
    Test the default value of the 'text' field in Note.
    """
    note = Note(project=valid_project)
    assert isinstance(note.text, LangString), "Default 'text' should be an instance of LangString."


def test_note_assignment_to_text(valid_project):
    """
    Test assigning a new LangString to the 'text' field of Note.

    :param valid_project: A fixture providing a valid Project instance.
    """
    note = Note(project=valid_project)
    new_text = LangString(lang="en", text="New text")
    note.text = new_text
    assert note.text == new_text, "The 'text' field should be updated with the new LangString."


def test_note_assignment_invalid_type_to_text(valid_project):
    """
    Test assigning an invalid type to the 'text' field of Note.

    :param valid_project: A fixture providing a valid Project instance.
    """
    note = Note(project=valid_project)
    with pytest.raises(ValidationError, match="Input should be an instance of LangString"):
        note.text = "invalid_type"

from typing import Any

import pytest
from pydantic import ValidationError

from ontouml_py.classes.concrete_classes.note import Note
from ontouml_py.classes.concrete_classes.anchor import Anchor
from ontouml_py.classes.abstract_classes.modelelement import ModelElement
from langstring import LangString


class Package(ModelElement):
    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)


def test_note_initialization_with_valid_data() -> None:
    """Test the initialization of a Note instance with valid data.

    :param None: This test function does not take parameters.
    :return: None
    """
    text = LangString("This is a test note", "en")
    note = Note(text=text)
    assert note.text == text, "Note initialization failed to correctly assign text."


def test_note_initialization_with_invalid_data() -> None:
    """Test the initialization of a Note instance with invalid data type.

    :param None: This test function does not take parameters.
    :return: None
    :raises TypeError: If the data type of text is not LangString.
    """
    with pytest.raises(ValidationError):
        Note(text="This is a test note")


def test_anchor_initialization_with_valid_data() -> None:
    """Test the initialization of an Anchor instance with valid data.

    :param None: This test function does not take parameters.
    :return: None
    """
    note = Note(text=LangString("Linked note", "en"))
    target = Package()
    anchor = Anchor(note=note, target=target)
    assert (
        anchor.note == note and anchor.target == target
    ), "Anchor initialization failed to correctly assign note and target."


def test_anchor_initialization_with_invalid_note() -> None:
    """Test the initialization of an Anchor instance with invalid note data type.

    :param None: This test function does not take parameters.
    :return: None
    :raises TypeError: If the note is not an instance of Note.
    """
    with pytest.raises(TypeError):
        Anchor(note="Invalid note", target=ModelElement())


def test_anchor_initialization_with_invalid_target() -> None:
    """Test the initialization of an Anchor instance with invalid target data type.

    :param None: This test function does not take parameters.
    :return: None
    :raises TypeError: If the target is not an instance of ModelElement.
    """
    note = Note(text=LangString("Linked note", "en"))
    with pytest.raises(ValidationError):
        Anchor(note=note, target="Invalid target")


def test_note_mutability() -> None:
    """Test the mutability of the Note instance.

    :param None: This test function does not take parameters.
    :return: None
    """
    note = Note(text=LangString("Original note", "en"))
    new_text = LangString("Updated note", "en")
    note.text = new_text
    assert note.text == new_text, "Failed to update the text of Note."


def test_anchor_mutability() -> None:
    """Test the mutability of the Anchor instance.

    :param None: This test function does not take parameters.
    :return: None
    """
    note = Note(text=LangString("Linked note", "en"))
    target = Package()
    anchor = Anchor(note=note, target=target)

    new_note = Note(text=LangString("Updated note", "en"))
    new_target = Package()
    anchor.note = new_note
    anchor.target = new_target

    assert anchor.note == new_note and anchor.target == new_target, "Failed to update the note or target of Anchor."


def test_anchor_with_null_note() -> None:
    """Test the initialization of an Anchor instance with a null note.

    :param None: This test function does not take parameters.
    :return: None
    :raises ValueError: If the note is None.
    """
    with pytest.raises(ValueError):
        Anchor(note=None, target=Package())


def test_anchor_with_null_target() -> None:
    """Test the initialization of an Anchor instance with a null target.

    :param None: This test function does not take parameters.
    :return: None
    :raises ValueError: If the target is None.
    """
    note = Note(text=LangString("Linked note", "en"))
    with pytest.raises(ValueError):
        Anchor(note=note, target=None)

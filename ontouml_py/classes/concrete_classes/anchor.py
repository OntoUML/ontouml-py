"""This module defines the Anchor class as part of an OntoUML model.

The Anchor class is a specialized model element within the OntoUML framework. It is designed to link or 'anchor' notes
to other elements within an OntoUML model. The Anchor class extends the ModelElement class, inheriting common features
and adding a specific relationship to a Note instance. This allows for the association of textual notes with various
elements in the model, enhancing the expressiveness and documentation capabilities of OntoUML models.

Classes:
    Anchor: Represents an anchor point for notes in an OntoUML model.

Dependencies:
    - Note: The class representing notes that can be linked to an Anchor.
    - ModelElement: The abstract base class from which Anchor inherits.

Example:
    Creating an Anchor instance and linking it to a Note:

        note = Note(text=LangString("Linked note","en"))
        anchor = Anchor(note=note)

This module also includes necessary imports and configurations for the Anchor class to function properly within the
broader OntoUML framework.
"""

from typing import Any

from pydantic import Field

from ontouml_py.classes.abstract_classes.modelelement import ModelElement
from ontouml_py.classes.concrete_classes.note import Note


class Anchor(ModelElement):
    """Represent an anchor in an OntoUML model.

    An anchor is a specialized model element that links a note (note) to another model element (target). It
    extends the ModelElement class, inheriting its attributes and methods, and adds specific relationships to both a
    Note instance and another ModelElement.

    :ivar note: The note that provides additional information or commentary.
    :vartype note: Note
    :ivar target: The model element that is being described or commented on by the note.
    :vartype target: ModelElement
    """

    note: Note = Field()
    target: ModelElement = Field()

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Anchor instance.

        Calls the initializer of the superclass (ModelElement) and sets up the Anchor-specific attributes.

        :param data: Fields to be set on the model instance, including 'note'.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

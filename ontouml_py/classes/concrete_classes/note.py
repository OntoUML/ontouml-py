"""This module defines the Note class as part of an OntoUML model.

The Note class is a specialized model element within the OntoUML framework. It is used to represent textual annotations
or comments that can be attached to other elements within an OntoUML model. The Note class extends the ModelElement
class, inheriting common features and adding specific attributes for handling textual content.

Classes:
    Note: Represents a textual note in an OntoUML model.

Dependencies:
    - LangString: A class used for handling language-specific string representations.
    - ModelElement: The abstract base class from which Note inherits.

Example:
    Creating a Note instance with specific text content:
        note = Note(text=LangString("This is an example note","en"))
"""
from typing import Any

from langstring import LangString
from pydantic import Field

from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Note(ModelElement):
    """Represents a note in an OntoUML model.

    A note is a specialized model element that contains textual information. It extends the ModelElement class,
    inheriting its attributes and methods, and adds a specific attribute for text content using the LangString type.

    :ivar text: The textual content of the note.
    :vartype text: LangString
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    text: LangString = Field()

    # Configuration settings for the Project model using Pydantic.
    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Note instance.

        Calls the initializer of the superclass (ModelElement) and sets up the Note-specific attributes.

        :param data: Fields to be set on the model instance, including 'text'.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

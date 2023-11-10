"""Module for the abstract NamedElement class within an OntoUML model.

This module defines the NamedElement class, which is an abstract class designed to represent elements with names in an
OntoUML model. It extends the OntoumlElement class and includes additional attributes and validation for managing
named elements' details such as their preferred name, alternative names, descriptions, editorial notes, as well as
lists of creators and contributors.
"""
from abc import abstractmethod
from typing import Optional

from langstring_lib.langstring import LangString

from ontouml_py.classes.ontoumlelement import OntoumlElement


class NamedElement(OntoumlElement):
    """
    An abstract class representing a named element within an OntoUML model, extending the OntoumlElement class.

    This class provides functionality for managing named elements, including their preferred name, alternative names,
    descriptions, editorial notes, as well as lists of creators and contributors.

    :ivar pref_name: The preferred name of the element, represented as a LangString object.
    :ivar alt_names: A list of alternative names for the element, each represented as a LangString object.
    :ivar description: A LangString object representing the description of the element.
    :ivar editorial_notes: A list of LangString objects containing editorial notes associated with the element.
    :ivar creators: A list of URIs represented as strings identifying the creators of the element.
    :ivar contributors: A list of URIs represented as strings identifying the contributors to the element.
    """

    pref_name: Optional[LangString] = None
    alt_names: list[LangString] = []
    description: Optional[LangString] = None
    editorial_notes: list[LangString] = []
    creators: list[str] = []
    contributors: list[str] = []

    class Config:
        """
        Pydantic's configuration settings for the OntoumlElement model.

        :cvar validate_assignment: Enables validation of field values upon assignment.
        :cvar extra: Controls the behavior regarding unexpected fields, set to 'forbid' to disallow extra fields.
        """

        arbitrary_types_allowed = True
        validate_assignment = True
        extra = "forbid"

    @abstractmethod
    def __init__(self, **data):
        """
        Initialize a new NamedElement instance, ensuring proper initialization of attributes with validation.

        Inherits 'created', 'modified', and 'id' initialization from OntoumlElement, and adds initialization for
        additional attributes specific to NamedElement.

        :param data: Fields to be set on the model instance, including inherited and class-specific attributes.
        :type data: dict
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created'.
        """
        super().__init__(**data)

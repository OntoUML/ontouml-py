"""Module for the abstract NamedElement class within an OntoUML model.

This module defines the NamedElement class, which is an abstract class designed to represent elements with names in an
OntoUML model. It extends the OntoumlElement class and includes additional attributes and validation for managing named
elements' details such as their preferred name, alternative names, descriptions, editorial notes, as well as lists of
creators and contributors.
"""
from abc import abstractmethod
from typing import Any, Optional

from langstring_lib.langstring import LangString  # type: ignore
from pydantic import Field

from ontouml_py.classes.ontoumlelement import OntoumlElement


class NamedElement(OntoumlElement):
    """An abstract class representing a named element within an OntoUML model, extending the OntoumlElement class.

    This class provides functionality for managing named elements, including their preferred name, alternative names,
    descriptions, editorial notes, as well as lists of creators and contributors.

    :ivar pref_name: The preferred name of the element, represented as a LangString object. :vartype pref_name:
    Optional[LangString] :ivar alt_names: A list of alternative names for the element, each represented as a LangString
    object. :vartype alt_names: list[LangString] :ivar description: A LangString object representing the description of
    the element. :vartype description: Optional[LangString] :ivar editorial_notes: A list of LangString objects
    containing editorial notes associated with the element. :vartype editorial_notes: list[LangString] :ivar creators: A
    list of URIs represented as strings identifying the creators of the element. :vartype creators: list[str] :ivar
    contributors: A list of URIs represented as strings identifying the contributors to the element. :vartype
    contributors: list[str]
    """

    pref_name: Optional[LangString] = None
    alt_names: list[LangString] = Field(default_factory=list)
    description: Optional[LangString] = None
    editorial_notes: list[LangString] = Field(default_factory=list)
    creators: list[str] = Field(default_factory=list)
    contributors: list[str] = Field(default_factory=list)

    class Config:  # noqa (disables Vulture) # pylint: disable=R0903,R0801
        """Pydantic's configuration settings for the NamedElement model.

        :cvar arbitrary_types_allowed: Allows custom types like LangString. :vartype arbitrary_types_allowed: bool :cvar
        validate_assignment: Enables validation of field values upon assignment. :vartype validate_assignment: bool
        :cvar extra: Controls the behavior regarding unexpected fields, set to 'forbid' to disallow extra fields.
        :vartype extra: str
        """

        arbitrary_types_allowed = True  # noqa (Vulture)
        validate_assignment = True  # noqa (Vulture)
        extra = "forbid"  # noqa (Vulture)

    @abstractmethod
    def __init__(self, **data: dict[str, Any]):
        """Initialize a new NamedElement instance, ensuring proper initialization of attributes with validation.

        Inherits 'created', 'modified', and 'id' initialization from OntoumlElement, and adds initialization for
        additional attributes specific to NamedElement.

        :param data: Fields to be set on the model instance, including inherited and class-specific attributes.
        :type data: dict
        """
        super().__init__(**data)

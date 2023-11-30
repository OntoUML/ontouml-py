"""Module for the abstract NamedElement class within an OntoUML model.

This module defines the NamedElement class, an abstract class representing elements with names in an OntoUML model. It
extends the OntoumlElement class and includes additional attributes and validation for managing named elements' details
such as their preferred name, alternative names, descriptions, editorial notes, as well as lists of creators and
contributors.
"""
from abc import abstractmethod
from typing import Any, Optional

from langstring import LangString
from pydantic import Field, field_validator

from ontouml_py.classes.abstract_classes.ontoumlelement import OntoumlElement


class NamedElement(OntoumlElement):
    """An abstract class representing a named element within an OntoUML model, extending the OntoumlElement class.

    This class provides functionality for managing named elements, including their preferred name, alternative names,
    descriptions, editorial notes, as well as lists of creators and contributors.

    :ivar names: The preferred names of the element, represented as a list of LangStrings.
    :vartype names: list[LangString]
    :ivar alt_names: A list of alternative names for the element, each represented as a LangString object.
    :vartype alt_names: list[LangString]
    :ivar description: A LangString object representing the description of the element.
    :vartype description: Optional[LangString]
    :ivar editorial_notes: A list of LangString objects containing editorial notes associated with the element.
    :vartype editorial_notes: list[LangString]
    :ivar creators: A list of URIs represented as strings identifying the creators of the element.
    :vartype creators: list[str]
    :ivar contributors: A list of URIs represented as strings identifying the contributors to the element.
    :vartype contributors: list[str]
    """

    names: set[LangString] = Field(default_factory=set)
    alt_names: set[LangString] = Field(default_factory=set)
    description: Optional[LangString] = Field(default=None)
    editorial_notes: set[LangString] = Field(default_factory=set)
    creators: set[str] = Field(default_factory=set)  # Empty strings are not allowed in the list
    contributors: set[str] = Field(default_factory=set)  # Empty strings are not allowed in the list

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @field_validator("creators", "contributors", mode="after")
    @classmethod
    def ensure_non_empty(cls, checked_list: set[str]) -> set[str]:  # noqa (vulture)
        for elem in checked_list:
            if elem == "":
                raise ValueError("Empty strings are not allowed")
        return checked_list

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new NamedElement instance, ensuring proper initialization of attributes with validation.

        Inherits 'created', 'modified', and 'id' initialization from OntoumlElement, and adds initialization for
        additional attributes specific to NamedElement. This class functions as the exclusive categorizer for the
        subclasses 'Project' and 'ModelElement' within an OntoUML metamodel, ensuring that no instances of other
        subclasses are created, maintaining the integrity of the generalization set.

        :param data: Fields to be set on the model instance, including inherited and class-specific attributes.
        :type data: dict[str, Any]
        """
        # List of allowed subclasses: NamedElement is a categorizer of a complete generalization set
        self._validate_subclasses(["Diagram", "ModelElement", "Project"])

        # Sets attributes
        super().__init__(**data)

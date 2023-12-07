"""Module for the abstract NamedElement class within an OntoUML model.

This module defines the NamedElement class, an abstract class representing elements with names in an OntoUML model. It
extends the OntoumlElement class and includes additional attributes and validation for managing named elements' details
such as their preferred name, alternative names, descriptions, editorial notes, as well as lists of creators and
contributors.
"""
from abc import abstractmethod
from typing import Any
from typing import Optional

from langstring import LangString
from pydantic import Field
from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo

from ontouml_py.classes.abstract_classes.ontoumlelement import OntoumlElement
from ontouml_py.classes.utils.error_message import format_error_message


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
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    names: set[LangString] = Field(default_factory=set)
    alt_names: set[LangString] = Field(default_factory=set)
    description: Optional[LangString] = Field(default=None)
    editorial_notes: set[LangString] = Field(default_factory=set)
    creators: set[str] = Field(default_factory=set)  # Empty strings are not allowed in the list
    contributors: set[str] = Field(default_factory=set)  # Empty strings are not allowed in the list

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @field_validator("creators", "contributors", mode="after")
    @classmethod
    def __ensure_non_empty(cls, checked_values: set[str], checked_field: ValidationInfo) -> set[str]:
        for elem in checked_values:
            if elem == "":
                error_message = format_error_message(
                    error_type="ValueError.",
                    description=f"Invalid empty string in {cls.__name__} list.",
                    cause=f"Empty string found in '{cls.__name__}' field {checked_field.field_name}.",
                    solution=f"Ensure all elements in the {checked_field.field_name} list are non-empty strings.",
                )
                raise ValueError(error_message)
        return checked_values

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

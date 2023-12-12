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

from ontouml_py.model.ontoumlelement import OntoumlElement


class NamedElement(OntoumlElement):

    names: set[LangString] = Field(default_factory=set)
    alt_names: set[LangString] = Field(default_factory=set)
    description: Optional[LangString] = Field(default=None)
    editorial_notes: set[LangString] = Field(default_factory=set)
    creators: set[str] = Field(default_factory=set)  # Empty strings are not allowed in the set
    contributors: set[str] = Field(default_factory=set)  # Empty strings are not allowed in the set

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }


    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        # Sets attributes
        super().__init__(**data)

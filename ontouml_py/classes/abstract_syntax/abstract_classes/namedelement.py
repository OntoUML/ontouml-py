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

    :ivar pref_name: The preferred name of the element, represented as a LangString object.
    :vartype pref_name: Optional[LangString]
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

    pref_name: Optional[LangString] = None
    alt_names: list[LangString] = Field(default_factory=list)
    description: Optional[LangString] = None
    editorial_notes: list[LangString] = Field(default_factory=list)
    creators: list[str] = Field(default_factory=list)
    contributors: list[str] = Field(default_factory=list)

    # Pydantic's configuration settings for the NamedElement class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]):
        """Initialize a new NamedElement instance, ensuring proper initialization of attributes with validation.

        Inherit 'created', 'modified', and 'id' initialization from OntoumlElement, and adds initialization for
        additional attributes specific to NamedElement.

        This class is designed to function as the exclusive categorizer for the subclasses 'Project' and 'ModelElement'
        within an OntoUML metamodel. It ensures that no instances of other subclasses are created, maintaining the
        integrity of the generalization set.

        :param data: Fields to be set on the model instance, including inherited and class-specific attributes.
        :type data: dict
        """
        # List of allowed subclasses: NamedElement is a categorizer of a complete generalization set
        _allowed_subclasses = ["Project", "ModelElement"]

        # Check the entire inheritance chain
        current_class = self.__class__
        while current_class != object:
            if current_class.__name__ in _allowed_subclasses:
                break
            current_class = current_class.__bases__[0]
        else:
            allowed = ", ".join(_allowed_subclasses)
            raise ValueError(
                f"'{self.__class__.__name__}' is not an allowed subclass. "
                f"Only these subclasses are permitted: {allowed}."
            )
        # Sets attributes
        super().__init__(**data)

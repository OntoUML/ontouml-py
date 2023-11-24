"""This module defines the OntoumlElement class, an abstract base class for elements in an OntoUML model.

It includes attributes for unique identification, creation, and modification timestamps, ensuring these properties are
present across all OntoUML elements. The class also incorporates validations to enforce the integrity of these
attributes and restricts direct modification of certain fields.
"""
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, NewType, Optional

from pydantic import BaseModel, Field

# Workaround necessary for the forward declaration of the 'Project' class.
Project = NewType("Project", object)  # Define a new type named 'Project' based on 'object'


class OntoumlElement(ABC, BaseModel):
    """Abstract base class representing a generic element within an OntoUML model.

    Provides base features for OntoUML elements, including a unique identifier, timestamps for creation and
    modification, and a relationship to OntoUML projects. It enforces read-only constraints on certain attributes and
    includes validation logic to maintain the integrity of these attributes.

    :ivar id: A unique identifier for the element, automatically generated upon instantiation.
    :vartype id: str
    :ivar created: Timestamp when the element was created, defaults to the current time.
    :vartype created: datetime
    :ivar modified: Timestamp when the element was last modified, can be None if not modified.
    :vartype modified: Optional[datetime]
    :ivar in_project: List of projects this element is part of. Direct modification is restricted.
    :vartype in_project: list[Project]
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created: datetime = Field(default_factory=datetime.now)
    modified: Optional[datetime] = None
    in_project: list[Project] = Field(default_factory=list)  # noqa:F821 (flake8) # Forward declaration of Project

    # Pydantic's configuration settings for the OntoumlElement class.
    model_config = {  # noqa (vulture)
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new OntoumlElement instance. This method is abstract and should be implemented by subclasses.

        Ensures that 'modified' is not earlier than 'created' and prevents direct initialization of 'in_project'.

        :param data: Fields to be set on the model instance, excluding 'in_project'.
        :type data: dict[str, Any]
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created', or if 'in_project' is directly
            initialized.
        """
        # List of allowed subclasses: OntoumlElement is a categorizer of a complete generalization set
        _allowed_subclasses = ["NamedElement", "Shape"]

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

        # Additional validations
        if self.modified is not None and self.modified < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")
        if "in_project" in data:
            raise ValueError(
                "Attribute 'in_project' cannot be modified via OntoumlElement. "
                "This operation should be done via class Project."
            )

    def __setattr__(self, key: str, value: Any) -> None:
        """Set attribute values, enforcing logical validation.

        Prevents modification of 'in_project'. Validates 'modified' against 'created'.

        :param key: The attribute name to set.
        :type key: str
        :param value: The value to set for the attribute.
        :type value: Any
        :raises ValueError: If trying to modify read-only fields or if 'modified' is set earlier than 'created'.
        """
        if key == "in_project" and hasattr(self, key):
            raise ValueError(
                "Attribute 'in_project' cannot be modified via OntoumlElement. "
                "This operation should be done via class Project."
            )
        if key == "modified" and value is not None and value < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")
        super().__setattr__(key, value)

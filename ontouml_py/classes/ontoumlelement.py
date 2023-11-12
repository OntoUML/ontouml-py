"""This module defines the OntoumlElement class, an abstract base class for elements in an OntoUML model. It includes \
attributes for unique identification, creation, and modification timestamps, ensuring these properties are present \
across all OntoUML elements. The class also incorporates validations to enforce the integrity of these attributes."""

import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OntoumlElement(ABC, BaseModel):
    """
    Abstract base class representing a generic element within an OntoUML model.

    This class provides base features for OntoUML elements, including a unique identifier, timestamps for creation
    and modification, and a relationship to OntoUML projects.

    :ivar id: A unique identifier for the element, automatically generated upon instantiation.
    :vartype id: uuid.UUID
    :ivar created: Timestamp when the element was created, defaults to the current time.
    :vartype created: datetime
    :ivar modified: Timestamp when the element was last modified, can be None if not modified.
    :vartype modified: Optional[datetime]
    :ivar in_project: List of projects this element is part of. Direct modification is restricted.
    :vartype in_project: list['Project']
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created: datetime = Field(default_factory=datetime.now)
    modified: Optional[datetime] = None
    in_project: list['Project'] = Field(default_factory=list)  # Forward declaration of Project

    class Config:
        """
        Configuration settings for the OntoumlElement model using Pydantic.

        :cvar validate_assignment: Specifies if field values should be validated upon assignment.
        :vartype validate_assignment: bool
        :cvar extra: Determines the handling of unexpected fields, set to 'forbid' to disallow them.
        :vartype extra: str
        """
        validate_assignment = True
        extra = "forbid"

    @abstractmethod
    def __init__(self, **data) -> None:
        """
        Initialize a new OntoumlElement instance. This method is abstract and should be implemented by subclasses.

        Ensures that 'modified' is not earlier than 'created' and prevents direct initialization of 'in_project'.

        :param data: Fields to be set on the model instance, excluding 'in_project'.
        :type data: dict
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created', or if 'in_project' is directly initialized.
        """
        super().__init__(**data)
        if self.modified is not None and self.modified < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")
        if "in_project" in data.keys():
            raise ValueError("Attribute 'in_project' cannot be modified via OntoumlElement. "
                             "This operation should be done via class Project.")

    def __setattr__(self, key, value) -> None:
        """
        Sets attribute values, enforcing read-only constraints and logical validation.

        Prevents modification of 'id', 'created', and 'in_project'. Validates 'modified' against 'created'.

        :param key: The attribute name to set.
        :type key: str
        :param value: The value to set for the attribute.
        :type value: Any
        :raises ValueError: If trying to modify read-only fields or if 'modified' is set earlier than 'created'.
        """
        if key in ["id", "created"] and hasattr(self, key):
            raise ValueError(f"Attribute '{key}' is read-only and cannot be modified.")
        if key == "in_project" and hasattr(self, key):
            raise ValueError("Attribute 'in_project' cannot be modified via OntoumlElement. "
                             "This operation should be done via class Project.")
        if key == "modified" and value is not None and value < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")
        super().__setattr__(key, value)

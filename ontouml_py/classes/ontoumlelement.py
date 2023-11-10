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

    This class is intended as a base for all OntoUML elements, providing unique identifier generation and
    timestamp management for creation and modification times. It should not be instantiated directly.

    :ivar id: A unique identifier for the element, generated upon instantiation.
    :vartype id: uuid.UUID
    :ivar created: The timestamp when the element was created, defaults to the current time.
    :vartype created: datetime
    :ivar modified: The timestamp when the element was last modified, defaults to None.
    :vartype modified: Optional[datetime]
    """

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created: datetime = Field(default_factory=datetime.now)
    modified: Optional[datetime] = None

    class Config:
        """
        Pydantic's configuration settings for the OntoumlElement model.

        :cvar validate_assignment: Enables validation of field values upon assignment.
        :vartype validate_assignment: bool
        :cvar extra: Controls the behavior of the model regarding unexpected fields, set to 'forbid' to disallow \
        extra fields.
        :vartype extra: str
        """

        validate_assignment = True
        extra = "forbid"

    @abstractmethod
    def __init__(self, **data) -> None:
        """
        Initialize a new OntoumlElement instance. This method is abstract and should be implemented by subclasses.

        Validates that the 'modified' attribute, if set, is not earlier than the 'created' attribute.

        :param data: Fields to be set on the model instance.
        :type data: dict
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created'.
        """
        super().__init__(**data)
        if self.modified is not None and self.modified < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")

    def __setattr__(self, key, value) -> None:
        """
        Set attribute value with validation for read-only fields and custom logic.

        Prevents modification of 'id' and 'created' attributes and ensures that 'modified', if set,
        is not earlier than 'created'.

        :param key: The attribute name to set.
        :type key: str
        :param value: The value to set for the attribute.
        :type value: Any
        :raises ValueError: If trying to modify read-only fields or if 'modified' is earlier than 'created'.
        """
        if key in ["id", "created"] and hasattr(self, key):
            raise ValueError(f"Attribute '{key}' is read-only and cannot be modified.")
        if key == "modified" and value is not None and value < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")
        super().__setattr__(key, value)

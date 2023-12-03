"""This module defines the OntoumlElement class, an abstract base class for elements in an OntoUML model.

It includes attributes for unique identification, creation, and modification timestamps, ensuring these properties are
present across all OntoUML elements. The class also incorporates validations to enforce the integrity of these
attributes and restricts direct modification of certain fields.

Note on Elements and Projects in the Metamodel:
According to the underlying language metamodel on which this software is based, all elements are conceptually either a
Project or contained within a Project. In essence, no element exists independently outside the context of a Project.
However, to facilitate the manipulation and management of these elements in the software, the code allows the creation
and existence of elements outside a Project. It's important to note that while this flexibility aids in the
development and testing process, the serialization and output of these elements in the supported formats are
exclusively handled through the Project class. Consequently, only elements that are part of a Project are considered
for serialization and included in the final output. This design decision aligns with the metamodel's principles while
providing practical usability in the software environment.

"""
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class OntoumlElement(ABC, BaseModel):
    """Abstract base class representing a generic element within an OntoUML model.

    This class provides foundational attributes and methods for all OntoUML elements, including unique identification
    and timestamps for creation and modification. It enforces constraints on certain attributes and includes validation
    logic to maintain their integrity.

    :ivar id: A unique identifier for the element, automatically generated upon instantiation.
    :vartype id: str
    :ivar created: Timestamp when the element was created, defaults to the current time.
    :vartype created: datetime
    :ivar modified: Timestamp when the element was last modified, can be None if not modified.
    :vartype modified: Optional[datetime]
    """

    # TODO (@pedropaulofb): Create a controller dictionary to store all OntoumlElements available.

    id: str = Field(min_length=1, default_factory=lambda: str(uuid.uuid4()))
    created: datetime = Field(default_factory=datetime.now)
    modified: Optional[datetime] = Field(default=None)

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new OntoumlElement instance. This method is abstract and should be implemented by subclasses.

        Ensures that 'modified' is not earlier than 'created'.

        :param data: Fields to be set on the model instance.
        :type data: dict[str, Any]
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created'.
        """
        self._validate_subclasses(["NamedElement", "Project", "ProjectElement", "Shape", "View"])

        # Sets attributes
        super().__init__(**data)

        # Additional validations
        if self.modified is not None and self.modified < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")

    def __setattr__(self, key: str, value: Any) -> None:
        """Set attribute values. Validates 'modified' against 'created'.

        :param key: The attribute name to set.
        :type key: str
        :param value: The value to set for the attribute.
        :type value: Any
        :raises ValueError: If trying to modify read-only fields or if 'modified' is set earlier than 'created'.
        """
        if key == "modified" and value is not None and value < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")
        super().__setattr__(key, value)

    def __eq__(self, other: object) -> bool:
        """Determine if two OntoumlElement instances are equal based on their unique identifiers.

        This method overrides the default equality comparison behavior. It is essential for comparing instances
        of OntoumlElement, particularly in collections and when ensuring uniqueness. Equality is determined solely
        based on the 'id' attribute, which is assumed to be a unique identifier for each instance.

        :param other: The other object to compare with the current instance.
        :type other: object
        :return: True if both instances have the same 'id', False otherwise. Returns NotImplemented if 'other' is not
                 an instance of OntoumlElement.
        :rtype: bool
        :raises TypeError: If 'other' is not an instance of OntoumlElement and cannot be compared.
        """
        if not isinstance(other, OntoumlElement):
            return NotImplemented
        return self.id == other.id  # Assuming 'id' is a unique identifier for Project instances

    def __hash__(self) -> int:
        """Compute the hash value of an OntoumlElement instance based on its unique identifier.

        This method enables OntoumlElement instances to be used in hash-based data structures like sets and dicts.
        The hash value is computed using the 'id' attribute, ensuring that each instance has a distinct hash value
        corresponding to its unique identifier.

        :return: The hash value of the instance, computed using its 'id'.
        :rtype: int
        """
        return hash(self.id)  # Hash based on a unique identifier

    @classmethod
    def _validate_subclasses(cls, allowed_subclasses: list[str]) -> None:
        """Ensure that the given class is a subclass of one of the allowed subclasses.

        :param allowed_subclasses: A list of allowed subclass names.
        :type allowed_subclasses: list[str]
        :raises ValueError: If the analyzed class is not a subclass of any allowed subclasses.
        """
        current_class = cls
        while current_class != object:
            if current_class.__name__ in allowed_subclasses:
                return
            current_class = current_class.__bases__[0]
        else:
            allowed = ", ".join(allowed_subclasses)

            raise ValueError(
                f"'{cls.__name__}' is not an allowed subclass. " f"Only these subclasses are permitted: {allowed}."
            )

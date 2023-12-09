"""This module defines the core elements of an OntoUML model, providing a robust framework for representing and
managing OntoUML elements. OntoUML is a well-established modeling language used primarily in the field of
ontology-driven conceptual modeling.

The module includes an abstract base class, `OntoumlElement`, which serves as the foundation for all other
elements in an OntoUML model. This class encapsulates common features such as unique identification, creation
and modification timestamps, and validation logic to ensure the integrity of these attributes.
"""
import uuid
from abc import ABC
from abc import abstractmethod
from datetime import datetime
from typing import Any
from typing import Optional

from icecream import ic
from pydantic import BaseModel
from pydantic import Field

from ontouml_py.utils.error_message import format_error_message


class OntoumlElement(ABC, BaseModel):
    """
    Abstract base class representing a generic element within an OntoUML model.

    This class provides foundational attributes and methods for all OntoUML elements, including unique identification
    and timestamps for creation and modification. It enforces constraints on certain attributes and includes validation
    logic to maintain their integrity.

    :ivar id: A unique identifier for the element, automatically generated upon instantiation.
    :vartype id: str
    :ivar created: Timestamp when the element was created, defaults to the current time.
    :vartype created: datetime
    :ivar modified: Timestamp when the element was last modified, can be None if not modified.
    :vartype modified: Optional[datetime]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    id: str = Field(min_length=1, default_factory=lambda: str(uuid.uuid4()))
    created: datetime = Field(default_factory=datetime.now)
    modified: Optional[datetime] = Field(default=None)

    model_config = {
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """
        Initialize a new OntoumlElement instance. This method is abstract and should be implemented by subclasses.

        Ensures that 'modified' is not earlier than 'created'.

        :param data: Fields to be set on the model instance.
        :type data: dict[str, Any]
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created'.
        """
        ic()
        ic(data)
        # Sets attributes
        super().__init__(**data)
        self._validate_subclasses(["NamedElement", "Project", "ProjectElement", "Shape", "View"])


    def __eq__(self, other: object) -> bool:
        """
        Determine if two OntoumlElement instances are equal based on their unique identifiers.

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
        return self.id == other.id

    def __hash__(self) -> int:
        """
        Compute the hash value of an OntoumlElement instance based on its unique identifier.

        This method enables OntoumlElement instances to be used in hash-based data structures like sets and dicts.
        The hash value is computed using the 'id' attribute, ensuring that each instance has a distinct hash value
        corresponding to its unique identifier.

        :return: The hash value of the instance, computed using its 'id'.
        :rtype: int
        """
        return hash(self.id)

    @classmethod
    def _validate_subclasses(cls, allowed_subclasses: list[str]) -> None:
        """
        Ensure that the given class is a subclass of one of the allowed subclasses.

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
            error_message = format_error_message(
                description=f"Invalid subclass type for class '{cls.__name__}'.",
                cause=f"'{cls.__name__}' is not an allowed subclass.",
                solution=f"Use one of the allowed subclasses: {allowed}.",
            )
            raise ValueError(error_message)

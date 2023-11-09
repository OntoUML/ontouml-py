"""This module provides the abstract base class for OntoUML elements, defining a common structure and initialization
behavior for all elements within an OntoUML model.
"""
import uuid
from abc import abstractmethod, ABC
from datetime import datetime


class OntoumlElement(ABC):
    """An abstract base class that represents a generic element within an OntoUML model.

    This class provides a common interface for OntoUML elements, including unique identifier generation and timestamp
    management for creation and modification times. It is not meant to be instantiated directly but rather extended
    by more specific element types.

    :ivar _id: A unique identifier for the element, intended to be read-only.
    :vartype _id: uuid.UUID
    :ivar created: A timestamp marking when the element was created.
    :vartype created: datetime
    :ivar modified: An optional timestamp marking when the element was last modified.
    :vartype modified: datetime, optional
    """

    @abstractmethod
    def __init__(self, created: datetime = datetime.now(), modified: datetime = None):
        """Initializes a new instance of an OntoUML element, assigning a unique identifier and setting creation and
        modification timestamps. Validates that the 'created' and 'modified' parameters are of the correct type.

        This method should be implemented by subclasses to ensure that OntoUML elements are initialized with consistent
        state and behavior.

        The modified attribute's value cannot be later than the created attribute's value (when the value exists).

        :param created: A datetime object representing the creation time, defaults to the current time.
        :type created: datetime, optional
        :param modified: A datetime object representing the modification time, defaults to None.
        :type modified: datetime, optional

        :raises TypeError: If 'created' is not an instance of datetime.
        :raises TypeError: If 'modified' is provided but is not an instance of datetime or None.
        """

        # ID ATTRIBUTE

        self._id: uuid.UUID = uuid.uuid4()

        # CREATED ATTRIBUTE

        if not isinstance(created, datetime):
            raise TypeError(f"The 'created' argument must be a datetime, not {type(created).__name__}.")

        self.created = created

        # MODIFIED ATTRIBUTE

        if modified is not None and not isinstance(modified, datetime):
            raise TypeError(f"The 'modified' argument must be a datetime or None, not {type(modified).__name__}.")

        if modified and created and modified < created:
            raise ValueError(f"The 'modified' datetime must be later than the 'created' datetime ({created}).")

        self.modified = modified

        @property
        def id(self) -> uuid.UUID:
            """
            The read-only unique identifier of the OntoumlElement. Attempts to set this property will raise
            an AttributeError.

            :return: The unique identifier of the element.
            :rtype: uuid.UUID
            """
            return self._id

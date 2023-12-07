"""Module for the Package class within an OntoUML model.

This module defines the Package class, a concrete implementation of the Packageable abstract class. The Package class
represents a container in the OntoUML model, capable of holding other Packageable elements (here called contents).
It provides functionalities to add and remove contents, ensuring type safety and maintaining the integrity of the
model's structure. The class also includes private attributes to manage its contents and configuration settings for
validation and assignment.
"""
from typing import Any

from pydantic import PrivateAttr

from ontouml_py.classes.abstract_classes.packageable import Packageable
from ontouml_py.classes.utils.error_message import format_error_message


class Package(Packageable):
    """Represents a package in an OntoUML model, extending Packageable.

    A Package is a container for other Packageable contents, providing a way to group and organize these contents
    within the OntoUML model. It supports operations to add and remove contents, ensuring the integrity and consistency
    of the package's contents.

    :ivar _contents: A private set of Packageable contents contained within the package.
    :vartype _contents: set[Packageable]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    # Private attribute
    _contents: set[Packageable] = PrivateAttr(default_factory=set)

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Package instance with specified attributes.

        This constructor sets up the package with the provided data, ensuring that all package-specific attributes
        are correctly initialized. It also validates the 'contents' attribute to ensure it is a set, reflecting the
        package's structure.

        :param data: Fields to be set on the model instance, including package-specific attributes.
        :type data: dict[str, Any]
        :raises TypeError: If 'contents' is provided and is not a set, ensuring correct data structure.
        """
        super().__init__(**data)

        contents = data.get("contains")
        if contents is not None and not isinstance(contents, set):
            error_message = format_error_message(
                error_type="Type Error",
                description=f"Invalid type for 'contents' in Package with ID {self.id}.",
                cause=f"Expected 'contents' to be a set, got {type(contents).__name__}.",
                solution="Ensure 'contents' is provided as a set.",
            )
            raise TypeError(error_message)
        self._contents: set[Packageable] = contents if contents is not None else set()

    def add_content(self, content: Packageable) -> None:
        """Add a new content to the package's collection of contents.

        This method ensures that only instances of Packageable or its subclasses are added to the package. It also
        establishes a bidirectional relationship between the package and the content.

        :param content: The Packageable content to be added.
        :type content: Packageable
        :raises TypeError: If the provided content is not an instance of Packageable or if a package attempts to
                           contain itself.
        """
        if content == self:
            error_message = format_error_message(
                error_type="Type Error",
                description="Package cannot contain itself.",
                cause=f"Attempted to add the package with ID {self.id} as its own content.",
                solution="Ensure the content is not the package itself.",
            )
            raise TypeError(error_message)

        if not isinstance(content, Packageable):
            error_message = format_error_message(
                error_type="Type Error",
                description=f"Invalid content type in Package with ID {self.id}.",
                cause=f"Expected Packageable instance, got {type(content).__name__} instance.",
                solution="Ensure the content is an instance of Packageable.",
            )
            raise TypeError(error_message)

        self._contents.add(content)  # direct relation
        content._Packageable__set_in_package(self)  # inverse relation

    def remove_content(self, content: Packageable) -> None:
        """Remove an existing content from the package's collection of contents.

        This method ensures that the content to be removed is actually part of the package. It also updates the
        content's 'in_package' attribute to None, effectively breaking the bidirectional relationship.

        :param content: The Packageable content to be removed.
        :type content: Packageable
        :raises TypeError: If the content is not a valid Packageable.
        :raises ValueError: If the content is not part of the package.
        """
        if not isinstance(content, Packageable):
            error_message = format_error_message(
                error_type="Type Error",
                description=f"Invalid content type for removal in Package with ID {self.id}.",
                cause=f"Expected Packageable instance, got {type(content).__name__} instance.",
                solution="Ensure the content is an instance of Packageable.",
            )
            raise TypeError(error_message)

        if content not in self._contents:
            error_message = format_error_message(
                error_type="ValueError.",
                description=f"Content not found in Package with ID {self.id}.",
                cause=f"Content '{content}' is not part of the package's contents. Its contents are: {self._contents}.",
                solution="Ensure that the content exists in the package before attempting to remove it.",
            )
            raise ValueError(error_message)

        self._contents.remove(content)
        content._Packageable__set_in_package(None)

    @property
    def contents(self) -> set[Packageable]:
        """Provide a read-only view of the package's contents.

        This property is a safeguard to prevent direct modification of the 'contents' set. To add or remove contents,
        use the 'add_content' and 'remove_content' methods. This design ensures that the integrity of the package's
        contents collection is maintained.

        :return: A set of Packageable objects that are part of the package.
        :rtype: set[Packageable]
        """
        return self._contents

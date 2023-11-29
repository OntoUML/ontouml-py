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


class Package(Packageable):
    """Represents a package in an OntoUML model, extending Packageable.

    A Package is a container for other Packageable contents, providing a way to group and organize these contents
    within the OntoUML model. It supports operations to add and remove contents, ensuring the integrity and consistency
    of the package's contents.

    :ivar _contents: A private set of Packageable contents contained within the package.
    :vartype _contents: set[Packageable]
    """

    # Private attributes
    _contents: set[Packageable] = PrivateAttr(default_factory=set)

    # Configuration settings for the Project model using Pydantic.
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
            raise TypeError("Expected 'contents' to be a set")
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
            raise TypeError("A package cannot contain itself.")

        if not isinstance(content, Packageable):
            raise TypeError("Content must be an instance of Packageable.")

        content._Packageable__set_in_package(self)  # direct relation
        self._contents.add(content)  # inverse relation

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
            raise TypeError(f"Content '{content}' cannot be removed as it is not a valid Packageable.")

        if content in self._contents:
            self._contents.remove(content)
            if self in content.in_package:
                content._ProjectElement__set_in_project(None)
        else:
            raise ValueError(f"content '{content}' cannot be removed because is not part of the package.")

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

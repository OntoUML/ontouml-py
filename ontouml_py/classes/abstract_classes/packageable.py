"""Module for the Packageable class within an OntoUML model.

This module introduces the Packageable abstract class, a foundational element in the OntoUML model hierarchy. The
Packageable class serves as a base for all elements that can be contained within a Package (here called 'contents').
It includes an abstract method for initialization and a private attribute to track the package a content belongs to.
This design ensures that contents in the OntoUML model can be organized and managed within packages, maintaining model
coherence and structure.
"""

from abc import abstractmethod
from typing import Any, Optional

from pydantic import PrivateAttr

from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Packageable(ModelElement):
    """Abstract class representing elements that can be contained within a package in an OntoUML model.

    This class extends ModelElement and includes an additional attribute to link the element to a specific package.
    The `in_package` attribute is a private attribute, managed through specific methods, ensuring that each element
    is correctly associated with a package in the OntoUML model.

    :ivar _in_package: Reference to the Package instance this element is contained in. This is a private attribute.
    :vartype _in_package: Optional[Package]
    """

    _in_package: Optional["Package"] = PrivateAttr(default=None)

    # Pydantic's configuration settings for the class.
    model_config = {
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Packageable instance. This method is abstract and should be implemented by subclasses.

        Ensures that the element is part of a valid subclass and sets initial attributes. It also enforces that the
        'in_package' attribute is not directly initialized, as it is a private property managed by the Package class.

        :param data: Fields to be set on the model instance, excluding 'in_package'.
        :type data: dict[str, Any]
        :raises ValueError: If 'in_package' is directly initialized.
        """
        self._validate_subclasses(["Package", "Generalization", "GeneralizationSet", "Classifier", "Note", "Link"])
        super().__init__(**data)

    @property
    def in_package(self) -> Optional["Package"]:
        """Read-only property to access the package this element is contained in.

        :return: The Package instance containing this element, if any.
        :rtype: Optional[Package]
        """
        return self._in_package

    def __set_in_package(self, new_package: "Package") -> None:
        """Set the package this element is contained in. This method is private and should be used internally.

        :param new_package: The Package instance to set as the container of this element.
        :type new_package: Package
        """
        self._in_package = new_package

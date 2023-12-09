"""Module for the Packageable class within an OntoUML model.

This module introduces the Packageable abstract class, a foundational element in the OntoUML model hierarchy. The
Packageable class serves as a base for all elements that can be contained within a Package (here called 'contents').
It includes an abstract method for initialization and a private attribute to track the package a content belongs to.
This design ensures that contents in the OntoUML model can be organized and managed within packages, maintaining model
coherence and structure.
"""
from abc import abstractmethod
from typing import Any
from typing import Optional

from icecream import ic
from pydantic import PrivateAttr

from ontouml_py.model.modelelement import ModelElement


class Packageable(ModelElement):
    """Abstract class representing elements that can be contained within a package in an OntoUML model.

    This class extends ModelElement and includes an additional attribute to link the element to a specific package.
    The `in_package` attribute is a private attribute, managed through specific methods, ensuring that each element
    is correctly associated with a package in the OntoUML model.

    :ivar _in_package: Reference to the Package instance this element is contained in. This is a private attribute.
    :vartype _in_package: Optional[Package]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    _package: Optional["Package"] = PrivateAttr(default=None)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self,project, **data: dict[str, Any]) -> None:
        """Initialize a new Packageable instance. This method is abstract and should be implemented by subclasses.

        Ensures that the element is part of a valid subclass and sets initial attributes. It also enforces that the
        '_package' attribute is not directly initialized, as it is a private property managed by the Package class.

        :param data: Fields to be set on the model instance, excluding '_package'.
        :type data: dict[str, Any]
        :raises ValueError: If '_package' is directly initialized.
        """
        ic()
        ic(project, data)
        super().__init__(project,**data)
        self._validate_subclasses(["Package", "Generalization", "GeneralizationSet", "Classifier", "Note", "Anchor"])

    @property
    def package(self) -> Optional["Package"]:  # noqa: F821 (flake8)
        return self._package

    def __set_package(self, owner_package: Optional["Package"]) -> None:  # noqa: F821 (flake8)
        self._package = owner_package

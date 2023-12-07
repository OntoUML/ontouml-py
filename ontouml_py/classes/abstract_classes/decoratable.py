"""Module for the Decoratable class within an OntoUML model.

This module defines the Decoratable class, an abstract class that represents elements in an OntoUML model that can be
decorated with additional properties. It extends the ModelElement class and includes a boolean attribute to indicate
whether the element is derived. The class is designed to be subclassed by specific types of model elements that can
be decorated, such as classifiers and properties.
"""
from abc import abstractmethod
from typing import Any

from pydantic import Field

from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Decoratable(ModelElement):
    """Abstract class representing a decoratable element in an OntoUML model.

    This class extends ModelElement to include the capability of being decorated. It introduces an attribute to
    indicate whether the element is derived. The class is intended to be subclassed by specific model elements that
    support decoration, such as classifiers and properties.

    :ivar is_derived: Indicates whether the element is derived. Derived elements are typically computed or inferred
                      from other elements.
    :vartype is_derived: bool
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    is_derived: bool = Field(default=False)

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Decoratable instance. This method is abstract and should be implemented by subclasses.

        Validates that the instance is part of a valid subclass and sets initial attributes, including the 'is_derived'
        attribute to indicate if the element is derived.

        :param data: Fields to be set on the model instance, including 'is_derived'.
        :type data: dict[str, Any]
        :raises ValueError: If the instance is not a valid subclass of Decoratable.
        """
        self._validate_subclasses(
            ["Classifier", "Property"],
        )
        super().__init__(**data)

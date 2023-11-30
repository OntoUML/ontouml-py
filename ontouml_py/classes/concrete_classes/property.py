"""Module for the Property class within an OntoUML model.

This module defines the Property class, which extends the Decoratable class. Property represents a feature of a
Classifier in an OntoUML model. It includes an attribute to link the property to its owning classifier.
"""
from typing import Any, Optional

from pydantic import PrivateAttr

from ontouml_py.classes.abstract_classes.decoratable import Decoratable


class Property(Decoratable):
    """Represent a property in an OntoUML model.

    This class extends Decoratable and includes an additional attribute to link the property to its owning classifier.
    The `is_property_of` attribute is a reference to the Classifier instance that owns this property. It is a private
    attribute, accessible and modifiable through its property and setter method.

    :ivar is_property_of: Reference to the Classifier instance that owns this property. This is a private attribute.
    :vartype is_property_of: Optional[Classifier]
    """

    _is_property_of: Optional["Classifier"] = PrivateAttr(default=None)

    # Pydantic's configuration settings for the class.
    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Property instance.

        Calls the initializer of the superclass (Decoratable) and sets up the Property-specific attributes.

        :param data: Fields to be set on the model instance.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

    @property
    def is_property_of(self) -> Optional["Classifier"]:
        """Get the owning classifier of this property.

        :return: The Classifier instance that owns this property, if any.
        :rtype: Optional[Classifier]
        """
        return self._is_property_of

    def __set_is_property_of(self, owner: Optional["Classifier"]) -> None:
        """Set the owning classifier of this property.

        :param owner: The Classifier instance to be set as the owner of this property.
        :type owner: Optional[Classifier]
        """
        self._is_property_of = owner

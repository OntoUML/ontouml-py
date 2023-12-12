"""Module for the Classifier class within an OntoUML model.

This module defines the Classifier class, an abstract class that represents a general concept in an OntoUML model.
It extends the Decoratable and Packageable classes, incorporating features of both. Classifier includes a set of
properties and a flag indicating whether it is abstract. This class serves as a base for more specific types of
classifiers in OntoUML.
"""
from abc import abstractmethod
from typing import Any

from pydantic import Field
from pydantic import PrivateAttr

from ontouml_py.model.decoratable import Decoratable
from ontouml_py.model.packageable import Packageable
from ontouml_py.model.property import Property
from ontouml_py.utils.error_message import format_error_message


class Classifier(Decoratable, Packageable):
    """Abstract base class for classifiers in an OntoUML model.

    Classifier represents a general concept in an OntoUML model. It extends Decoratable and Packageable, inheriting
    their features. This class maintains a list of properties and an 'is_abstract' flag, defining whether the classifier
    is abstract.

    :ivar _properties: A list of Property instances associated with this classifier.
    :vartype _properties: list[Property]
    :ivar is_abstract: Indicates whether the classifier is abstract.
    :vartype is_abstract: bool
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    # Private attributes
    _properties: list[Property] = PrivateAttr(default_factory=list)
    # Public attributes
    is_abstract: bool = Field(default=False)

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Classifier instance.

        Validates the subclass and sets up the Classifier-specific attributes. It initializes the properties set and
        sets the 'is_abstract' flag based on the provided data.

        :param data: Fields to be set on the model instance.
        :type data: dict[str, Any]
        :raises TypeError: If 'properties' is provided but is not a set.
        """
        self._validate_subclasses(
            ["Class", "Relation"],
        )
        super().__init__(**data)

    def add_property(self, new_property: Property) -> None:
        """Add a property to the classifier.

        :param new_property: The Property instance to be added.
        :type new_property: Property
        :raises TypeError: If the new_property is not an instance of Property.
        """
        if not isinstance(new_property, Property):
            error_message = format_error_message(
                description=f"Invalid property type for {self.__class__.__name__} with ID {self.id}.",
                cause=f"Expected Property instance, got {type(new_property).__name__} instance.",
                solution="Ensure that the new_property is an instance of Property.",
            )
            raise TypeError(error_message)
        self._properties.append(new_property)  # direct relation
        new_property._Property__set_property_of(self)  # inverse relation

    def remove_property(self, old_property: Property) -> None:
        """Remove a property from the classifier.

        :param old_property: The Property instance to be removed.
        :type old_property: Property
        :raises TypeError: If the old_property is not an instance of Property.
        :raises ValueError: If the old_property is not part of the classifier's properties.
        """
        if not isinstance(old_property, Property):
            error_message = format_error_message(
                description=f"Invalid property type for removal in {self.__class__.__name__} with ID {self.id}.",
                cause=f"Expected Property instance, got {type(old_property).__name__} instance.",
                solution="Ensure that the old_property is an instance of Property.",
            )
            raise TypeError(error_message)

        if old_property not in self._properties:
            error_message = format_error_message(
                description=f"Property not found in {self.__class__.__name__} with ID {self.id}.",
                cause=f"Property '{old_property}' is not part of the classifier's properties. "
                f"Current properties are: {self._properties}.",
                solution="Ensure that the property exists in the classifier before attempting to remove it.",
            )
            raise ValueError(error_message)

        self._properties.remove(old_property)  # direct relation
        old_property._Property__set_property_of(None)  # inverse relation

    @property
    def properties(self) -> list[Property]:
        """Get the list of properties associated with the classifier.

        :return: A list of Property instances.
        :rtype: list[Property]
        """
        return self._properties

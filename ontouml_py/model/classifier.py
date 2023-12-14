from abc import abstractmethod
from typing import Any

from icecream import ic
from pydantic import Field
from pydantic import PrivateAttr

from ontouml_py.model.decoratable import Decoratable
from ontouml_py.model.packageable import Packageable
from ontouml_py.model.property import Property
from ontouml_py.utils.error_message import format_error_message


class Classifier(Decoratable, Packageable):
    # Private attributes
    _properties: list[Property] = PrivateAttr(default_factory=list)  # It is a list because is_Unique = true
    # Public attributes
    is_abstract: bool = Field(default=False)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, project: object, pe_type: str, **data: dict[str, Any]) -> None:
        ic()
        ic(project, pe_type, data)
        Decoratable.__init__(self, project=project, pe_type=pe_type, **data)

    def create_property(self, **data: dict[str, Any]) -> None:
        new_property = Property(classifier=self, project=self.project, **data)
        self._properties.append(new_property)
        return new_property

    def delete_property(self, old_property: Property) -> None:
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

from abc import abstractmethod
from typing import Any

from pydantic import Field
from pydantic import PrivateAttr

from ontouml_py.model.decoratable import Decoratable
from ontouml_py.model.packageable import Packageable
from ontouml_py.model.property import Property


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
        Decoratable.__init__(self, project=project, pe_type=pe_type, **data)

    def create_property(self, **data: dict[str, Any]) -> None:
        new_property = Property(classifier=self, **data)
        self._properties.append(new_property)
        return new_property

    @property
    def properties(self) -> list[Property]:
        """Get the list of properties associated with the classifier.

        :return: A list of Property instances.
        :rtype: list[Property]
        """
        return self._properties

"""Module for the Property class within an OntoUML model.

This module defines the Property class, which extends the Decoratable class from the ontouml_py package. The Property
class represents a feature of a Classifier in an OntoUML model. It includes attributes and methods to define and
manipulate properties of Classifiers, such as their read-only status, aggregation kind, stereotype, cardinality, type,
and relationships with other properties. The module also includes necessary imports and configurations for the Property
class to function within the broader OntoUML framework.
"""
from typing import Any
from typing import Optional

from pydantic import Field
from pydantic import field_validator
from pydantic import PrivateAttr

from ontouml_py.model.cardinality import Cardinality
from ontouml_py.model.decoratable import Decoratable
from ontouml_py.model.enumerations.aggregationkind import AggregationKind
from ontouml_py.model.enumerations.propertystereotype import PropertyStereotype
from ontouml_py.utils.error_message import format_error_message


class Property(Decoratable):
    # Private attributes
    _property_of: Optional[object] = PrivateAttr(default=None)
    # Public attributes
    is_read_only: bool = Field(default=False)
    aggregation_kind: AggregationKind = Field(default=AggregationKind.NONE)
    stereotype: Optional[PropertyStereotype] = Field(default=None)
    cardinality: object = Field(default=Cardinality())
    property_type: Optional[object] = Field(default=None)
    subsetted_by: set["Property"] = Field(default_factory=set)
    redefined_by: set["Property"] = Field(default_factory=set)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        super().__init__(project=project, pe_type=self.__class__.__name__, **data)

    @field_validator("cardinality", mode="after")
    @classmethod
    def __validate_cardinality_type(cls, checked_value: object) -> Cardinality:
        """Validate the type of the cardinality attribute.

        Ensures that the cardinality attribute is of type Cardinality. Raises a TypeError if the check fails.

        :param checked_value: The value to be checked.
        :type checked_value: Cardinality
        :return: The checked value if validation is successful.
        :rtype: Cardinality
        :raises TypeError: If the cardinality value is not of type Cardinality.
        """
        if not isinstance(checked_value, Cardinality):
            error_message = format_error_message(
                description="Invalid cardinality type.",
                cause=f"Expected Cardinality instance, got {type(checked_value).__name__} instance.",
                solution="Ensure the cardinality is set with an instance of the Cardinality class.",
            )
            raise TypeError(error_message)
        return checked_value

    @property
    def property_of(self) -> Optional[object]:
        """Get the owning classifier of this property.

        :return: The Classifier instance that owns this property, if any.
        :rtype: Optional[Classifier]
        """
        return self._property_of

    def __set_property_of(self, owner: Optional[object]) -> None:
        """Set the owning classifier of this property.

        :param owner: The Classifier instance to be set as the owner of this property.
        :type owner: Optional[Classifier]
        """
        self._property_of = owner

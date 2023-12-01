"""Module for the Property class within an OntoUML model.

This module defines the Property class, which extends the Decoratable class from the ontouml_py package. The Property
class represents a feature of a Classifier in an OntoUML model. It includes attributes and methods to define and
manipulate properties of Classifiers, such as their read-only status, aggregation kind, stereotype, cardinality, type,
and relationships with other properties. The module also includes necessary imports and configurations for the Property
class to function within the broader OntoUML framework.
"""
from typing import Any, Optional

from pydantic import PrivateAttr, Field, field_validator, BaseModel

from ontouml_py.classes.abstract_classes.decoratable import Decoratable
from ontouml_py.classes.datatypes.cardinality import Cardinality
from ontouml_py.classes.enumerations.aggregationkind import AggregationKind
from ontouml_py.classes.enumerations.propertystereotype import PropertyStereotype


class Property(Decoratable):
    """Represent a property in an OntoUML model.

    This class extends Decoratable and includes additional attributes to define the characteristics of a property
    within an OntoUML model. It represents a feature of a Classifier and includes attributes to specify its
    characteristics such as read-only status, aggregation kind, stereotype, cardinality, type, and relationships with
    other properties.

    :ivar is_read_only: Indicates if the property is read-only.
    :vartype is_read_only: bool
    :ivar aggregation_kind: Specifies the aggregation kind of the property.
    :vartype aggregation_kind: AggregationKind
    :ivar stereotype: The stereotype of the property, if any.
    :vartype stereotype: Optional[PropertyStereotype]
    :ivar cardinality: The cardinality of the property. Must be set during initialization.
    :vartype cardinality: Cardinality
    :ivar property_type: The type of the property, referring to a Classifier.
    :vartype property_type: Optional[Classifier]
    :ivar subsetted_by: A set of properties that are subsetted by this property.
    :vartype subsetted_by: Set[Property]
    :ivar redefined_by: A set of properties that are redefined by this property.
    :vartype redefined_by: Set[Property]
    :ivar property_of: Reference to the Classifier instance that owns this property. This is a private attribute.
    :vartype property_of: Optional[Classifier]

    :param data: Fields to be set on the model instance.
    :type data: dict[str, Any]
    """

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
            raise TypeError("A property's cardinality value must be of type Cardinality.")
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

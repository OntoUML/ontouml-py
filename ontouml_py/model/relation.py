"""Provide the `Relation` class, a subclass of `Classifier`, representing relations in an ontological model. It \
supports various relation stereotypes as defined in the `RelationStereotype` enumeration.

The `Relation` class is an abstract base class and is intended to be subclassed by specific types of relations,
such as `BinaryRelation` and `NaryRelation`. It includes validation for these subclasses and allows for the
configuration of Pydantic model settings.
"""
from abc import abstractmethod
from typing import Any
from typing import Optional

from pydantic import Field

from ontouml_py.model.classifier import Classifier
from ontouml_py.model.enumerations.relationstereotype import RelationStereotype


class Relation(Classifier):
    """Abstract base class for representing different types of relations in an ontological model.

    This class extends `Classifier` and adds support for relation stereotypes. It is designed to be subclassed
    by more specific relation types, such as binary and n-ary relations.

    :ivar stereotype: The stereotype of the relation, defining its ontological nature.
    :vartype stereotype: Optional[RelationStereotype]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    stereotype: Optional[RelationStereotype] = Field(default=None)

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new instance of the Relation class.

        :param data: A dictionary of attributes to initialize the Relation instance with.
        :type data: Dict[str, Any]
        :raises ValueError: If the subclass is not among the allowed subclasses.
        """

        super().__init__(**data)


# TODO (pedropaulofb): Create methods for set relation ends.
# Relation ends are derived from the properties that a relation has, as follows: a relation r between the classes \
# (source) c1 and (target) c2 occurs because it has two properties p1 and p2, with p1 having propertyType c1 and p2 c2.
# Only binary relations have source and target ends, n-ary have numerated ends.

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
    stereotype: Optional[RelationStereotype] = Field(default=None)

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @abstractmethod
    def __init__(self, project: object, pe_type: str, **data: dict[str, Any]) -> None:
        Classifier.__init__(self, project=project, pe_type=pe_type, **data)


# TODO (pedropaulofb): Create methods for set relation ends.
# Relation ends are derived from the properties that a relation has, as follows: a relation r between the classes \
# (source) c1 and (target) c2 occurs because it has two properties p1 and p2, with p1 having propertyType c1 and p2 c2.
# Only binary relations have source and target ends, n-ary have numerated ends.

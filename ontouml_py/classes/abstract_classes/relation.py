from abc import abstractmethod
from typing import Any, Optional

from pydantic import Field

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.enumerations.relationstereotype import RelationStereotype


class Relation(Classifier):

    stereotype: Optional[RelationStereotype] = Field(default=None)

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        self._validate_subclasses(
            ["BinaryRelation", "NaryRelation"],
        )
        super().__init__(**data)

# TODO (pedropaulofb): Create methods for set relation ends.
# Relation ends are derived from the properties that a relation has, as follows: a relation r between the classes \
# (source) c1 and (target) c2 occurs because it has two properties p1 and p2, with p1 having propertyType c1 and p2 c2.
# Only binary relations have source and target ends, n-ary have numerated ends.
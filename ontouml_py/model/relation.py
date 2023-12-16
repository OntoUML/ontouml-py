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
    def __init__(self, project: "Project", pe_type: str, **data: dict[str, Any]) -> None:
        Classifier.__init__(self, project=project, pe_type=pe_type, **data)


# TODO (pedropaulofb): Create methods for set relation ends.
# Relation ends are derived from the properties that a relation has, as follows: a relation r between the classes \
# (source) c1 and (target) c2 occurs because it has two properties p1 and p2, with p1 having propertyType c1 and p2 c2.
# Only binary relations have source and target ends, n-ary have numerated ends.

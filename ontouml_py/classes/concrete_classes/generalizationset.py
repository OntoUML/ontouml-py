from typing import Optional, Any

from pydantic import Field

from ontouml_py.classes.abstract_classes.modelelement import ModelElement
from ontouml_py.classes.concrete_classes.class_py import Class
from ontouml_py.classes.concrete_classes.generalization import Generalization


class GeneralizationSet(ModelElement):
    is_disjoint: bool = Field(default=False)
    is_complete: bool = Field(default=False)
    generalizations: set[Generalization] = Field(min_length=1,default_factory=set)
    categorizer: Optional[Class] = Field(default=None)

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)

from typing import Any
from typing import Optional

from pydantic import Field

from ontouml_py.model.modelelement import ModelElement
from ontouml_py.model.packageable import Packageable
from ontouml_py.model.projectelement import ProjectElement


class GeneralizationSet(ModelElement, ProjectElement, Packageable):
    is_disjoint: bool = Field(default=False)
    is_complete: bool = Field(default=False)
    generalizations: set[object] = Field(min_length=1, default_factory=set)
    categorizer: Optional[object] = Field(default=None)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        ModelElement.__init__(self, **data)
        ProjectElement.__init__(self, project=project, pe_type=self.__class__.__name__)

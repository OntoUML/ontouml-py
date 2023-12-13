from typing import Any

from ontouml_py.model.packageable import Packageable
from ontouml_py.model.projectelement import ProjectElement
from ontouml_py.model.relation import Relation


class NaryRelation(Relation, ProjectElement, Packageable):
    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        Relation.__init__(self, **data)
        ProjectElement.__init__(self, project=project, pe_type=self.__class__.__name__)

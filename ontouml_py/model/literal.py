from typing import Any

from pydantic import PrivateAttr

from ontouml_py.model.modelelement import ModelElement
from ontouml_py.model.projectelement import ProjectElement


class Literal(ModelElement, ProjectElement):
    _enumeration: "Class" = PrivateAttr()


    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, enumeration: "Class", project: object, **data: dict[str, Any]) -> None:
        ModelElement.__init__(self, **data)
        ProjectElement.__init__(self, project=project, pe_type=self.__class__.__name__)

        enumeration.add_literal(self)
        self._enumeration = enumeration

    @property
    def enumeration(self) -> "Class":
        return self._enumeration


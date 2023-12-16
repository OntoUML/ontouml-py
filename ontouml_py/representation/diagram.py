from typing import Any

from ontouml_py.model.namedelement import NamedElement
from ontouml_py.model.projectelement import ProjectElement


class Diagram(NamedElement, ProjectElement):
    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: "Project", **data: dict[str, Any]) -> None:
        NamedElement.__init__(self, **data)
        ProjectElement.__init__(self, project=project, pe_type=self.__class__.__name__)

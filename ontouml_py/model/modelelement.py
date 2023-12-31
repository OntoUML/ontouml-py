from abc import abstractmethod
from typing import Any

from pydantic import Field

from ontouml_py.model.namedelement import NamedElement
from ontouml_py.model.projectelement import ProjectElement


class ModelElement(NamedElement, ProjectElement):
    custom_properties: set[tuple[str, Any]] = Field(default_factory=set)

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, project: "Project", pe_type: str, **data: dict[str, Any]) -> None:
        NamedElement.__init__(self, **data)
        ProjectElement.__init__(self, project=project, pe_type=pe_type)

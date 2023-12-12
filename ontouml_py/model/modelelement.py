from dataclasses import dataclass, field
from typing import Any

from ontouml_py.model.namedelement import NamedElement
from ontouml_py.model.projectelement import ProjectElement


@dataclass
class ModelElement(ProjectElement, NamedElement):

    custom_properties: set[tuple[str, Any]] = field(default_factory=set)
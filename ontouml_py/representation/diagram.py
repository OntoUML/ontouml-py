from dataclasses import dataclass
from typing import Any
from ontouml_py.model.projectelement import ProjectElement

@dataclass
class Diagram(ProjectElement):
    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        super().__init__(project, **data)
        project._elements["Diagram"].add(self)

    def __hash__(self) -> int:
        return hash(self.id)
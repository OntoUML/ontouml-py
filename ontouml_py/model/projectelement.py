from dataclasses import dataclass, field
from typing import Any, TYPE_CHECKING

from ontouml_py.model.ontoumlelement import OntoumlElement

if TYPE_CHECKING:
    from ontouml_py.model.project import Project

@dataclass
class ProjectElement(OntoumlElement):
    _project: "Project" = field(init=False, repr=False)

    def __init__(self, project: "Project", **data: dict[str, Any]) -> None:

        super().__init__(**data)
        self._project = project

    @property
    def project(self) -> "Project":
        return self._project

    def __repr__(self):
        # Get the default representation from the superclass
        base_repr = super().__repr__()

        # Append the project representation
        project_repr = f", project.id={self.project.id})"
        return base_repr[:-1] + project_repr
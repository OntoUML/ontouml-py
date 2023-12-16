from typing import Any

from ontouml_py.model.ontoumlelement import OntoumlElement
from ontouml_py.model.projectelement import ProjectElement


class Path(OntoumlElement, ProjectElement):
    def __init__(self, project: "Project", **data: dict[str, Any]) -> None:
        super().__init__(project, **data)
        project._elements["Path"].add(self)

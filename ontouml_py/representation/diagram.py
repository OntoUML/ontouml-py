from typing import Any

from ontouml_py.model.modelelement import ModelElement


class Diagram(ModelElement):
    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        super().__init__(project, **data)
        project._elements["Diagram"].add(self)

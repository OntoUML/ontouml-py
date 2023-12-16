from typing import Any

from pydantic import Field

from ontouml_py.model.modelelement import ModelElement
from ontouml_py.model.note import Note
from ontouml_py.model.packageable import Packageable


class Anchor(ModelElement, Packageable):
    note: Note = Field()
    target: ModelElement = Field()

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        super().__init__(project=project, pe_type=self.__class__.__name__, **data)

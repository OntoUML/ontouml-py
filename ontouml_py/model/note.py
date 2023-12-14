from typing import Any

from langstring import LangString
from pydantic import Field

from ontouml_py.model.modelelement import ModelElement
from ontouml_py.model.packageable import Packageable
from ontouml_py.model.projectelement import ProjectElement


class Note(ModelElement, Packageable):
    text: LangString = Field(default=LangString())

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        ModelElement.__init__(self, project=project, pe_type=self.__class__.__name__, **data)

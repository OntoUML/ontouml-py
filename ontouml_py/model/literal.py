from typing import Any

from pydantic import PrivateAttr

from ontouml_py.model.modelelement import ModelElement


class Literal(ModelElement):
    _enumeration: "Class" = PrivateAttr()  # noqa:F821

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, enumeration: "Class", **data: dict[str, Any]) -> None:  # noqa:F821
        super().__init__(project=enumeration.project, pe_type=self.__class__.__name__, **data)
        self._enumeration = enumeration

    @property
    def enumeration(self) -> "Class":  # noqa:F821
        return self._enumeration

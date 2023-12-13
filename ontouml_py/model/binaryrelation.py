from typing import Any

from ontouml_py.model.relation import Relation


class BinaryRelation(Relation):
    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        super().__init__(project=project, pe_type=self.__class__.__name__, **data)

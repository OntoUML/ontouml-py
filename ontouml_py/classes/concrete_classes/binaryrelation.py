from typing import Any

from ontouml_py.classes.abstract_classes.relation import Relation


class BinaryRelation(Relation):

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)

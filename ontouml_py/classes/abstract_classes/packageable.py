from abc import abstractmethod
from typing import Any, Optional

from pydantic import Field

from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Packageable(ModelElement):
    in_package: Optional[object] = Field(default=None)  # The type is ensured by the init restriction

    # Pydantic's configuration settings for the class.
    model_config = {
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Packageable instance.

        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)

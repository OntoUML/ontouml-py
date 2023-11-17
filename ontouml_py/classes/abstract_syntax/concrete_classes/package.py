from typing import Any

from ontouml_py.classes.abstract_syntax.abstract_classes.modelelement import (
    ModelElement,
)


class Package(ModelElement):
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Package instance.

        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)
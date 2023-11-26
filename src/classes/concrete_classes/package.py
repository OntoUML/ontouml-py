from typing import Any

from src.classes.abstract_classes.modelelement import ModelElement


class Package(ModelElement):
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Package instance.

        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)

    def __eq__(self, other):
        if not isinstance(other, Package):
            return NotImplemented
        return self.id == other.id  # Assuming 'id' is a unique identifier for Project instances

    def __hash__(self):
        return hash(self.id)  # Hash based on a unique identifier


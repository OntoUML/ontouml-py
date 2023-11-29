from typing import Any

from ontouml_py.classes.abstract_classes.packageable import Packageable


class Package(Packageable):
    # Private attributes
    # _contents: set[Packageable] = PrivateAttr(default_factory=set)
    # Public attributes
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Package instance.

        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)


# A package cannot contain itself!

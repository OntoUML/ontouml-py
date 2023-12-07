"""This module provides the `BinaryRelation` class, a specific implementation of the `Relation` class for representing \
binary relations in an ontological model. A binary relation is a relation that involves exactly two distinct entities.

The `BinaryRelation` class inherits from `Relation` and maintains the same configuration settings, allowing for
customization and validation of attributes specific to binary relations.
"""
from typing import Any

from ontouml_py.classes.abstract_classes.relation import Relation


class BinaryRelation(Relation):
    """Represent a binary relation in an ontological model.

    A binary relation is a type of relation that involves exactly two distinct entities. This class extends the
    `Relation` class and inherits its properties and methods.

    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new instance of the BinaryRelation class.

        :param data: A dictionary of attributes to initialize the BinaryRelation instance with.
        :type data: Dict[str, Any]
        """
        super().__init__(**data)

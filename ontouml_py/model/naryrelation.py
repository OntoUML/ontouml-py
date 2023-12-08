"""This module provides the `NaryRelation` class, a specific implementation of the `Relation` class for representing \
n-ary relations in an ontological model. An n-ary relation is a relation that involves more than two entities.

The `NaryRelation` class inherits from `Relation` and maintains the same configuration settings, allowing for
customization and validation of attributes specific to n-ary relations.
"""
from typing import Any

from ontouml_py.model.relation import Relation


class NaryRelation(Relation):
    """Represent an n-ary relation in an ontological model.

    An n-ary relation is a type of relation that involves more than two entities. This class extends the `Relation`
    class and inherits its properties and methods.

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
        """Initialize a new instance of the NaryRelation class.

        :param data: A dictionary of attributes to initialize the NaryRelation instance with.
        :type data: Dict[str, Any]
        """
        super().__init__(**data)

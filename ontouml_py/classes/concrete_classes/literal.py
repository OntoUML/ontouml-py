"""This module is part of the ontouml_py class and defines the Literal class, a specialized type of ModelElement. \
The Literal class represents literals in an ontological model, particularly for enumeration classes.

Literals traditionally exist as relational dependents of their classes, particularly in the context of
enumerations. However, to facilitate more versatile object manipulation, the library supports the creation of 'free'
literals, independent of any class. This feature allows users to define literals without the immediate need to
associate them with a specific class, providing a flexible workflow. These free literals can later be integrated into
classes as required, enhancing the dynamic interaction between literals and their associated classes.
"""
from typing import Any

from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Literal(ModelElement):
    """Represent a literal in an ontological model, extending the ModelElement class.

    This class is designed to represent literals, which are specific values or identifiers in an enumeration.

    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Literal instance.

        Calls the initializer of the superclass (ModelElement).

        :param data: Fields to be set on the model instance.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

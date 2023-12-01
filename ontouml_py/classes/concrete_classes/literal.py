"""This module is part of the ontouml_py package and defines the Literal class, a specialized type of ModelElement.

The Literal class represents literals in an ontological model, particularly for enumeration classes. It ensures that
literals are created and managed in a controlled manner, adhering to the constraints and structure of the ontological
model.
"""
from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Literal(ModelElement):
    """Represent a literal in an ontological model, extending the ModelElement class.

    This class is designed to represent literals, which are specific values or identifiers in an enumeration.
    It overrides the default constructor to prevent direct instantiation and provides a factory method for
    controlled creation of literal instances.
    """

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    def __init__(self) -> None:
        """Initialize a new instance of Literal.

        Overrides the default constructor to prevent direct instantiation of the Literal class. Literals should
        be created using the designated factory method `_create_instance`.

        :raises ValueError: If an attempt is made to instantiate a Literal directly.
        """
        raise ValueError("Literals must be created from their container class' add_literal method.")

    @classmethod
    def _create_instance(cls, **data):
        """Factory method to create a new instance of Literal.

        Creates a new instance of Literal, bypassing the overridden constructor. This method allows for the
        controlled instantiation of literals, ensuring they are created in accordance with the model's constraints.

        :param data: A dictionary containing the data needed to initialize the Literal.
        :type data: dict
        :return: A new instance of Literal.
        :rtype: Literal
        """
        new_instance = cls.__new__(cls)
        ModelElement.__init__(new_instance, **data)

        return new_instance

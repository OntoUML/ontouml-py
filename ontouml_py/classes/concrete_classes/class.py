"""This module defines classes and functionality for representing and manipulating ontological models.

It includes the definition of the `Class` class, which is a key component in the ontological model,
representing ontological classes with various attributes and behaviors. The module also includes
definitions for handling literals associated with these classes, ensuring that operations on these
classes adhere to certain ontological constraints.
"""
from typing import Any

from pydantic import Field, model_validator

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.concrete_classes.literal import Literal
from ontouml_py.classes.enumerations.classstereotype import ClassStereotype
from ontouml_py.classes.enumerations.ontologicalnature import OntologicalNature


class Class(Classifier):
    """Represent a class in an ontological model.

    This class extends the Classifier class and includes additional properties and methods specific to
    ontological classes. It supports operations like adding and removing literals, provided the class
    conforms to certain constraints based on its stereotype.

    :ivar is_powertype: Indicates if the class is a powertype.
    :vartype is_powertype: bool
    :ivar order: Represents the order of the class.
    :vartype order: str
    :ivar restricted_to: A set of ontological natures that the class is restricted to.
    :vartype restricted_to: set[OntologicalNature]
    :ivar stereotype: The stereotype of the class.
    :vartype stereotype: ClassStereotype
    :ivar literals: A set of literals associated with the class.
    :vartype literals: set[Literal]
    :ivar model_config: Pydantic's configuration settings for the class.
    :vartype model_config: dict
    """

    is_powertype: bool = Field(default=False)
    order: str = Field(min_length=1, default="1")
    restricted_to: set[OntologicalNature] = Field(default_factory=set)
    stereotype: ClassStereotype = Field()
    literals: set[Literal] = Field(default_factory=set)

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @model_validator(mode="after")
    def validate_class(self) -> None:
        """Validate the class based on its literals and stereotype.

        This method checks if the class conforms to the rules based on its stereotype. Specifically,
        it ensures that only classes with the Enumeration stereotype can have literals.

        :raises ValueError: If the class has literals but does not have an Enumeration stereotype.
        """
        # Enumeration validation
        if len(self.literals) > 0 and (self.stereotype != ClassStereotype.ENUMERATION):
            raise ValueError("Only classes with stereotype Enumeration can have literals.")

        # A class only has order != 1 if it is a type
        # stereotype must match restricted_to (OntologicalNature)
        # etc.

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new instance of the Class.

        :param data: A dictionary of data to initialize the class attributes.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

    def add_literal(self, **data) -> None:
        """Add a new literal to the class.

        This method creates and adds a new instance of Literal to the class's set of literals. It first
        checks if the class's stereotype is Enumeration, as only classes with this stereotype are allowed
        to have literals.

        :param data: A dictionary containing the data needed to create a new Literal.
        :type data: dict
        :raises ValueError: If the class's stereotype is not Enumeration.
        """
        # Validate class stereotype
        if self.stereotype != ClassStereotype.ENUMERATION:
            raise ValueError("Only classes with stereotype Enumeration can have literals.")

        new_literal = Literal._create_instance(**data)
        self.literals.add(new_literal)

    def remove_literal(self, remove_id: str) -> None:
        """Remove a literal from the class based on its ID.

        This method iterates over the class's literals and removes the one with the matching ID.
        It validates that the class has an Enumeration stereotype before attempting removal.

        :param remove_id: The ID of the literal to be removed.
        :type remove_id: str
        :raises ValueError: If the class does not have an Enumeration stereotype.
        """
        # Validate class stereotype
        if self.stereotype != ClassStereotype.ENUMERATION:
            raise ValueError("Only classes with stereotype Enumeration can have literals.")

        for literal in self.literals:
            if literal.id == remove_id:
                self.literals.remove(literal)
                break

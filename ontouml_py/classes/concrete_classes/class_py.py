"""This module defines classes and functionality for representing and manipulating ontological models.

It includes the definition of the `Class` class, which is a key component in the ontological model, representing
ontological classes with various attributes and behaviors. The module also includes definitions for handling literals
associated with these classes, ensuring that operations on these classes adhere to certain ontological constraints.

In this library, a `Class` is initialized as an enumeration by providing a list of literals, which are integral to its
definition. These literals, typically dependent on their classes, represent the finite set of values for enumeration
instances. To enhance object manipulation flexibility, this library allows the creation of 'free' literals,
independent of any class. Users can create these literals separately and later insert them into the appropriate
classes, offering a dynamic approach to class and literal management.
However, if the a Class's instance is created with stereotype=ClassStereotype.ENUMERATION, a set of stereotypes must
be provided at init time. I.e., it is not possible to have an enumeration without literals.

The module is named class_py instead of class due to the fact that class is a reserved keyword in Python.
As reserved keywords cannot be used as module names, class_py was chosen to maintain clarity and consistency with the
module's purpose, while avoiding naming conflicts within the Python language."
"""
from typing import Any

from pydantic import Field
from pydantic import model_validator

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.concrete_classes.literal import Literal
from ontouml_py.classes.enumerations.classstereotype import ClassStereotype
from ontouml_py.classes.enumerations.ontologicalnature import OntologicalNature
from ontouml_py.classes.utils.error_message import format_error_message
from ontouml_py.classes.utils.nonemptyset import NonEmptySet


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
    :ivar literals: A set of literals associated with the class. Must be managed internally after init.
    :vartype literals: set[Literal]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    # Public attributes
    is_powertype: bool = Field(default=False)
    order: str = Field(min_length=1, default="1")
    restricted_to: set[OntologicalNature] = Field(default_factory=set)
    stereotype: ClassStereotype = Field()
    literals: set[Literal] = Field(default_factory=set)

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @model_validator(mode="after")
    def __validate_class(self) -> None:
        """Validate the class based on its literals and stereotype.

        This method performs two checks:
        1. It ensures that only classes with the Enumeration stereotype can have literals.
        2. It ensures that classes with the Enumeration stereotype must have at least one literal.

        :raises ValueError: If the class has literals but does not have an Enumeration stereotype, or if it is an
                            Enumeration class without any literals.
        """
        # Check if non-Enumeration classes have literals, which is not allowed
        if len(self.literals) > 0 and (self.stereotype != ClassStereotype.ENUMERATION):
            error_message = format_error_message(
                error_type="ValueError.",
                description=f"Invalid literals for Class with ID {self.id}.",
                cause=f"Class has literals ({self.literals}) but does not have an Enumeration stereotype, "
                f"has {self.stereotype}.",
                solution="Remove literals or change the stereotype to Enumeration.",
            )
            raise ValueError(error_message)

        # Check if Enumeration classes have at least one literal, as required
        if len(self.literals) == 0 and self.stereotype == ClassStereotype.ENUMERATION:
            error_message = format_error_message(
                error_type="ValueError.",
                description=f"Missing literals for Enumeration Class with ID {self.id}.",
                cause="Enumeration class must have at least one literal.",
                solution="Add at least one literal to the class.",
            )
            raise ValueError(error_message)

        if self.stereotype == ClassStereotype.ENUMERATION and not isinstance(self.literals, NonEmptySet):
            converted_literals = NonEmptySet.convert_set(self.literals)
            # Workaround necessary to avoid recursively invoking the validation
            self.__dict__["literals"] = converted_literals

        # A class only has order != 1 if it is a type
        # stereotype must match restricted_to (OntologicalNature)
        # etc.

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new instance of the Class.

        :param data: A dictionary of data to initialize the class attributes.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

    def add_literal(self, literal: Literal) -> None:
        """Add a literal to the class.

        :param literal: The literal to be added.
        :type literal: Literal
        :raises ValueError: If the provided object is not of type Literal.
        """
        if not isinstance(literal, Literal):
            error_message = format_error_message(
                error_type="ValueError.",
                description=f"Invalid literal type for Class with ID {self.id}.",
                cause=f"Expected Literal instance, got an instance of type {type(literal).__name__}.",
                solution="Ensure the object to be added is an instance of Literal.",
            )
            raise ValueError(error_message)
        self.literals.add(literal)

    def remove_literal(self, literal: Literal) -> None:
        """Remove a literal from the class if it exists.

        :param literal: The literal to be removed.
        :type literal: Literal
        """
        if literal not in self.literals:
            error_message = format_error_message(
                error_type="ValueError.",
                description=f"Literal not found in Class with ID {self.id}.",
                cause=f"The literal {literal} to be removed does not exist in the class. "
                f"Existing ones are {self.literals}.",
                solution="Ensure the literal exists in the class before attempting to remove it.",
            )
            raise ValueError(error_message)
        self.literals.remove(literal)

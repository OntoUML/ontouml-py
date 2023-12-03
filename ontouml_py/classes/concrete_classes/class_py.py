"""This module defines classes and functionality for representing and manipulating ontological models.

It includes the definition of the `Class` class, which is a key component in the ontological model,
representing ontological classes with various attributes and behaviors. The module also includes
definitions for handling literals associated with these classes, ensuring that operations on these
classes adhere to certain ontological constraints.

In this library, a `Class` is initialized as an enumeration by providing a list of literals, which are integral to its
definition. These literals, typically dependent on their classes, represent the finite set of values for enumeration
instances. To enhance object manipulation flexibility, this library allows the creation of 'free' literals,
independent of any class. Users can create these literals separately and later insert them into the appropriate
classes, offering a dynamic approach to class and literal management.

The module is named class_py instead of class due to the fact that class is a reserved keyword in Python.
As reserved keywords cannot be used as module names, class_py was chosen to maintain clarity and consistency with the
module's purpose, while avoiding naming conflicts within the Python language."
"""
from typing import Any

from pydantic import Field, model_validator, PrivateAttr

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
    """

    # Private attribute
    _literals: set[Literal] = PrivateAttr(default_factory=set)
    # Public attributes
    is_powertype: bool = Field(default=False)
    order: str = Field(min_length=1, default="1")
    restricted_to: set[OntologicalNature] = Field(default_factory=set)
    stereotype: ClassStereotype = Field()

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

    def add_literal(self, new_literal: Literal) -> None:
        """Add a new literal to the class's collection of literals.

        This method ensures that only instances of Literal or its subclasses are added to the class. It also
        establishes a bidirectional relationship between the class and the literal.

        :param new_literal: The Literal to be added.
        :type new_literal: Literal
        :raises TypeError: If the provided new_literal is not an instance of Literal or if a class attempts to add itself.
        """
        if self.stereotype != ClassStereotype.ENUMERATION:
            raise TypeError(f"Literals can only be added to classes stereotyped with ClassStereotype.ENUMERATION")

        if new_literal == self:
            raise TypeError("A class cannot contain itself.")

        if not isinstance(new_literal, Literal):
            raise TypeError("New_Literal must be an instance of Literal.")

        self._literals.add(new_literal)  # direct relation
        new_literal._Literal__set_in_class(self)  # inverse relation

    def remove_literal(self, old_literal: Literal) -> None:
        """Remove an existing content from the class's collection of literals.

        This method ensures that the content to be removed is actually part of the class. It also updates the
        content's 'in_class' attribute to None, effectively breaking the bidirectional relationship.

        :param old_literal: The Literal content to be removed.
        :type old_literal: Literal
        :raises TypeError: If the content is not a valid Literal.
        :raises ValueError: If the content is not part of the class.
        """

        if self.stereotype != ClassStereotype.ENUMERATION:
            raise TypeError(f"Literals can only be removed from classes stereotyped with ClassStereotype.ENUMERATION")

        if not isinstance(old_literal, Literal):
            raise TypeError(f"Literal '{old_literal}' cannot be removed as it is not a valid Literal.")

        if old_literal in self._literals:
            self._literals.remove(old_literal)  # direct relation
            old_literal._Literal__set_in_class(None)  # inverse relation
        else:
            raise ValueError(f"Literal '{old_literal}' cannot be removed because is not part of the class.")

    @property
    def literals(self) -> set[Literal]:
        """Provide a read-only view of the class's literals.

        This property is a safeguard to prevent direct modification of the 'literals' set. To add or remove literals,
        use the 'add_literal' and 'remove_literal' methods. This design ensures that the integrity of the class's
        literals collection is maintained.

        :return: A set of Literal objects that are part of the class.
        :rtype: set[Literal]
        """
        return self._literals

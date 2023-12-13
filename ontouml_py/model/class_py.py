from typing import Any
from typing import Optional

from pydantic import Field

from ontouml_py.model.classifier import Classifier
from ontouml_py.model.enumerations.classstereotype import ClassStereotype
from ontouml_py.model.enumerations.ontologicalnature import OntologicalNature
from ontouml_py.model.literal import Literal
from ontouml_py.model.packageable import Packageable
from ontouml_py.model.projectelement import ProjectElement
from ontouml_py.utils.error_message import format_error_message


class Class(Classifier, ProjectElement, Packageable):
    is_powertype: bool = Field(default=False)
    order: str = Field(min_length=1, default="1")
    restricted_to: set[Optional[OntologicalNature]] = Field(default_factory=set)
    stereotype: Optional[ClassStereotype] = Field(default=None)
    literals: set[Optional[Literal]] = Field(default_factory=set)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        Classifier.__init__(self, **data)
        ProjectElement.__init__(self, project=project, pe_type=self.__class__.__name__)

    def add_literal(self, literal: Literal) -> None:
        """Add a literal to the class.

        :param literal: The literal to be added.
        :type literal: Literal
        :raises ValueError: If the provided object is not of type Literal.
        """
        if not isinstance(literal, Literal):
            error_message = format_error_message(
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
                description=f"Literal not found in Class with ID {self.id}.",
                cause=f"The literal {literal} to be removed does not exist in the class. "
                f"Existing ones are {self.literals}.",
                solution="Ensure the literal exists in the class before attempting to remove it.",
            )
            raise ValueError(error_message)
        self.literals.remove(literal)

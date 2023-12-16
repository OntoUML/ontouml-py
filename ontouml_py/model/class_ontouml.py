from typing import Any
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import PrivateAttr

from ontouml_py.model.classifier import Classifier
from ontouml_py.model.enumerations.classstereotype import ClassStereotype
from ontouml_py.model.enumerations.ontologicalnature import OntologicalNature
from ontouml_py.model.literal import Literal
from ontouml_py.utils.error_message import format_error_message


class Class(Classifier):
    _literals: set[Literal] = PrivateAttr(default_factory=set)
    is_powertype: bool = Field(default=False)
    order: Union[str, int] = Field(default=1)
    restricted_to: set[OntologicalNature] = Field(default_factory=set)
    stereotype: Optional[Union[ClassStereotype, str]] = Field(default=None)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: "Project", **data: dict[str, Any]) -> None:
        super().__init__(project=project, pe_type=self.__class__.__name__, **data)

    def create_literal(self) -> Literal:
        """Add a literal to the class."""
        new_literal = Literal(enumeration=self)
        self._literals.add(new_literal)
        return new_literal

    def delete_literal(self, old_literal: Literal) -> None:
        """Remove a literal from the class if it exists.

        :param old_literal: The literal to be removed.
        :type old_literal: Literal
        """
        if old_literal not in self._literals:
            error_message = format_error_message(
                description=f"Literal not found in Class with ID {self.id}.",
                cause=f"The literal {old_literal} to be removed does not exist in the class. "
                f"Existing ones are {self._literals}.",
                solution="Ensure the literal exists in the class before attempting to remove it.",
            )
            raise ValueError(error_message)
        self._literals.remove(old_literal)
        del old_literal

    @property
    def literals(self):
        return self._literals

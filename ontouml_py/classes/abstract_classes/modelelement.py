from abc import abstractmethod
from typing import Any, Optional

from pydantic import Field

from ontouml_py.classes.abstract_classes.namedelement import NamedElement
from ontouml_py.classes.abstract_classes.projectelement import ProjectElement
from ontouml_py.utils import validate_subclasses


class ModelElement(ProjectElement, NamedElement):
    custom_properties: set[tuple[str, Any]] = Field(default_factory=set)
    contained_in: Optional["Package"] = Field(default=None)  # Forward declaration of 'Package'

    # Pydantic's configuration settings for the NamedElement class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """
        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        _allowed_subclasses = [
            "Decoratable",
            "Generalization",
            "GeneralizationSet",
            "Link",
            "Literal",
            "Note",
            "Package",
        ]
        validate_subclasses(self, _allowed_subclasses)

        super().__init__(**data)

"""This module defines the ModelElement class, which represents a model element in an OntoUML model. It inherits \
properties from both NamedElement and ProjectElement, and includes additional features specific to model elements."""

from abc import abstractmethod
from typing import Any

from pydantic import Field

from ontouml_py.classes.abstract_classes.namedelement import NamedElement
from ontouml_py.classes.abstract_classes.projectelement import ProjectElement


class ModelElement(NamedElement, ProjectElement):
    """Represents a model element, inheriting properties from both NamedElement and ProjectElement.

    :ivar custom_properties: A set of custom properties associated with the model element. Each property is a tuple
        containing a string key and a value of any type.
    :vartype custom_properties: Set[Tuple[str, Any]]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    custom_properties: set[tuple[str, Any]] = Field(default_factory=set)

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new ModelElement instance.

        :param data: Fields to be set on the model instance. This includes fields inherited from NamedElement and
            ProjectElement, as well as any additional fields specific to ModelElement.
        :type data: Dict[str, Any]
        :raises ValueError: If the instance does not belong to the allowed subclasses.
        """
        self._validate_subclasses(
            [
                "Decoratable",
                "Generalization",
                "GeneralizationSet",
                "Anchor",
                "Literal",
                "Note",
                "Package",
                "Packageable",
            ],
        )
        super().__init__(**data)

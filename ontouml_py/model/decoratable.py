"""Module for the Decoratable class within an OntoUML model.

This module defines the Decoratable class, an abstract class that represents elements in an OntoUML model that can be
decorated with additional properties. It extends the ModelElement class and includes a boolean attribute to indicate
whether the element is derived. The class is designed to be subclassed by specific types of model elements that can
be decorated, such as classifiers and properties.
"""
from abc import abstractmethod
from typing import Any

from pydantic import Field

from ontouml_py.model.modelelement import ModelElement


class Decoratable(ModelElement):
    is_derived: bool = Field(default=False)

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, project: object, pe_type: str, **data: dict[str, Any]) -> None:
        super().__init__(project=project, pe_type=pe_type, **data)

from abc import abstractmethod
from typing import Any, NewType

from pydantic import Field

from src.classes.abstract_syntax.abstract_classes.namedelement import NamedElement

# Workaround necessary for the forward declaration of Project class.
Package = NewType("Package", object)  # Define a new type named 'Package' based on 'object'


class ModelElement(NamedElement):
    # TODO (@pedropaulofb): Check how to implement this default_factory.
    #  Contained_in can relate a NamedElement to a Package or it may be empty.
    contained_in: Package = Field(default_factory=object)  # Forward declaration of Project # noqa (Vulture)

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """
        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)

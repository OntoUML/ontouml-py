"""Module for the Package class within an OntoUML model.

This module defines the Package class, a concrete implementation of the Packageable abstract class. The Package class
represents a container in the OntoUML model, capable of holding other Packageable elements (here called contents).
It provides functionalities to add and remove contents, ensuring type safety and maintaining the integrity of the
model's structure. The class also includes private attributes to manage its contents and configuration settings for
validation and assignment.
"""
from typing import Any
from typing import Optional

from pydantic import PrivateAttr

from ontouml_py.model.modelelement import ModelElement
from ontouml_py.model.package_methods import PackageMethodsMixin
from ontouml_py.model.packageable import Packageable
from ontouml_py.model.projectelement import ProjectElement
from ontouml_py.utils.error_message import format_error_message


class Package(ModelElement, ProjectElement, Packageable, PackageMethodsMixin):
    # Private attribute
    _contents: dict[str, set[Packageable]] = PrivateAttr(
        default={
            "Anchor": set(),
            "BinaryRelation": set(),
            "Class": set(),
            "Generalization": set(),
            "GeneralizationSet": set(),
            "NaryRelation": set(),
            "Note": set(),
            "Package": set(),
        }
    )

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, **data: dict[str, Any]) -> None:
        ModelElement.__init__(self, **data)
        ProjectElement.__init__(self, project=project, pe_type=self.__class__.__name__)

    def get_contents(self) -> dict:
        return self._contents

    def get_content_by_id(self, content_type: str, content_id: Packageable) -> Optional[Packageable]:
        for internal_content in self._contents[content_type]:
            if internal_content.id == content_id:
                return internal_content
        return None

    def remove_content(self, old_content: Packageable) -> None:
        old_content_type = str(type(old_content))
        if old_content not in self._contents[old_content_type]:
            raise ValueError(self._removal_error_message(old_content, old_content_type))
        self._contents[old_content_type].remove(old_content)

    def _removal_error_message(self, old_content: Packageable, old_content_type: str) -> str:
        error_message = format_error_message(
            description=f"Invalid {old_content_type} content for removal.",
            cause=f"The content {old_content} is not found in the {old_content_type} contents of the package with ID {self.id}.",
            solution=f"Ensure the content to be removed is a valid {old_content_type} content in the package.",
        )
        return error_message

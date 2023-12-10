"""Module for the Package class within an OntoUML model.

This module defines the Package class, a concrete implementation of the Packageable abstract class. The Package class
represents a container in the OntoUML model, capable of holding other Packageable elements (here called contents).
It provides functionalities to add and remove contents, ensuring type safety and maintaining the integrity of the
model's structure. The class also includes private attributes to manage its contents and configuration settings for
validation and assignment.
"""
from typing import Any

from icecream import ic
from pydantic import PrivateAttr

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.class_py import Class
from ontouml_py.model.generalization import Generalization
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.packageable import Packageable
from ontouml_py.utils.error_message import format_error_message


class Package(Packageable):
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

    def __init__(self, project, **data: dict[str, Any]) -> None:
        super().__init__(project, **data)
        project._elements["Package"].add(self)

    def get_contents(self) -> dict:
        return self._contents

    def get_anchors(self) -> set[str]:
        return self._contents["Anchor"]

    def get_binary_relations(self) -> set[str]:
        return self._contents["BinaryRelation"]

    def get_classes(self) -> set[str]:
        return self._contents["Class"]

    def get_generalizations(self) -> set[str]:
        return self._contents["Generalization"]

    def get_generalization_sets(self) -> set[str]:
        return self._contents["GeneralizationSet"]

    def get_nary_relations(self) -> set[str]:
        return self._contents["NaryRelation"]

    def get_notes(self) -> set[str]:
        return self._contents["Note"]

    def get_packages(self) -> set[str]:
        return self._contents["Package"]

    def get_content_by_id(self, content_type: str, content_id: str):
        for internal_content in self._contents[content_type]:
            if internal_content.id == content_id:
                return internal_content

    def get_anchor_by_id(self, content_id: str):
        return self.get_content_by_id("Anchor", content_id)

    def get_binary_relation_by_id(self, content_id: str):
        return self.get_content_by_id("BinaryRelation", content_id)

    def get_class_by_id(self, content_id: str):
        return self.get_content_by_id("Class", content_id)

    def get_generalization_by_id(self, content_id: str):
        return self.get_content_by_id("Generalization", content_id)

    def get_generalization_set_by_id(self, content_id: str):
        return self.get_content_by_id("GeneralizationSet", content_id)

    def get_nary_relation_by_id(self, content_id: str):
        return self.get_content_by_id("NaryRelation", content_id)

    def get_note_by_id(self, content_id: str):
        return self.get_content_by_id("Note", content_id)

    def get_package_by_id(self, content_id: str):
        return self.get_content_by_id("Package", content_id)

    def add_anchor(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["Anchor"].add(new_content)

    def add_binary_relation(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["BinaryRelation"].add(new_content)

    def add_class(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["Class"].add(new_content)

    def add_generalization(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["Generalization"].add(new_content)

    def add_generalization_set(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["GeneralizationSet"].add(new_content)

    def add_nary_relation(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["NaryRelation"].add(new_content)

    def add_note(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["Note"].add(new_content)

    def add_package(self, new_content):
        new_content.__Packageable__set_package(self)
        self._contents["Package"].add(new_content)

    def remove_content(self, old_content:Packageable)->None:
        old_content_type = type(old_content)
        if old_content not in self._contents[old_content_type]:
            raise ValueError("Removal by id error")
        self._contents[old_content_type].remove(old_content)

    def remove_anchor(self, old_content: Anchor) -> None:
        if old_content not in self._contents["Anchor"]:
            raise ValueError(self.__removal_error_message(old_content, "Anchor"))
        self._contents["Anchor"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def remove_binary_relation(self, old_content: BinaryRelation) -> None:
        if old_content not in self._contents["BinaryRelation"]:
            raise ValueError(self.__removal_error_message(old_content, "BinaryRelation"))
        self._contents["BinaryRelation"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def remove_class(self, old_content: Class) -> None:
        if old_content not in self._contents["Class"]:
            raise ValueError(self.__removal_error_message(old_content, "Class"))
        self._contents["Class"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def remove_generalization(self, old_content: Generalization) -> None:
        if old_content not in self._contents["Generalization"]:
            raise ValueError(self.__removal_error_message(old_content, "Generalization"))
        self._contents["Generalization"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def remove_generalization_set(self, old_content: GeneralizationSet) -> None:
        if old_content not in self._contents["GeneralizationSet"]:
            raise ValueError(self.__removal_error_message(old_content, "GeneralizationSet"))
        self._contents["GeneralizationSet"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def remove_nary_relation(self, old_content: NaryRelation) -> None:
        if old_content not in self._contents["NaryRelation"]:
            raise ValueError(self.__removal_error_message(old_content, "NaryRelation"))
        self._contents["NaryRelation"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def remove_note(self, old_content: Note) -> None:
        if old_content not in self._contents["Note"]:
            raise ValueError(self.__removal_error_message(old_content, "Note"))
        self._contents["Note"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def remove_package(self, old_content) -> None:
        if old_content not in self._contents["Package"]:
            raise ValueError(self.__removal_error_message(old_content, "Package"))
        self._contents["Package"].remove(old_content)
        old_content.__Packageable__set_package(None)

    def __removal_error_message(self, old_content: Packageable, old_content_type: str) -> str:
        error_message = format_error_message(
            description=f"Invalid {old_content_type} content for removal.",
            cause=f"The content {old_content} is not found in the {old_content_type} contents of the package with ID {self.id}.",
            solution=f"Ensure the content to be removed is a valid {old_content_type} content in the package.",
        )
        return error_message

from typing import Optional

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.class_ontouml import Class
from ontouml_py.model.generalization import Generalization
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.packageable import Packageable


class PackageMethodsMixin:
    def __init__(self, *args, **kwargs):
        if type(self) is PackageMethodsMixin:
            raise TypeError(f"{type(self).__name__} is an abstract class and cannot be directly instantiated.")

    def get_anchors(self) -> set[Packageable]:
        return self._contents["Anchor"]

    def get_binary_relations(self) -> set[Packageable]:
        return self._contents["BinaryRelation"]

    def get_classes(self) -> set[Packageable]:
        return self._contents["Class"]

    def get_generalizations(self) -> set[Packageable]:
        return self._contents["Generalization"]

    def get_generalization_sets(self) -> set[Packageable]:
        return self._contents["GeneralizationSet"]

    def get_nary_relations(self) -> set[Packageable]:
        return self._contents["NaryRelation"]

    def get_notes(self) -> set[Packageable]:
        return self._contents["Note"]

    def get_packages(self) -> set[Packageable]:
        return self._contents["Package"]

    def get_anchor_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("Anchor", content_id)

    def get_binary_relation_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("BinaryRelation", content_id)

    def get_class_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("Class", content_id)

    def get_generalization_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("Generalization", content_id)

    def get_generalization_set_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("GeneralizationSet", content_id)

    def get_nary_relation_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("NaryRelation", content_id)

    def get_note_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("Note", content_id)

    def get_package_by_id(self, content_id: Packageable) -> Optional[Packageable]:
        return self.get_content_by_id("Package", content_id)

    def add_anchor(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["Anchor"].add(new_content)

    def add_binary_relation(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["BinaryRelation"].add(new_content)

    def add_class(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["Class"].add(new_content)

    def add_generalization(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["Generalization"].add(new_content)

    def add_generalization_set(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["GeneralizationSet"].add(new_content)

    def add_nary_relation(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["NaryRelation"].add(new_content)

    def add_note(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["Note"].add(new_content)

    def add_package(self, new_content: Packageable) -> None:
        new_content.__Packageable__set_package(self)
        self._contents["Package"].add(new_content)

        def remove_anchor(self, old_content: Anchor) -> None:
            if old_content not in self._contents["Anchor"]:
                raise ValueError(self._removal_error_message(old_content, "Anchor"))
            self._contents["Anchor"].remove(old_content)
            old_content.__Packageable__set_package(None)

        def remove_binary_relation(self, old_content: BinaryRelation) -> None:
            if old_content not in self._contents["BinaryRelation"]:
                raise ValueError(self._removal_error_message(old_content, "BinaryRelation"))
            self._contents["BinaryRelation"].remove(old_content)
            old_content.__Packageable__set_package(None)

        def remove_class(self, old_content: Class) -> None:
            if old_content not in self._contents["Class"]:
                raise ValueError(self._removal_error_message(old_content, "Class"))
            self._contents["Class"].remove(old_content)
            old_content.__Packageable__set_package(None)

        def remove_generalization(self, old_content: Generalization) -> None:
            if old_content not in self._contents["Generalization"]:
                raise ValueError(self._removal_error_message(old_content, "Generalization"))
            self._contents["Generalization"].remove(old_content)
            old_content.__Packageable__set_package(None)

        def remove_generalization_set(self, old_content: GeneralizationSet) -> None:
            if old_content not in self._contents["GeneralizationSet"]:
                raise ValueError(self._removal_error_message(old_content, "GeneralizationSet"))
            self._contents["GeneralizationSet"].remove(old_content)
            old_content.__Packageable__set_package(None)

        def remove_nary_relation(self, old_content: NaryRelation) -> None:
            if old_content not in self._contents["NaryRelation"]:
                raise ValueError(self._removal_error_message(old_content, "NaryRelation"))
            self._contents["NaryRelation"].remove(old_content)
            old_content.__Packageable__set_package(None)

        def remove_note(self, old_content: Note) -> None:
            if old_content not in self._contents["Note"]:
                raise ValueError(self._removal_error_message(old_content, "Note"))
            self._contents["Note"].remove(old_content)
            old_content.__Packageable__set_package(None)

        def remove_package(self, old_content) -> None:
            if old_content not in self._contents["Package"]:
                raise ValueError(self._removal_error_message(old_content, "Package"))
            self._contents["Package"].remove(old_content)
            old_content.__Packageable__set_package(None)

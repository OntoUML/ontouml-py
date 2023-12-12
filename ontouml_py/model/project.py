from dataclasses import dataclass, field
from typing import Any
from typing import Optional

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.class_py import Class
from ontouml_py.model.enumerations.classstereotype import ClassStereotype
from ontouml_py.model.enumerations.ontologicalnature import OntologicalNature
from ontouml_py.model.enumerations.ontologyrepresentationstyle import OntologyRepresentationStyle
from ontouml_py.model.generalization import Generalization
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.namedelement import NamedElement
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.package import Package
from ontouml_py.model.projectelement import ProjectElement
from ontouml_py.representation.diagram import Diagram


@dataclass
class Project(NamedElement):
    # Private attribute (converted from PrivateAttr)
    _elements: dict[str, set[ProjectElement]] = field(default_factory=lambda: {
        "Anchor": set(),
        "BinaryRelation": set(),
        "Class": set(),
        "Diagram": set(),
        "Generalization": set(),
        "GeneralizationSet": set(),
        "Literal": set(),
        "NaryRelation": set(),
        "Note": set(),
        "Package": set(),
        "Property": set(),
        "Shape": set(),
        "View": set(),
    }, init=False)

    # Public attributes
    acronyms: set[str] = field(default_factory=set)
    bibliographic_citations: set[str] = field(default_factory=set)
    keywords: set[str] = field(default_factory=set)
    landing_pages: set[str] = field(default_factory=set)
    languages: set[str] = field(default_factory=set)
    namespace: Optional[str] = None
    sources: set[str] = field(default_factory=set)
    access_rights: set[str] = field(default_factory=set)
    ontology_types: set[str] = field(default_factory=set)
    themes: set[str] = field(default_factory=set)
    license: Optional[str] = None
    contexts: set[str] = field(default_factory=set)
    designed_for_task: set[str] = field(default_factory=set)
    publisher: Optional[str] = None
    root_package: Optional[Package] = None
    representation_style: OntologyRepresentationStyle = OntologyRepresentationStyle.ONTOUML_STYLE


    def get_elements(self) -> dict:
        return self._elements

    def get_anchors(self) -> set[ProjectElement]:
        return self._elements["Anchor"]

    def get_binary_relations(self) -> set[ProjectElement]:
        return self._elements["BinaryRelation"]

    def get_classes(self) -> set[ProjectElement]:
        return self._elements["Class"]

    def get_diagrams(self) -> set[ProjectElement]:
        return self._elements["Diagram"]

    def get_generalizations(self) -> set[ProjectElement]:
        return self._elements["Generalization"]

    def get_generalization_sets(self) -> set[ProjectElement]:
        return self._elements["GeneralizationSet"]

    def get_literals(self) -> set[ProjectElement]:
        return self._elements["Literal"]

    def get_nary_relations(self) -> set[ProjectElement]:
        return self._elements["NaryRelation"]

    def get_notes(self) -> set[ProjectElement]:
        return self._elements["Note"]

    def get_packages(self) -> set[ProjectElement]:
        return self._elements["Package"]

    def get_properties(self) -> set[ProjectElement]:
        return self._elements["Property"]

    def get_shapes(self) -> set[ProjectElement]:
        return self._elements["Shape"]

    def get_views(self) -> set[ProjectElement]:
        return self._elements["View"]

    def get_element_by_id(self, element_type: str, element_id: str):
        for internal_element in self._elements[element_type]:
            if internal_element.id == element_id:
                return internal_element

    def get_anchor_by_id(self, element_id: str):
        return self.get_element_by_id("Anchor", element_id)

    def get_binary_relation_by_id(self, element_id: str):
        return self.get_element_by_id("BinaryRelation", element_id)

    def get_class_by_id(self, element_id: str):
        return self.get_element_by_id("Class", element_id)

    def get_diagram_by_id(self, element_id: str):
        return self.get_element_by_id("Diagram", element_id)

    def get_generalization_by_id(self, element_id: str):
        return self.get_element_by_id("Generalization", element_id)

    def get_generalization_set_by_id(self, element_id: str):
        return self.get_element_by_id("GeneralizationSet", element_id)

    def get_literal_by_id(self, element_id: str):
        return self.get_element_by_id("Literal", element_id)

    def get_nary_relation_by_id(self, element_id: str):
        return self.get_element_by_id("NaryRelation", element_id)

    def get_note_by_id(self, element_id: str):
        return self.get_element_by_id("Note", element_id)

    def get_package_by_id(self, element_id: str):
        return self.get_element_by_id("Package", element_id)

    def get_property_by_id(self, element_id: str):
        return self.get_element_by_id("Property", element_id)

    def get_shape_by_id(self, element_id: str):
        return self.get_element_by_id("Shape", element_id)

    def get_view_by_id(self, element_id: str):
        return self.get_element_by_id("View", element_id)

    ### ELEMENTS' CREATION CREATION METHODS

    def create_anchor(self, **data: dict[str, Any]) -> Anchor:
        new_element = Anchor(self, **data)
        self._elements["Anchor"].add(new_element)
        return new_element

    def create_binary_relation(self, **data: dict[str, Any]) -> BinaryRelation:
        new_element = BinaryRelation(self, **data)
        self._elements["BinaryRelation"].add(new_element)
        return new_element

    def create_class(
        self,
        stereotype: Optional[ClassStereotype] = None,
        order: int = 1,
        restricted_to: Optional[set[Optional[OntologicalNature]]] = None,
        is_abstract: bool = False,
        **data: dict[str, Any],
    ) -> Class:
        if restricted_to is None:
            restricted_to = set()

        new_element = Class(
            self, stereotype=stereotype, order=order, restricted_to=restricted_to, is_abstract=is_abstract, **data
        )
        self._elements["Class"].add(new_element)
        return new_element

    def create_diagram(self, **data: dict[str, Any]) -> Diagram:
        new_element = Diagram(self, **data)
        self._elements["Diagram"].add(new_element)
        return new_element

    def create_generalization(self, **data: dict[str, Any]) -> Generalization:
        new_element = Generalization(self, **data)
        self._elements["Generalization"].add(new_element)
        return new_element

    def create_generalization_set(self, **data: dict[str, Any]) -> GeneralizationSet:
        new_element = GeneralizationSet(self, **data)
        self._elements["GeneralizationSet"].add(new_element)
        return new_element

    def create_nary_relation(self, **data: dict[str, Any]) -> NaryRelation:
        new_element = NaryRelation(self, **data)
        self._elements["NaryRelation"].add(new_element)
        return new_element

    def create_note(self, **data: dict[str, Any]) -> Note:
        new_element = Note(self, **data)
        self._elements["Note"].add(new_element)
        return new_element

    def create_package(self, **data: dict[str, Any]) -> Package:
        new_element = Package(self, **data)
        self._elements["Package"].add(new_element)
        return new_element

    ### CLASSES'S CREATION METHODS

    def create_class_abstract(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.ABSTRACT
        order = 1
        restricted_to = {OntologicalNature.ABSTRACT_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_category(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.CATEGORY
        restricted_to = {OntologicalNature.FUNCTIONAL_COMPLEX_NATURE}
        is_abstract = True
        return self.create_class(stereotype=stereotype, restricted_to=restricted_to, is_abstract=is_abstract, **data)

    def create_class_collective(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.COLLECTIVE
        order = 1
        restricted_to = {OntologicalNature.COLLECTIVE_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_datatype(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.DATATYPE
        order = 1
        restricted_to = {OntologicalNature.ABSTRACT_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_enumeration(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.ENUMERATION
        order = 1
        restricted_to = {OntologicalNature.ABSTRACT_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_event(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.EVENT
        order = 1
        restricted_to = {OntologicalNature.EVENT_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_historical_role(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.HISTORICAL_ROLE
        return self.create_class(stereotype=stereotype, **data)

    def create_class_historical_role_mixin(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.HISTORICAL_ROLE_MIXIN
        restricted_to = {OntologicalNature.FUNCTIONAL_COMPLEX_NATURE}
        is_abstract = True
        return self.create_class(stereotype=stereotype, restricted_to=restricted_to, is_abstract=is_abstract, **data)

    def create_class_kind(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.KIND
        order = 1
        restricted_to = {OntologicalNature.FUNCTIONAL_COMPLEX_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_mixin(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.MIXIN
        restricted_to = {OntologicalNature.FUNCTIONAL_COMPLEX_NATURE}
        is_abstract = True
        return self.create_class(stereotype=stereotype, restricted_to=restricted_to, is_abstract=is_abstract, **data)

    def create_class_mode(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.MODE
        order = 1
        restricted_to = {OntologicalNature.INTRINSIC_MODE_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_phase(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.PHASE
        return self.create_class(stereotype=stereotype, **data)

    def create_class_phase_mixin(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.PHASE_MIXIN
        restricted_to = {OntologicalNature.FUNCTIONAL_COMPLEX_NATURE}
        is_abstract = True
        return self.create_class(stereotype=stereotype, restricted_to=restricted_to, is_abstract=is_abstract, **data)

    def create_class_quality(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.QUALITY
        order = 1
        restricted_to = {OntologicalNature.QUALITY_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_quantity(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.QUANTITY
        order = 1
        restricted_to = {OntologicalNature.QUANTITY_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_relator(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.RELATOR
        order = 1
        restricted_to = {OntologicalNature.RELATOR_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_role(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.ROLE
        return self.create_class(stereotype=stereotype, **data)

    def create_class_role_mixin(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.ROLE_MIXIN
        restricted_to = {OntologicalNature.FUNCTIONAL_COMPLEX_NATURE}
        return self.create_class(stereotype=stereotype, restricted_to=restricted_to, **data)

    def create_class_situation(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.SITUATION
        order = 1
        restricted_to = {OntologicalNature.SITUATION_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

    def create_class_subkind(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.SUBKIND
        return self.create_class(stereotype=stereotype, **data)

    def create_class_type(self, **data: dict[str, Any]) -> Class:
        stereotype = ClassStereotype.TYPE
        order = 2
        restricted_to = {OntologicalNature.TYPE_NATURE}
        return self.create_class(stereotype=stereotype, order=order, restricted_to=restricted_to, **data)

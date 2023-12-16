from typing import Any
from typing import Optional

from pydantic import Field
from pydantic import PrivateAttr

from ontouml_py.model.enumerations.ontologyrepresentationstyle import OntologyRepresentationStyle
from ontouml_py.model.namedelement import NamedElement
from ontouml_py.model.package import Package
from ontouml_py.model.project_methods import ProjectMethodsMixin
from ontouml_py.model.projectelement import ProjectElement


class Project(NamedElement, ProjectMethodsMixin):
    # Private attributes
    # Dictionary that contains, for each ProjectElement concrete class, a set of the elements inside the project
    _elements: dict[str, set[ProjectElement]] = PrivateAttr(
        default={
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
        }
    )

    # Public attributes
    acronyms: set[str] = Field(default_factory=set)
    bibliographic_citations: set[str] = Field(default_factory=set)
    keywords: set[str] = Field(default_factory=set)
    landing_pages: set[str] = Field(default_factory=set)
    languages: set[str] = Field(default_factory=set)
    namespace: Optional[str] = Field(default=None)
    sources: set[str] = Field(default_factory=set)
    access_rights: set[str] = Field(default_factory=set)
    ontology_types: set[str] = Field(default_factory=set)
    themes: set[str] = Field(default_factory=set)
    license: Optional[str] = Field(default=None)
    contexts: set[str] = Field(default_factory=set)
    designed_for_task: set[str] = Field(default_factory=set)
    publisher: Optional[str] = Field(default=None)
    rOt_package: Optional[Package] = Field(default=None)
    representation_style: OntologyRepresentationStyle = Field(default=OntologyRepresentationStyle.ONTOUML_STYLE)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        NamedElement.__init__(self, **data)

    def get_elements(self) -> dict[str, set[ProjectElement]]:
        return self._elements

    def get_element_by_id(self, element_type: str, element_id: str) -> Optional[ProjectElement]:
        for internal_element in self._elements[element_type]:
            if internal_element.id == element_id:
                return internal_element
        return None

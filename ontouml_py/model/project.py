from typing import Any
from typing import Optional

from pydantic import Field
from pydantic import PrivateAttr

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.class_py import Class
from ontouml_py.model.enumerations.ontologyrepresentationstyle import OntologyRepresentationStyle
from ontouml_py.model.generalization import Generalization
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.namedelement import NamedElement
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.package import Package
from ontouml_py.model.projectelement import ProjectElement
from ontouml_py.representation.diagram import Diagram
from ontouml_py.utils.error_message import format_error_message


class Project(NamedElement):
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
            "Shape": set(),
            "View": set(),
        }
    )

    # Public attributes
    acronyms: set[str] = Field(default_factory=set)
    bibliographic_citations: set[str] = Field(default_factory=set)
    keywords: set[str] = Field(default_factory=set)
    landing_pages: set[str] = Field(default_factory=set)
    languages: set[str] = Field(default_factory=set)
    namespace: Optional[str] = Field(min_length=1, default=None)
    sources: set[str] = Field(default_factory=set)
    access_rights: set[str] = Field(default_factory=set)
    ontology_types: set[str] = Field(default_factory=set)
    themes: set[str] = Field(default_factory=set)
    license: Optional[str] = Field(min_length=1, default=None)
    contexts: set[str] = Field(default_factory=set)
    designed_for_task: set[str] = Field(default_factory=set)
    publisher: Optional[str] = Field(min_length=1, default=None)
    root_package: Optional[Package] = Field(default=None)
    representation_style: OntologyRepresentationStyle = Field(default=OntologyRepresentationStyle.ONTOUML_STYLE)

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)

        if "root_package" in data:
            self.__validate_root_package(data.get("root_package"))

    def __setattr__(self, key: str, value: Any) -> None:
        """Override the default attribute setting behavior to include validation for 'root_package'.

        This method intercepts the setting of the 'root_package' attribute to ensure that the assigned package is
        a part of the project's elements. If the validation fails, a ValueError is raised.

        :param key: The name of the attribute to be set.
        :type key: str
        :param value: The value to be assigned to the attribute.
        :type value: Any
        :raises ValueError: If 'root_package' is set to a package not in the project's elements.
        """
        if key == "root_package":
            self.__validate_root_package(value)
        super().__setattr__(key, value)

    def __validate_root_package(self, package: Optional[Package]) -> None:
        """Validate if the provided package is a valid root package for the project.

        This method performs two checks:
        1. It verifies that the provided package is of the correct type (Package).
        2. It checks if the specified package is included in the project's elements set, ensuring it is a valid and
        integral part of the project's structure.

        :param package: The package to be validated as the root package of the project.
        :type package: Optional[Package]
        :raises TypeError: If the provided object is not of type Package.
        :raises ValueError: If the package is not included in the project's elements or is not a valid Package instance.
        """
        if package and not isinstance(package, Package):
            error_message = format_error_message(
                error_type="TypeError.",
                description=f"Invalid root_package type received for Project with ID {self.id}.",
                cause=f"The received root_package is not a Package, but a {type(package).__name__}.",
                solution="Ensure the root_package is of type Package.",
            )
            raise TypeError(error_message)

        if package is not None and package not in self._elements:
            error_message = format_error_message(
                error_type="ValueError.",
                description="Invalid root package for Project.",
                cause=f"The root_package {package.id} is not an element of the project with ID {self.id}.",
                solution="Ensure the root_package is included in the project's elements.",
            )
            raise ValueError(error_message)

    def get_elements(self) -> dict:
        return self._elements

    def get_anchors(self) -> set[str]:
        return self._elements["Anchor"]

    def get_binary_relations(self) -> set[str]:
        return self._elements["BinaryRelation"]

    def get_classes(self) -> set[str]:
        return self._elements["Class"]

    def get_diagrams(self) -> set[str]:
        return self._elements["Diagram"]

    def get_generalizations(self) -> set[str]:
        return self._elements["Generalization"]

    def get_generalization_sets(self) -> set[str]:
        return self._elements["GeneralizationSet"]

    def get_literals(self) -> set[str]:
        return self._elements["Literal"]

    def get_nary_relations(self) -> set[str]:
        return self._elements["NaryRelation"]

    def get_notes(self) -> set[str]:
        return self._elements["Note"]

    def get_packages(self) -> set[str]:
        return self._elements["Package"]

    def get_propertys(self) -> set[str]:
        return self._elements["Property"]

    def get_shapes(self) -> set[str]:
        return self._elements["Shape"]

    def get_views(self) -> set[str]:
        return self._elements["View"]

    def create_anchor(self):
        new_element = Anchor(self)
        self._elements["Anchor"].add(new_element)

    def create_binary_relation(self):
        new_element = BinaryRelation(self)
        self._elements["BinaryRelation"].add(new_element)
        return new_element

    def create_class(self):
        new_element = Class(self)
        self._elements["Class"].add(new_element)
        return new_element

    def create_diagram(self, **data: dict[str, Any]):
        new_element = Diagram(self, **data)
        self._elements["Diagram"].add(new_element)
        return new_element

    def create_generalization(self):
        new_element = Generalization(self)
        self._elements["Generalization"].add(new_element)
        return new_element

    def create_generalization_set(self):
        new_element = GeneralizationSet(self)
        self._elements["GeneralizationSet"].add(new_element)
        return new_element

    def create_nary_relation(self):
        new_element = NaryRelation(self)
        self._elements["NaryRelation"].add(new_element)
        return new_element

    def create_note(self):
        new_element = Note(self)
        self._elements["Note"].add(new_element)
        return new_element

    def create_package(self):
        new_element = Package(self)
        self._elements["Package"].add(new_element)
        return new_element

    def delete_anchor(self, old_element: Anchor) -> None:
        if old_element not in self._elements["Anchor"]:
            raise ValueError(self.__deletion_error_message(old_element, "Anchor"))
        self._elements["Anchor"].remove(old_element)

    def delete_binary_relation(self, old_element: BinaryRelation) -> None:
        if old_element not in self._elements["BinaryRelation"]:
            raise ValueError(self.__deletion_error_message(old_element, "BinaryRelation"))
        self._elements["BinaryRelation"].remove(old_element)

    def delete_class(self, old_element: Class) -> None:
        if old_element not in self._elements["Class"]:
            raise ValueError(self.__deletion_error_message(old_element, "Class"))
        self._elements["Class"].remove(old_element)

    def delete_diagram(self, old_element: Diagram) -> None:
        if old_element not in self._elements["Diagram"]:
            raise ValueError(self.__deletion_error_message(old_element, "Diagram"))
        self._elements["Diagram"].remove(old_element)

    def delete_generalization(self, old_element: Generalization) -> None:
        if old_element not in self._elements["Generalization"]:
            raise ValueError(self.__deletion_error_message(old_element, "Generalization"))
        self._elements["Generalization"].remove(old_element)

    def delete_generalization_set(self, old_element: GeneralizationSet) -> None:
        if old_element not in self._elements["GeneralizationSet"]:
            raise ValueError(self.__deletion_error_message(old_element, "GeneralizationSet"))
        self._elements["GeneralizationSet"].remove(old_element)

    def delete_nary_relation(self, old_element: NaryRelation) -> None:
        if old_element not in self._elements["NaryRelation"]:
            raise ValueError(self.__deletion_error_message(old_element, "NaryRelation"))
        self._elements["NaryRelation"].remove(old_element)

    def delete_note(self, old_element: Note) -> None:
        if old_element not in self._elements["Note"]:
            raise ValueError(self.__deletion_error_message(old_element, "Note"))
        self._elements["Note"].remove(old_element)

    def delete_package(self, old_element: Package) -> None:
        if old_element not in self._elements["Package"]:
            raise ValueError(self.__deletion_error_message(old_element, "Package"))
        self._elements["Package"].remove(old_element)

    def __deletion_error_message(self, old_element: ProjectElement, old_element_type: str) -> str:
        error_message = format_error_message(
            description=f"Invalid {old_element_type} element for deletion.",
            cause=f"The element {old_element} is not found in the {old_element_type} elements of the project with ID {self.id}.",
            solution=f"Ensure the element to be deleted is a valid {old_element_type} element in the project.",
        )
        return error_message

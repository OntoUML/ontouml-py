"""Module for the Project class within an OntoUML model.

The Project class extends NamedElement to include project-specific details such as bibliographic citations, keywords,
and landing pages, among others, providing a comprehensive representation of a project's metadata.
"""

from typing import Any, Optional

from pydantic import Field, PrivateAttr, field_validator

from src.classes.abstract_classes.namedelement import NamedElement
from src.classes.abstract_classes.ontoumlelement import OntoumlElement
from src.classes.concrete_classes.package import Package
from src.classes.enumerations.ontologyrepresentationstyle import (
    OntologyRepresentationStyle,
)


class Project(NamedElement):
    """
    A concrete class representing an OntoUML Project, extending the NamedElement class.

    Manages project-related elements such as acronyms, bibliographic citations, keywords, landing pages, and more,
    providing a comprehensive representation of project metadata.

    The 'elements' attribute is implemented as a read-only property to maintain control over the list of elements and
    enforce the inverse relationship with OntoumlElement instances. The actual data is stored in the private attribute
    '_elements', which can be manipulated via add_element and remove_element methods.

    :ivar acronyms: List of acronyms associated with the project.
    :vartype acronyms: set[str]
    :ivar bibliographic_citations: Bibliographic citations related to the project.
    :vartype bibliographic_citations: set[str]
    :ivar keywords: Keywords describing the project.
    :vartype keywords: set[str]
    :ivar landing_pages: URLs to landing pages of the project.
    :vartype landing_pages: set[str]
    :ivar languages: Languages used in the project.
    :vartype languages: set[str]
    :ivar namespace: Namespace of the project. Optional.
    :vartype namespace: Optional[str]
    :ivar sources: Sources of information for the project.
    :vartype sources: set[str]
    :ivar access_rights: Information about access rights for the project.
    :vartype access_rights: set[str]
    :ivar ontology_types: Types of ontologies used in the project.
    :vartype ontology_types: set[str]
    :ivar themes: Themes associated with the project.
    :vartype themes: set[str]
    :ivar license: Licensing information of the project. Optional.
    :vartype license: Optional[str]
    :ivar contexts: Contexts for which the project is designed.
    :vartype contexts: set[str]
    :ivar designed_for_task: Tasks for which the project is designed.
    :vartype designed_for_task: set[str]
    :ivar publisher: Publisher of the project. Optional.
    :vartype publisher: Optional[str]
    :ivar root_package: Root package of the project. Optional.
    :vartype root_package: Optional[Package]
    :ivar representation_style: Style of ontology representation used in the project.
    :vartype representation_style: OntologyRepresentationStyle
    """

    # Private attributes
    _elements: set[OntoumlElement] = PrivateAttr(default_factory=set)
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

    # Configuration settings for the Project model using Pydantic.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @field_validator(
        "acronyms",
        "bibliographic_citations",
        "keywords",
        "landing_pages",
        "languages",
        "sources",
        "access_rights",
        "ontology_types",
        "themes",
        "contexts",
        "designed_for_task",
        mode="after",
    )
    @classmethod
    def ensure_non_empty(cls, checked_list: set[str]) -> set[str]:  # noqa (vulture)
        """
        Validates that the provided list does not contain empty strings.

        :param checked_list: The list to be validated.
        :type checked_list: set[str]
        :return: The validated list.
        :rtype: set[str]
        :raises ValueError: If any element in the list is an empty string.
        """
        for elem in checked_list:
            if elem == "":
                raise ValueError("Empty strings are not allowed")
        return checked_list

    def __init__(self, **data: dict[str, Any]) -> None:
        """
        Initialize a new Project instance.

        Inherits attributes from NamedElement and adds additional project-specific attributes.

        :param data: Fields to be set on the model instance.
        :type data: dict[str, Any]
        :raises TypeError: If 'elements' is provided and is not a list.
        """
        super().__init__(**data)
        elements = data.get("elements")
        if elements is not None and not isinstance(elements, set):
            raise TypeError("Expected 'elements' to be a set")
        self._elements: set[OntoumlElement] = elements if elements is not None else set()

    def add_element(self, element: OntoumlElement) -> None:
        """
        Add an OntoumlElement to the project.

        Ensures that the element is of the correct type and not a Project itself. Also updates the inverse relationship
        in OntoumlElement and checks for duplicates.

        :param element: The OntoumlElement to be added to the project.
        :type element: OntoumlElement
        :raises TypeError: If the element is not an instance of OntoumlElement.
        """
        if not isinstance(element, OntoumlElement):
            raise TypeError("Element must be an instance of OntoumlElement.")
        if not isinstance(element, Project):
            element.in_project.add(self)  # direct relation
            self._elements.add(element)  # inverse relation

    def remove_element(self, element: OntoumlElement) -> None:
        """
        Remove an OntoumlElement from the project if it exists.

        Also updates the inverse relationship in OntoumlElement.

        :param element: The OntoumlElement to be removed from the project.
        :type element: OntoumlElement
        :raises TypeError: If the element is not a valid OntoumlElement.
        """
        if not isinstance(element, OntoumlElement):
            raise TypeError(f"Element '{element}' cannot be removed as it is not a valid OntoumlElement.")

        if element in self._elements:
            self._elements.remove(element)
            if self in element.in_project:
                element.in_project.remove(self)

    @property
    def elements(self) -> set[OntoumlElement]:
        """
        Provide read-only access to the elements attribute.

        This is a workaround to prevent direct modification of the 'elements' list. Modifications should be done using
        add_element and remove_element methods.

        :return: A list of OntoumlElement objects.
        :rtype: set[OntoumlElement]
        """
        return self._elements

"""Module for the Project class within an OntoUML model.

The Project class extends NamedElement to include project-specific details such as bibliographic citations, keywords,
and landing pages, among others, providing a comprehensive representation of a project's metadata.
"""

from typing import Any, Optional

from langstring_lib.langstring import LangString  # type: ignore
from pydantic import Field, PrivateAttr

from ontouml_py.classes.abstract_syntax.abstract_classes.namedelement import (
    NamedElement,
)
from ontouml_py.classes.abstract_syntax.concrete_classes.package import Package
from ontouml_py.classes.ontoumlelement import OntoumlElement


class Project(NamedElement):
    """A concrete class representing an OntoUML Project, extending the NamedElement class.

    Manages project-related elements such as acronyms, bibliographic citations, keywords, landing pages, and more,
    providing a comprehensive representation of project metadata.

    The 'elements' attribute is implemented as a read-only property to maintain control over the list of elements and
    enforce the inverse relationship with OntoumlElement instances. The actual data is stored in the private attribute
    '_elements', which can be manipulated via add_element and remove_element methods.

    :ivar acronyms: List of acronyms associated with the project.
    :vartype acronyms: list[str]
    :ivar bibliographic_citations: Bibliographic citations related to the project.
    :vartype bibliographic_citations: list[str]
    :ivar keywords: Keywords describing the project.
    :vartype keywords: list[LangString]
    :ivar landing_pages: URLs to landing pages of the project.
    :vartype landing_pages: list[str]
    :ivar languages: Languages used in the project.
    :vartype languages: list[str]
    :ivar namespace: Namespace of the project. Optional.
    :vartype namespace: Optional[str]
    :ivar sources: Sources of information for the project.
    :vartype sources: list[str]
    :ivar access_rights: Information about access rights for the project.
    :vartype access_rights: list[str]
    :ivar ontology_types: Types of ontologies used in the project.
    :vartype ontology_types: list[str]
    :ivar themes: Themes associated with the project.
    :vartype themes: list[str]
    :ivar license: Licensing information of the project. Optional.
    :vartype license: Optional[str]
    :ivar contexts: Contexts for which the project is designed.
    :vartype contexts: list[str]
    :ivar designed_for_task: Tasks for which the project is designed.
    :vartype designed_for_task: list[str]
    :ivar publisher: Publisher of the project. Optional.
    :vartype publisher: Optional[str]
    """

    # Private attributes
    _elements: list[OntoumlElement] = PrivateAttr(default_factory=list)
    # Public attributes
    acronyms: list[str] = Field(default_factory=list)
    bibliographic_citations: list[str] = Field(default_factory=list)
    keywords: list[LangString] = Field(default_factory=list)
    landing_pages: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
    namespace: Optional[str] = None
    sources: list[str] = Field(default_factory=list)
    access_rights: list[str] = Field(default_factory=list)
    ontology_types: list[str] = Field(default_factory=list)
    themes: list[str] = Field(default_factory=list)
    license: Optional[str] = None
    contexts: list[str] = Field(default_factory=list)
    designed_for_task: list[str] = Field(default_factory=list)
    publisher: Optional[str] = None
    root_package: Optional[Package] = None
    # TODO (@pedropaulofb): Add representationStyle

    # Configuration settings for the Project model using Pydantic.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Project instance.

        Inherits attributes from NamedElement and adds additional project-specific attributes.

        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)
        elements = data.get("elements")
        if elements is not None and not isinstance(elements, list):
            raise TypeError("Expected 'elements' to be a list")
        self._elements: list[OntoumlElement] = elements if elements is not None else []

    def add_element(self, element: OntoumlElement) -> None:
        """Add an OntoumlElement to the project. Ensures that the element is of the correct type and not a Project \
        itself. Also updates the inverse relationship in OntoumlElement and checks for duplicates.

        :param element: The OntoumlElement to be added to the project.
        :type element: OntoumlElement
        :raises TypeError: If the element is not an instance of OntoumlElement.
        """
        if not isinstance(element, OntoumlElement):
            raise TypeError("Element must be an instance of OntoumlElement.")

        if not isinstance(element, Project) and element not in self._elements:
            self._elements.append(element)
            if self not in element.in_project:
                element.in_project.append(self)

    def remove_element(self, element: OntoumlElement) -> None:
        """Remove an OntoumlElement from the project if it exists. Also updates the inverse relationship in \
        OntoumlElement.

        :param element: The OntoumlElement to be removed from the project.
        :type element: OntoumlElement
        :raises TypeError: If the element is None.
        """
        if not isinstance(element, OntoumlElement):
            raise TypeError(f"Element '{element}' cannot be removed as it is not a valid OntoumlElement.")

        if element in self._elements:
            self._elements.remove(element)
            if self in element.in_project:
                element.in_project.remove(self)

    @property
    def elements(self) -> list[OntoumlElement]:
        """Provide read-only access to the elements attribute. This is a workaround to prevent direct modification of \
        the 'elements' list. Modifications should be done using add_element and remove_element methods.

        :return: A list of OntoumlElement objects.
        :rtype: list[OntoumlElement]
        """
        return self._elements

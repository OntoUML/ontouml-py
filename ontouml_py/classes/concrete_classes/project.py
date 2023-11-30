"""Module for the Project class within an OntoUML model.

The Project class extends NamedElement to include project-specific details such as bibliographic citations, keywords,
and landing pages, among others, providing a comprehensive representation of a project's metadata.
"""

from typing import Any, Optional

from pydantic import Field, PrivateAttr, field_validator

from ontouml_py.classes.abstract_classes.namedelement import NamedElement
from ontouml_py.classes.abstract_classes.projectelement import ProjectElement
from ontouml_py.classes.concrete_classes.package import Package
from ontouml_py.classes.enumerations.ontologyrepresentationstyle import (
    OntologyRepresentationStyle,
)


class Project(NamedElement):
    """Represent an OntoUML Project, extending NamedElement with additional project-specific metadata.

    This class encapsulates various aspects of a project, such as acronyms, bibliographic citations, keywords,
    landing pages, and more. It provides a structured way to represent and access these details. The 'elements'
    attribute, which holds the project elements, is managed through specific methods to ensure integrity and
    consistency of the project's structure.

    :ivar acronyms: A set of acronyms associated with the project, aiding in its identification and reference.
    :vartype acronyms: set[str]
    :ivar bibliographic_citations: A collection of bibliographic citations that reference/are relevant to the project
    :vartype bibliographic_citations: set[str]
    :ivar keywords: Descriptive keywords that encapsulate the essence and focus areas of the project.
    :vartype keywords: set[str]
    :ivar landing_pages: URLs pointing to web pages that provide an entry point or overview of the project.
    :vartype landing_pages: set[str]
    :ivar languages: The set of languages that are used or supported within the scope of the project.
    :vartype languages: set[str]
    :ivar namespace: An optional namespace that provides a unique context for the project's elements.
    :vartype namespace: Optional[str]
    :ivar sources: A set of sources or references that have contributed information to the project.
    :vartype sources: set[str]
    :ivar access_rights: Information detailing the access rights and restrictions associated with the project.
    :vartype access_rights: set[str]
    :ivar ontology_types: The types of ontologies that are utilized or represented in the project.
    :vartype ontology_types: set[str]
    :ivar themes: Themes or topics that are central or relevant to the project's objectives and content.
    :vartype themes: set[str]
    :ivar license: Optional licensing information, specifying the legal usage terms of the project's outputs.
    :vartype license: Optional[str]
    :ivar contexts: The contexts or environments for which the project is specifically designed.
    :vartype contexts: set[str]
    :ivar designed_for_task: A set of tasks or objectives that the project is intended to address or facilitate.
    :vartype designed_for_task: set[str]
    :ivar publisher: The entity responsible for publishing or disseminating the project, optional.
    :vartype publisher: Optional[str]
    :ivar root_package: The root package of the project, serving as the entry point for the project's structure.
    :vartype root_package: Optional[Package]
    :ivar representation_style: The style or methodology used for representing the ontologies within the project.
    :vartype representation_style: OntologyRepresentationStyle
    """

    # Private attributes
    _elements: set[ProjectElement] = PrivateAttr(default_factory=set)
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

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new Project instance with specified attributes.

        This constructor sets up the project with the provided data, ensuring that all project-specific attributes
        are correctly initialized. It also validates the 'elements' attribute to ensure it is a set, reflecting the
        project's structure.

        :param data: Fields to be set on the model instance, including project-specific attributes.
        :type data: dict[str, Any]
        :raises TypeError: If 'elements' is provided and is not a set, ensuring correct data structure.
        """
        super().__init__(**data)

        elements = data.get("elements")
        if elements is not None and not isinstance(elements, set):
            raise TypeError("Expected 'elements' to be a set")
        self._elements: set[ProjectElement] = elements if elements is not None else set()

        if "root_package" in data:
            self.__validate_root_package(data.get("root_package"))

    def __setattr__(self, key, value):
        """Override the default attribute setting behavior to include validation for 'root_package'.

        This method intercepts the setting of the 'root_package' attribute to ensure that the assigned package is
        a part of the project's elements. If the validation fails, a ValueError is raised.

        :param key: The name of the attribute to be set.
        :param value: The value to be assigned to the attribute.
        :type key: str
        :type value: Any
        :raises ValueError: If 'root_package' is set to a package not in the project's elements.
        """
        if key == "root_package":
            self.__validate_root_package(value)
        super().__setattr__(key, value)

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
    def __ensure_non_empty(cls, checked_list: set[str]) -> set[str]:
        """Validate that the provided list does not contain empty strings.

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

    def __validate_root_package(self, package):
        """Validate if the provided package is a part of the project's elements.

        This method checks if the specified package is included in the project's elements set. It is used to ensure
        that the root package is a valid and integral part of the project's structure.

        :param package: The package to be validated as part of the project.
        :type package: Optional[Package]
        :raises ValueError: If the package is not included in the project's elements.
        """
        if package is not None and package not in self._elements:
            raise ValueError("The root_package must be an element of the project.")

    def add_element(self, element: ProjectElement) -> None:
        """Add a new element to the project's collection of elements.

        This method ensures that only instances of ProjectElement or its subclasses are added to the project. It also
        establishes a bidirectional relationship between the project and the element by setting the element's
        'in_project' attribute to this project instance.

        :param element: The ProjectElement to be added.
        :type element: ProjectElement
        :raises TypeError: If the provided element is not an instance of ProjectElement.
        """
        if not isinstance(element, ProjectElement):
            raise TypeError("Element must be an instance of ProjectElement.")

        element._ProjectElement__set_in_project(self)  # direct relation
        self._elements.add(element)  # inverse relation

    def remove_element(self, element: ProjectElement) -> None:
        """Remove an existing element from the project's collection of elements.

        This method ensures that the element to be removed is actually part of the project. It also updates the
        element's 'in_project' attribute to None, effectively breaking the bidirectional relationship.

        :param element: The ProjectElement to be removed.
        :type element: ProjectElement
        :raises TypeError: If the element is not a valid ProjectElement.
        :raises ValueError: If the element is not part of the project.
        """
        if not isinstance(element, ProjectElement):
            raise TypeError(f"Element '{element}' cannot be removed as it is not a valid ProjectElement.")

        if element in self._elements:
            self._elements.remove(element)  # direct relation
            element._ProjectElement__set_in_project(None)  # inverse relation
        else:
            raise ValueError(f"Element '{element}' cannot be removed because is not part of the project.")

    @property
    def elements(self) -> set[ProjectElement]:
        """Provide a read-only view of the project's elements.

        This property is a safeguard to prevent direct modification of the 'elements' set. To add or remove elements,
        use the 'add_element' and 'remove_element' methods. This design ensures that the integrity of the project's
        elements collection is maintained.

        :return: A set of ProjectElement objects that are part of the project.
        :rtype: set[ProjectElement]
        """
        return self._elements

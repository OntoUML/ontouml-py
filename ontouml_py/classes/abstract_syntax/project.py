"""Module for the Project class within an OntoUML model.

The Project class extends NamedElement to include project-specific details such as bibliographic citations,
keywords, and landing pages, among others, providing a comprehensive representation of a project's metadata.
"""

from typing import Optional

from langstring_lib.langstring import LangString
from pydantic import Field

from ontouml_py.classes.abstract_syntax.namedelement import NamedElement
from ontouml_py.classes.ontoumlelement import OntoumlElement


class Project(NamedElement):
    """
    A concrete class representing an OntoUML Project, extending the NamedElement class.

    This class manages project-related elements including acronyms, bibliographic citations, keywords, landing pages,
    and more, providing a rich representation of project metadata.

    :ivar elements: List of OntoumlElement objects in the project.
    :vartype elements: list[OntoumlElement]
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

    elements: list[OntoumlElement] = Field(default_factory=list)
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

    class Config:
        """
        Configuration settings for the Project model using Pydantic.

        :cvar arbitrary_types_allowed: Allows custom types like LangString.
        :vartype arbitrary_types_allowed: bool
        :cvar validate_assignment: Enables validation of field values on assignment.
        :vartype validate_assignment: bool
        :cvar extra: Controls the behavior regarding unexpected fields, set to 'forbid'.
        :vartype extra: str
        """

        arbitrary_types_allowed = True
        validate_assignment = True
        extra = "forbid"

    def __init__(self, **data) -> None:
        """
        Initialize a new Project instance.

        Inherits attributes from NamedElement and adds additional project-specific attributes.

        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)

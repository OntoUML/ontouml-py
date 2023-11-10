"""Define the Project class for representing projects within an OntoUML model.

The Project class extends NamedElement to include project-specific details such as bibliographic citations,
keywords, and landing pages, among others, providing a comprehensive representation of a project's metadata.
"""

from datetime import datetime

from langstring_lib.langstring import LangString

from ontouml_py.classes.abstract_syntax.namedelement import NamedElement
from ontouml_py.classes.ontoumlelement import OntoumlElement
from ontouml_py.utils.utils import validate_and_set


class Project(NamedElement):
    """A concrete class representing an OntoUML Project, extending the NamedElement class.

    This class provides functionality for managing project-related elements, including acronyms, bibliographic
    citations, keywords, landing pages, languages, and more.

    :ivar elements: A list of OntoumlElement objects representing the elements of the project.
    :ivar acronyms: A list of strings representing acronyms associated with the project.
    :ivar bibliographic_citations: A list of strings representing bibliographic citations.
    :ivar keywords: A list of LangString objects representing keywords associated with the project.
    :ivar landing_pages: A list of strings representing URLs to landing pages of the project.
    :ivar languages: A list of strings representing languages used in the project.
    :ivar namespace: A string representing the namespace of the project.
    :ivar sources: A list of strings representing sources of information for the project.
    :ivar access_rights: A list of strings representing access rights information for the project.
    :ivar ontology_types: A list of strings representing types of ontologies used in the project.
    :ivar themes: A list of strings representing themes associated with the project.
    :ivar license: A string representing the licensing information for the project.
    :ivar contexts: A list of strings representing contexts the project is designed for.
    :ivar designed_for_task: A list of strings representing tasks the project is designed for.
    :ivar publisher: A string representing the publisher of the project.
    """
    # TODO (@pedropaulofb): add attribute representation_style, root
    def __init__(
        self,  # INHERITED ATTRIBUTES
        created: datetime = None,
        modified: datetime = None,
        pref_name: LangString = None,
        alt_names: list[LangString] = None,
        description: LangString = None,
        editorial_notes: list[LangString] = None,
        creators: list[str] = None,
        contributors: list[str] = None,
        # CLASS'S ATTRIBUTES
        elements: list[OntoumlElement] = None,
        acronyms: list[str] = None,
        bibliographic_citations: list[str] = None,
        keywords: list[LangString] = None,
        landing_pages: list[str] = None,
        languages: list[str] = None,
        namespace: str = None,
        sources: list[str] = None,
        access_rights: list[str] = None,
        ontology_types: list[str] = None,
        themes: list[str] = None,
        license: str = None,
        contexts: list[str] = None,
        designed_for_task: list[str] = None,
        publisher: str = None,
    ):
        """Initialize a new Project instance.

        :param created: The datetime when the project was created, defaults to the current time if None.
        :type created: Optional[datetime]
        :param modified: The datetime when the project was last modified.
        :type modified: Optional[datetime]
        :param pref_name: The preferred LangString name of the project.
        :type pref_name: Optional[LangString]
        :param alt_names: A list of alternative LangString names for the project.
        :type alt_names: Optional[List[LangString]]
        :param description: A LangString object for the project's description.
        :type description: Optional[LangString]
        :param editorial_notes: A list of LangString objects for the project's editorial notes.
        :type editorial_notes: Optional[List[LangString]]
        :param creators: A list of strings for the URIs of the project's creators.
        :type creators: Optional[List[str]]
        :param contributors: A list of strings for the URIs of the project's contributors.
        :type contributors: Optional[List[str]]
        :param elements: A list of OntoumlElement objects for the project's elements.
        :type elements: Optional[List[OntoumlElement]]
        :param acronyms: A list of strings for the project's acronyms.
        :type acronyms: Optional[List[str]]
        :param bibliographic_citations: A list of strings for the project's bibliographic citations.
        :type bibliographic_citations: Optional[List[str]]
        :param keywords: A list of LangString objects for the project's keywords.
        :type keywords: Optional[List[LangString]]
        :param landing_pages: A list of strings for the project's landing pages URLs.
        :type landing_pages: Optional[List[str]]
        :param languages: A list of strings for the languages used in the project.
        :type languages: Optional[List[str]]
        :param namespace: The namespace string for the project.
        :type namespace: Optional[str]
        :param sources: A list of strings for the project's sources of information.
        :type sources: Optional[List[str]]
        :param access_rights: A list of strings for the project's access rights information.
        :type access_rights: Optional[List[str]]
        :param ontology_types: A list of strings for the types of ontologies used in the project.
        :type ontology_types: Optional[List[str]]
        :param themes: A list of strings for the project's themes.
        :type themes: Optional[List[str]]
        :param license: The licensing information string for the project.
        :type license: Optional[str]
        :param contexts: A list of strings for the contexts the project is designed for.
        :type contexts: Optional[List[str]]
        :param designed_for_task: A list of strings for the tasks the project is designed for.
        :type designed_for_task: Optional[List[str]]
        :param publisher: The publisher string for the project.
        :type publisher: Optional[str]
        """
        # Allows the initialization of the created attribute without overwriting the default value.
        if created is None:
            super().__init__(
                modified=modified,
                pref_name=pref_name,
                alt_names=alt_names,
                description=description,
                editorial_notes=editorial_notes,
                creators=creators,
                contributors=contributors,
            )
        else:
            super().__init__(
                created=created,
                modified=modified,
                pref_name=pref_name,
                alt_names=alt_names,
                description=description,
                editorial_notes=editorial_notes,
                creators=creators,
                contributors=contributors,
            )

        validate_and_set(self, "elements", elements, list[OntoumlElement])
        validate_and_set(self, "acronyms", acronyms, list[str])
        validate_and_set(self, "bibliographic_citations", bibliographic_citations, list[str])
        validate_and_set(self, "keywords", keywords, list[LangString])
        validate_and_set(self, "landing_pages", landing_pages, list[str])
        validate_and_set(self, "languages", languages, list[str])
        validate_and_set(self, "namespace", namespace, str)
        validate_and_set(self, "sources", sources, list[str])
        validate_and_set(self, "access_rights", access_rights, list[str])
        validate_and_set(self, "ontology_types", ontology_types, list[str])
        validate_and_set(self, "themes", themes, list[str])
        validate_and_set(self, "license", license, str)
        validate_and_set(self, "contexts", contexts, list[str])
        validate_and_set(self, "designed_for_task", designed_for_task, list[str])
        validate_and_set(self, "publisher", publisher, str)

x = Project(themes="a")
x.themes="b"
x.themes=1
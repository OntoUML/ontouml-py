"""Module for the abstract NamedElement class within an OntoUML model.

This module defines the NamedElement class, which is an abstract class designed to represent elements with names in an
OntoUML model. It extends the OntoumlElement class and includes additional attributes and validation for managing
named elements' details such as their preferred name, alternative names, descriptions, editorial notes, as well as
lists of creators and contributors.
"""

import datetime
from abc import abstractmethod

from langstring_lib.langstring import LangString

from ontouml_py.classes.ontoumlelement import OntoumlElement
from ontouml_py.utils.utils import validate_and_set


class NamedElement(OntoumlElement):
    """An abstract class representing a named element within an OntoUML model, extending the OntoumlElement class.

    The class provides functionality for managing named elements, including their preferred name, alternative names,
    descriptions, and editorial notes.

    :ivar pref_name: The preferred name of the element, represented as a LangString object.
    :ivar alt_names: A list of alternative names for the element, each represented as a LangString object.
    :ivar description: A LangString object representing the description of the element.
    :ivar editorialNotes: A LangString object containing editorial notes associated with the element.
    :ivar creators: A list of URIs represented as strings identifying the creators of the element.
    :ivar contributors: A list of URIs represented as strings identifying the contributors to the element.

    """

    @abstractmethod
    def __init__(
        self,
        # Inherited attributes
        created: datetime = None,
        modified: datetime = None,
        # Class's attributes
        pref_name: LangString = None,
        alt_names: list[LangString] = None,
        description: LangString = None,
        editorialNotes: LangString = None,
        creators: list[str] = None,
        contributors: list[str] = None,
    ):
        """Initialize a new NamedElement instance, ensuring proper initialization of attributes with validation.

        :param created: The datetime instance representing when the element was created. If not provided, the current
        time is used by default.
        :type created: Optional[datetime], optional
        :param modified: The datetime instance representing when the element was last modified. This is optional and
        can be left as None if the element has not been modified.
        :type modified: Optional[datetime], optional
        :param pref_name: The preferred name of the element, represented as a LangString object.
        :type pref_name: Optional[LangString], optional
        :param alt_names: A list of alternative names for the element, each represented as a LangString object.
        :type alt_names: Optional[List[LangString]], optional
        :param description: A LangString object representing the description of the element.
        :type description: Optional[LangString], optional
        :param editorialNotes: A LangString object containing editorial notes associated with the element.
        :type editorialNotes: Optional[LangString], optional
        :param creators: A list of strings representing the URIs of the creators of the element.
        :type creators: Optional[List[str]], optional
        :param contributors: A list of strings representing the URIs of the contributors to the element.
        :type contributors: Optional[List[str]], optional
        """
        # Allows the initialization of the created attribute without overwriting the default value.
        if created is None:
            super().__init__(modified=modified)
        else:
            super().__init__(created=created, modified=modified)

        validate_and_set(self, "pref_name", pref_name, LangString)
        validate_and_set(self, "alt_names", alt_names, list[LangString])
        validate_and_set(self, "description", description, LangString)
        validate_and_set(self, "editorialNotes", editorialNotes, LangString)
        validate_and_set(self, "creators", creators, list[str])
        validate_and_set(self, "contributors", contributors, list[str])

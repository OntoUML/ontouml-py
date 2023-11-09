import datetime
from abc import abstractmethod

from langstring_lib.langstring import LangString

from ontouml_py.classes.ontoumlelement import OntoumlElement
from ontouml_py.utils.utils import validate_and_set


class NamedElement(OntoumlElement):
    """An abstract class representing a named element within an OntoUML model, extending the OntoumlElement class.

    The class provides functionality for managing named elements, including their preferred name, alternative names,
    descriptions, and editorial notes.

    :ivar prefName: The preferred name of the element, represented as a LangString object.
    :ivar altNames: A list of alternative names for the element, each represented as a LangString object.
    :ivar description: A LangString object representing the description of the element.
    :ivar editorialNotes: A LangString object containing editorial notes associated with the element.
    """

    @abstractmethod
    def __init__(
            self,
            # Inherited attributes
            created: datetime = None,
            modified: datetime = None,
            # Class's attributes
            prefName: LangString = None,
            altNames: list[LangString] = None,
            description: LangString = None,
            editorialNotes: LangString = None,
    ):
        """Initializes a new NamedElement instance, ensuring proper initialization of attributes with validation.

        :param created: The datetime instance representing when the element was created. If not provided, the
                        current time is used by default.
        :type created: Optional[datetime], optional
        :param modified: The datetime instance representing when the element was last modified. This is optional and
                         can be left as None if the element has not been modified.
        :type modified: Optional[datetime], optional
        :param prefName: The preferred name of the element, represented as a LangString object.
        :type prefName: Optional[LangString], optional
        :param altNames: A list of alternative names for the element, each represented as a LangString object.
        :type altNames: Optional[List[LangString]], optional
        :param description: A LangString object representing the description of the element.
        :type description: Optional[LangString], optional
        :param editorialNotes: A LangString object containing editorial notes associated with the element.
        :type editorialNotes: Optional[LangString], optional
        """
        # Allows the initialization of the created attribute without overwriting the default value.
        if created is None:
            super().__init__(modified=modified)
        else:
            super().__init__(created=created, modified=modified)

        validate_and_set(self, "prefName", prefName, LangString)
        validate_and_set(self, "altNames", altNames, list[LangString])
        validate_and_set(self, "description", description, LangString)
        validate_and_set(self, "editorialNotes", editorialNotes, LangString)

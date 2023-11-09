import datetime

from langstring_lib.langstring import LangString

from ontouml_py.classes.ontoumlelement import OntoumlElement
from ontouml_py.utils.utils import secure_set


class NamedElement(OntoumlElement):
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
        # Allows the initialization of the created attribute without overwriting the default value.
        if created is None:
            super().__init__(modified=modified)
        else:
            super().__init__(created=created, modified=modified)

        secure_set(self, "prefName", prefName, LangString)
        secure_set(self, "altNames", altNames, list[LangString])
        secure_set(self, "description", description, LangString)
        secure_set(self, "editorialNotes", editorialNotes, LangString)

import datetime

from icecream import ic
from langstring_lib.langstring import LangString

from ontouml_py.classes.ontoumlelement import OntoumlElement


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
        if created is None:
            super().__init__(modified=modified)
        else:
            super().__init__(created=created, modified=modified)
        self.prefName = prefName
        self.altNames = altNames
        self.description = description
        self.editorialNotes = editorialNotes


a = LangString("a", "en")
d = datetime.datetime(2020, 10, 10)
x = NamedElement(modified=d)
z = OntoumlElement()
ic(x.__dict__)
ic(z.__dict__)

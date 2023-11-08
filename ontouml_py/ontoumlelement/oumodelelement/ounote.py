from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUNote(_OUElement):
    """Represents a note in OntoUML.



    :param object_id: The URI reference of the note.
    :type object_id: URIRef

    :ivar text: The text content of the note.
    :vartype text: List[URIRef]
    """

    def __init__(
        self, object_id: URIRef, text: list[URIRef] = None, name: URIRef = None, description: URIRef = None
    ) -> None:
        related_type = OntoUML.Note
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.text: list[URIRef] = text

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

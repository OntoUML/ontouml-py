from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUText(_OUElement):
    """Represents text in OntoUML.

    :param object_id: The URI reference of the text.
    :type object_id: URIRef

    :ivar height: The height of the text.
    :vartype height: URIRef
    :ivar project: The project to which the text belongs.
    :vartype project: URIRef
    :ivar text: The text content.
    :vartype text: URIRef
    :ivar topLeftPosition: The top-left position of the text.
    :vartype topLeftPosition: URIRef
    :ivar width: The width of the text.
    :vartype width: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        height: URIRef = None,
        project: URIRef = None,
        text: URIRef = None,
        topLeftPosition: URIRef = None,
        width: URIRef = None,
        description: URIRef = None,
    ) -> None:
        related_type = OntoUML.Text
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.height: URIRef = height
        self.project: URIRef = project
        self.text: URIRef = text
        self.topLeftPosition: URIRef = topLeftPosition
        self.width: URIRef = width

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

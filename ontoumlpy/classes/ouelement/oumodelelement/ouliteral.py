from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouexception import OUInvalidAttribute


class OULiteral(_OUElement):
    """Represents a literal in OntoUML.



    :param object_id: The URI reference of the literal.
    :type object_id: URIRef

    :ivar project: The project to which the literal belongs.
    :vartype project: URIRef
    """

    def __init__(
        self, object_id: URIRef, project: URIRef = None, name: URIRef = None, description: URIRef = None
    ) -> None:
        related_type = OntoUML.Literal
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

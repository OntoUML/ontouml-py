from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUPoint(_OUElement):
    """Represents a point in OntoUML.



    :param object_id: The URI reference of the point.
    :type object_id: URIRef

    :ivar xCoordinate: The x-coordinate of the point.
    :vartype xCoordinate: URIRef
    :ivar yCoordinate: The y-coordinate of the point.
    :vartype yCoordinate: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        description: URIRef = None,
        xCoordinate: URIRef = None,
        yCoordinate: URIRef = None,
    ) -> None:
        related_type = OntoUML.Point
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.xCoordinate: URIRef = xCoordinate
        self.yCoordinate: URIRef = yCoordinate

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

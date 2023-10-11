from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouexception import OUInvalidAttribute


class OURectangle(_OUElement):
    """Represents a rectangle in OntoUML.



    :param object_id: The URI reference of the rectangle.
    :type object_id: URIRef

    :ivar topLeftPosition: The top-left position of the rectangle.
    :vartype topLeftPosition: URIRef
    :ivar height: The height of the rectangle.
    :vartype height: URIRef
    :ivar width: The width of the rectangle.
    :vartype width: URIRef
    :ivar project: The project to which the rectangle belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        description: URIRef = None,
        height: URIRef = None,
        name: URIRef = None,
        project: URIRef = None,
        topLeftPosition: URIRef = None,
        width: URIRef = None,
    ) -> None:
        related_type = OntoUML.Rectangle
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.topLeftPosition: URIRef = topLeftPosition
        self.height: URIRef = height
        self.width: URIRef = width
        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

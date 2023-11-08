from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUPath(_OUElement):
    """Represents a path in OntoUML.



    :param object_id: The URI reference of the path.
    :type object_id: URIRef

    :ivar point: A list of points that make up the path.
    :vartype point: List[URIRef]
    :ivar project: The project to which the path belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        description: URIRef = None,
        point: list[URIRef] = None,
        project: URIRef = None,
    ) -> None:
        related_type = OntoUML.Path
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.point: list[URIRef] = point
        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

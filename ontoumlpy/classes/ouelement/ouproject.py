from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouexception import OUInvalidAttribute


class OUProject(_OUElement):
    """Represents a project in OntoUML.



    :param object_id: The URI reference of the project.
    :type object_id: URIRef

    :ivar name: The name of the project.
    :vartype name: URIRef
    :ivar diagram: A list of diagrams associated with the project.
    :vartype diagram: List[URIRef]
    :ivar model: The model associated with the project.
    :vartype model: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        diagram: list[URIRef] = None,
        model: URIRef = None,
        description: URIRef = None,
    ) -> None:
        related_type = OntoUML.Project
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.name: URIRef = name
        self.diagram: list[URIRef] = diagram
        self.model: URIRef = model

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

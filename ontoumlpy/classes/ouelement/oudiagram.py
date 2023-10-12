from icecream import ic
from rdflib import URIRef, Graph

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouexception import OUInvalidAttribute


class OUDiagram(_OUElement):
    """Represents a diagram in OntoUML.

    :param object_id: The URI reference of the diagram.
    :type object_id: URIRef

    :ivar name: The name of the diagram.
    :vartype name: URIRef
    :ivar containsView: A list of views contained within the diagram.
    :vartype containsView: List[URIRef]
    :ivar owner: The owner of the diagram.
    :vartype owner: URIRef
    :ivar project: The project to which the diagram belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        # Mandatory URIRef
        object_id: URIRef,
        # Optional URIRef
        description: URIRef = None,
        name: URIRef = None,
        owner: URIRef = None,
        project: URIRef = None,
        # Optional list[URIRef]
        containsView: list[URIRef] = None,
    ) -> None:
        related_type = OntoUML.Diagram
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.owner: URIRef = owner
        self.project: URIRef = project
        self.containsView: list[URIRef] = containsView

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


g = Graph()
x = OUDiagram(URIRef("x"))
x.add_to_rdf_graph(g)
x.name = URIRef("test")
x.add_to_rdf_graph(g)
x.add_to_rdf_graph(g)
ic()
for s, p, o in g.triples((None, None, None)):
    ic(s, p, o)

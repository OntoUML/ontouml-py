from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUGeneralizationSet(_OUElement):
    """Represents a generalization set in OntoUML.



    :param object_id: The URI reference of the generalization set.
    :type object_id: URIRef

    :ivar generalization: A list of generalizations included in the set.
    :vartype generalization: List[URIRef]
    :ivar isComplete: Indicates if the generalization set is complete.
    :vartype isComplete: URIRef
    :ivar isDisjoint: Indicates if the generalization set is disjoint.
    :vartype isDisjoint: URIRef
    :ivar name: The name of the generalization set.
    :vartype name: URIRef
    :ivar project: The project to which the generalization set belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name=None,
        description=None,
        generalization=None,
        isComplete=None,
        isDisjoint=None,
        project=None,
    ) -> None:
        related_type = OntoUML.GeneralizationSet
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.generalization: list[URIRef] = generalization
        self.isComplete: URIRef = isComplete
        self.isDisjoint: URIRef = isDisjoint
        self.name: URIRef = name
        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

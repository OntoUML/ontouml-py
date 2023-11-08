from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OURelation(_OUElement):
    """Represents a relation in OntoUML.



    :param object_id: The URI reference of the relation.
    :type object_id: URIRef

    :ivar description: The description of the relation.
    :vartype description: URIRef
    :ivar isAbstract: Indicates if the relation is abstract.
    :vartype isAbstract: URIRef
    :ivar isDerived: Indicates if the relation is derived.
    :vartype isDerived: URIRef
    :ivar name: The name of the relation.
    :vartype name: URIRef
    :ivar relationEnd: A list of ends associated with the relation.
    :vartype relationEnd: List[URIRef]
    :ivar sourceEnd: The source end of the relation.
    :vartype sourceEnd: URIRef
    :ivar stereotype: The stereotype of the relation.
    :vartype stereotype: URIRef
    :ivar targetEnd: The target end of the relation.
    :vartype targetEnd: URIRef
    :ivar project: The project to which the relation belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        description: URIRef = None,
        isAbstract: URIRef = None,
        isDerived: URIRef = None,
        relationEnd: URIRef = None,
        stereotype: URIRef = None,
        sourceEnd: URIRef = None,
        targetEnd: URIRef = None,
        project: URIRef = None,
    ) -> None:
        related_type = OntoUML.Relation
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.isAbstract: URIRef = isAbstract
        self.isDerived: URIRef = isDerived
        self.relationEnd: list[URIRef] = relationEnd
        self.sourceEnd: URIRef = sourceEnd
        self.stereotype: URIRef = stereotype
        self.targetEnd: URIRef = targetEnd
        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUProperty(_OUElement):
    """Represents a property in OntoUML.



    :param object_id: The URI reference of the property.
    :type object_id: URIRef

    :ivar aggregationKind: The aggregation kind of the property.
    :vartype aggregationKind: URIRef
    :ivar cardinality: The cardinality of the property.
    :vartype cardinality: URIRef
    :ivar isDerived: Indicates if the property is derived.
    :vartype isDerived: URIRef
    :ivar isOrdered: Indicates if the property is ordered.
    :vartype isOrdered: URIRef
    :ivar isReadOnly: Indicates if the property is read-only.
    :vartype isReadOnly: URIRef
    :ivar name: The name of the property.
    :vartype name: URIRef
    :ivar propertyType: The type of the property.
    :vartype propertyType: URIRef
    :ivar project: The project to which the property belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        aggregationKind: URIRef = None,
        cardinality: URIRef = None,
        description: URIRef = None,
        isDerived: URIRef = None,
        isOrdered: URIRef = None,
        isReadOnly: URIRef = None,
        name: URIRef = None,
        project: URIRef = None,
        propertyType: URIRef = None,
    ) -> None:
        related_type = OntoUML.Property
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.aggregationKind: URIRef = aggregationKind
        self.cardinality: URIRef = cardinality
        self.isDerived: URIRef = isDerived
        self.isOrdered: URIRef = isOrdered
        self.isReadOnly: URIRef = isReadOnly
        self.propertyType: URIRef = propertyType
        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

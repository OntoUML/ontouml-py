from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUCardinality(_OUElement):
    """Represents cardinality information for a property.

    :param object_id: The URI reference of the cardinality object.
    :type object_id: URIRef

    :ivar cardinalityValue: The cardinality value.
    :vartype cardinalityValue: URIRef
    :ivar lowerBound: The lower bound of the cardinality.
    :vartype lowerBound: URIRef
    :ivar upperBound: The upper bound of the cardinality.
    :vartype upperBound: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        cardinalityValue: URIRef = None,
        description: URIRef = None,
        lowerBound: URIRef = None,
        name: URIRef = None,
        upperBound: URIRef = None,
    ) -> None:
        related_type = OntoUML.Cardinality
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.cardinalityValue: URIRef = cardinalityValue
        self.lowerBound: URIRef = lowerBound
        self.upperBound: URIRef = upperBound

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

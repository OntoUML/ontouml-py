class OUCardinality(_OUElement):
    """Represents cardinality information for a property.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the cardinality object.
    :type object_id: URIRef

    :ivar cardinalityValue: The cardinality value.
    :vartype cardinalityValue: URIRef
    :ivar lowerBound: The lower bound of the cardinality.
    :vartype lowerBound: URIRef
    :ivar upperBound: The upper bound of the cardinality.
    :vartype upperBound: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.cardinalityValue: URIRef = ontouml_graph.value(object_id, OntoUML.cardinalityValue)
        self.lowerBound: URIRef = ontouml_graph.value(object_id, OntoUML.lowerBound)
        self.upperBound: URIRef = ontouml_graph.value(object_id, OntoUML.upperBound)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

class OUProperty(_OUElement):
    """Represents a property in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
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

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.aggregationKind: URIRef = ontouml_graph.value(object_id, OntoUML.aggregationKind)
        self.cardinality: URIRef = ontouml_graph.value(object_id, OntoUML.cardinality)
        self.isDerived: URIRef = ontouml_graph.value(object_id, OntoUML.isDerived)
        self.isOrdered: URIRef = ontouml_graph.value(object_id, OntoUML.isOrdered)
        self.isReadOnly: URIRef = ontouml_graph.value(object_id, OntoUML.isReadOnly)
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.propertyType: URIRef = ontouml_graph.value(object_id, OntoUML.propertyType)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

class OUPoint(_OUElement):
    """Represents a point in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the point.
    :type object_id: URIRef

    :ivar xCoordinate: The x-coordinate of the point.
    :vartype xCoordinate: URIRef
    :ivar yCoordinate: The y-coordinate of the point.
    :vartype yCoordinate: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.xCoordinate: URIRef = ontouml_graph.value(object_id, OntoUML.xCoordinate)
        self.yCoordinate: URIRef = ontouml_graph.value(object_id, OntoUML.yCoordinate)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

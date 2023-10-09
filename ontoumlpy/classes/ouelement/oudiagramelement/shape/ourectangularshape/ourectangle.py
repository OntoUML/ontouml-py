class OURectangle(_OUElement):
    """Represents a rectangle in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the rectangle.
    :type object_id: URIRef

    :ivar topLeftPosition: The top-left position of the rectangle.
    :vartype topLeftPosition: URIRef
    :ivar height: The height of the rectangle.
    :vartype height: URIRef
    :ivar width: The width of the rectangle.
    :vartype width: URIRef
    :ivar project: The project to which the rectangle belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.topLeftPosition: URIRef = ontouml_graph.value(object_id, OntoUML.topLeftPosition)
        self.height: URIRef = ontouml_graph.value(object_id, OntoUML.height)
        self.width: URIRef = ontouml_graph.value(object_id, OntoUML.width)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

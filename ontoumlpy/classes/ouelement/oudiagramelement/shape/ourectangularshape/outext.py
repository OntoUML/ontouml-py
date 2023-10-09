class OUText(_OUElement):
    """Represents text in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the text.
    :type object_id: URIRef

    :ivar height: The height of the text.
    :vartype height: URIRef
    :ivar project: The project to which the text belongs.
    :vartype project: URIRef
    :ivar text: The text content.
    :vartype text: URIRef
    :ivar topLeftPosition: The top-left position of the text.
    :vartype topLeftPosition: URIRef
    :ivar width: The width of the text.
    :vartype width: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.height: URIRef = ontouml_graph.value(object_id, OntoUML.height)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.text: URIRef = ontouml_graph.value(object_id, OntoUML.text)
        self.topLeftPosition: URIRef = ontouml_graph.value(object_id, OntoUML.topLeftPosition)
        self.width: URIRef = ontouml_graph.value(object_id, OntoUML.width)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

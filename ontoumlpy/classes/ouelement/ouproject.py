class OUProject(_OUElement):
    """Represents a project in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the project.
    :type object_id: URIRef

    :ivar name: The name of the project.
    :vartype name: URIRef
    :ivar diagram: A list of diagrams associated with the project.
    :vartype diagram: List[URIRef]
    :ivar model: The model associated with the project.
    :vartype model: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.diagram: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.diagram))
        self.model: URIRef = ontouml_graph.value(object_id, OntoUML.model)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

class OUPackage(_OUElement):
    """Represents a package in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the package.
    :type object_id: URIRef

    :ivar containsModelElement: A list of model elements contained within the package.
    :vartype containsModelElement: List[URIRef]
    :ivar name: The name of the package.
    :vartype name: URIRef
    :ivar project: The project to which the package belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.containsModelElement: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.containsModelElement))
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

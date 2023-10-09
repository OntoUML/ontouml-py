class OUGeneralizationSetView(_OUElement):
    """Represents a view of a generalization set in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization set view.
    :type object_id: URIRef

    :ivar isViewOf: The generalization set that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the generalization set view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the generalization set view.
    :vartype shape: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

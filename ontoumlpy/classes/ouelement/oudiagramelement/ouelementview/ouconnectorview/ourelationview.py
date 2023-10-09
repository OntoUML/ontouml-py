class OURelationView(_OUElement):
    """Represents a view of a relation in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the relation view.
    :type object_id: URIRef

    :ivar isViewOf: The relation that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the relation view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the relation view.
    :vartype shape: URIRef
    :ivar sourceView: The source view associated with the relation view.
    :vartype sourceView: URIRef
    :ivar targetView: The target view associated with the relation view.
    :vartype targetView: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)
        self.sourceView: URIRef = ontouml_graph.value(object_id, OntoUML.sourceView)
        self.targetView: URIRef = ontouml_graph.value(object_id, OntoUML.targetView)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

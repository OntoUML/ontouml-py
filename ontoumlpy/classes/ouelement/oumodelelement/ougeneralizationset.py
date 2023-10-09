class OUGeneralizationSet(_OUElement):
    """Represents a generalization set in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization set.
    :type object_id: URIRef

    :ivar generalization: A list of generalizations included in the set.
    :vartype generalization: List[URIRef]
    :ivar isComplete: Indicates if the generalization set is complete.
    :vartype isComplete: URIRef
    :ivar isDisjoint: Indicates if the generalization set is disjoint.
    :vartype isDisjoint: URIRef
    :ivar name: The name of the generalization set.
    :vartype name: URIRef
    :ivar project: The project to which the generalization set belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.generalization: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.generalization))
        self.isComplete: URIRef = ontouml_graph.value(object_id, OntoUML.isComplete)
        self.isDisjoint: URIRef = ontouml_graph.value(object_id, OntoUML.isDisjoint)
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

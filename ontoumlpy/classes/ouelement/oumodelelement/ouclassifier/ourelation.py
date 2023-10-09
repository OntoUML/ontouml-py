class OURelation(_OUElement):
    """Represents a relation in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the relation.
    :type object_id: URIRef

    :ivar description: The description of the relation.
    :vartype description: URIRef
    :ivar isAbstract: Indicates if the relation is abstract.
    :vartype isAbstract: URIRef
    :ivar isDerived: Indicates if the relation is derived.
    :vartype isDerived: URIRef
    :ivar name: The name of the relation.
    :vartype name: URIRef
    :ivar relationEnd: A list of ends associated with the relation.
    :vartype relationEnd: List[URIRef]
    :ivar sourceEnd: The source end of the relation.
    :vartype sourceEnd: URIRef
    :ivar stereotype: The stereotype of the relation.
    :vartype stereotype: URIRef
    :ivar targetEnd: The target end of the relation.
    :vartype targetEnd: URIRef
    :ivar project: The project to which the relation belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.description: URIRef = ontouml_graph.value(object_id, OntoUML.description)
        self.isAbstract: URIRef = ontouml_graph.value(object_id, OntoUML.isAbstract)
        self.isDerived: URIRef = ontouml_graph.value(object_id, OntoUML.isDerived)
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.relationEnd: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.relationEnd))
        self.sourceEnd: URIRef = ontouml_graph.value(object_id, OntoUML.sourceEnd)
        self.stereotype: URIRef = ontouml_graph.value(object_id, OntoUML.stereotype)
        self.targetEnd: URIRef = ontouml_graph.value(object_id, OntoUML.targetEnd)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

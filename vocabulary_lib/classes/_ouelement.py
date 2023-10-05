from rdflib import URIRef, Graph

from vocabulary_lib.classes.ouexception import OUIDNotInGraph, OUIDTypeMismatchError


class _OUElement:
    """Main class for OntoUML models. Private.

    :param object_id: The URI reference of the cardinality object.
    :type object_id: URIRef

    :vartype id: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef, class_name: str, related_type: URIRef):
        if (object_id, None, None) not in ontouml_graph:
            raise OUIDNotInGraph(object_id, class_name)
        elif (object_id, None, related_type) not in ontouml_graph:
            raise OUIDTypeMismatchError(object_id, class_name, related_type)
        else:
            self.id: URIRef = object_id

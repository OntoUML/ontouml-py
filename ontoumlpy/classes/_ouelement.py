"""
This module provides the foundational class for representing elements in OntoUML models.
It includes the `_OUElement` class, which serves as the main class for OntoUML models, and
is designed to be private to prevent direct instantiation. The module also includes
necessary exceptions for handling issues related to OntoUML ID and type mismatches.

The `_OUElement` class is initialized with a URI reference representing the object's ID,
and performs checks to ensure that the ID exists in the provided OntoUML graph and has a
valid type. It raises exceptions (`OUIDNotInGraph`, `OUIDTypeMismatchError`) when these
checks fail, providing informative error messages to facilitate debugging.
"""
from ontoumlpy.classes.ouexception import OUIDNotInGraph, OUIDTypeMismatchError
from rdflib import URIRef, Graph


class _OUElement:
    """Main class for OntoUML models. Private.

    :param object_id: The URI reference of the cardinality object.
    :type object_id: URIRef

    :ivar id: The URI reference of the object.
    :vartype id: URIRef
    :ivar type: The type of the object as a URI reference.
    :vartype type: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef, class_name: str, related_type: URIRef):
        """Initializes an instance of the _OUElement class, verifying the existence and type of the object in \
        the OntoUML graph.

        This constructor method performs two main checks on the provided object_id:
        1. Checks if the object_id exists in the ontouml_graph.
        2. Checks if the object_id has the expected related_type in the ontouml_graph.

        If either check fails, an exception is raised. Otherwise, the instance is successfully created with the
        specified object_id and related_type.

        :param ontouml_graph: The OntoUML graph in which to look for the object_id.
        :type ontouml_graph: Graph
        :param object_id: The URI reference of the object being created.
        :type object_id: URIRef
        :param class_name: The name of the class for which the object is being created.
        :type class_name: str
        :param related_type: The expected type of the object in the OntoUML graph.
        :type related_type: URIRef

        :raises OUIDNotInGraph: If the object_id does not exist in the ontouml_graph.
        :raises OUIDTypeMismatchError: If the object_id exists but does not have the expected related_type in the \
        ontouml_graph.

        :ivar id: The URI reference of the object, initialized to `object_id`.
        :vartype id: URIRef
        :ivar type: The type of the object as a URI reference, initialized to `related_type`.
        :vartype type: URIRef
        """
        # Verify if ID exists in the graph
        if (object_id, None, None) not in ontouml_graph:
            raise OUIDNotInGraph(object_id, class_name)

        # Verify if ID has a valid type
        elif (object_id, None, related_type) not in ontouml_graph:
            raise OUIDTypeMismatchError(object_id, class_name, related_type)

        # If valid, instantiate
        else:
            self.id: URIRef = object_id
            self.type: URIRef = related_type

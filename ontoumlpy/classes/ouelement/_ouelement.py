"""This module provides foundational classes for representing elements in OntoUML models.

The module contains the `_OUElement` class, which serves as the base class for OntoUML models. Designed to be
abstract and protected, it must not be directly used by users and prevents direct instantiation, requiring subclassing
to provide specific functionalities and representations for OntoUML models.

While managing elements within the model by keeping track of their ID, type, name, and description using
URI references, `_OUElement` does not perform checks for the existence or the validity of the ID within an OntoUML
graph. Such checks and additional logic for managing OntoUML models should be implemented within
subclasses.

Note that the implementation assumes URI references are utilized for model element identification, ensuring
compatibility with RDF data structures and semantics.
"""
from abc import abstractmethod

from icecream import ic
from loguru import logger
from rdflib import URIRef, Graph, RDF

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouexception import OUUnavailableOUTerm


class _OUElement:
    """Abstract and protected foundational class for elements in OntoUML models.

    The `_OUElement` class encapsulates common attributes like ID, name, type, and description using URI references and
    is intended to be subclassed to provide specific functionalities and representations for OntoUML models. Direct
    instantiation is discouraged, and therefore, the class is marked as abstract.

    :ivar id: The URI reference identifying the object.
    :vartype id: URIRef
    :ivar description: A textual description of the object being created, represented as a URI reference.
    :vartype description: URIRef
    :ivar element_type: The type of the object represented as a URI reference.
    :vartype element_type: URIRef
    :ivar name: The name of the object, represented as a URI reference.
    :vartype name: URIRef
    """

    element_term_mapping = {}

    @abstractmethod
    def __init__(self, object_id: URIRef, related_type: URIRef, name: URIRef, description: URIRef):
        """Initialize an instance of the _OUElement class, intended to be overridden by child classes.

        Declared as abstract, it indicates that the class should not be used to instantiate objects directly and should
        be implemented by subclasses. However, it includes logic to set up basic properties, allowing for attribute setup
        in derived classes.

        :param object_id: The URI reference of the object being created.
        :type object_id: URIRef
        :param related_type: The URI reference indicating the OntoUML type for the object.
        :type related_type: URIRef
        :param name: The name of the object being created.
        :type name: URIRef
        :param description: A textual description of the object being created.
        :type description: URIRef
        """

        # If valid, instantiate
        self.id: URIRef = object_id
        self.name: URIRef = name
        self.description: URIRef = description
        self.element_type: URIRef = related_type

    def add_to_rdf_graph(self, graph: Graph) -> None:
        """Integrate the _OUElement instance data into the provided RDF graph.

        This method selectively iterates through the attributes of an _OUElement instance, identifies corresponding
        OntoUML terms, and inserts triples into the supplied RDF graph, where each triple represents a meaningful
        semantic relationship (subject, predicate, object) pertinent to OntoUML models.

        Notably, while the method acts on the current state of the instance, it does not maintain ongoing synchronization
        with subsequent alterations to the element. Therefore, subsequent changes to the element post-graph addition
        will not automatically reflect in the graph and would necessitate a re-invocation of this method for update.

        In cases where the OntoUML term for a particular attribute is unavailable, the method proceeds without raising
        an exception or halting execution but does log the occurrence for debugging purposes. This behavior ensures that
        a singular issue during the graph addition process does not inhibit the incorporation of remaining, valid data.

        :param graph: The RDF graph where the instance’s semantic data, in the form of triples, should be appended.
        :type graph: Graph
        """
        # Inserting element type as a fundamental triple
        graph.add((self.id, RDF.type, self.element_type))

        # Iterating through and adding other object properties
        for obj_predicate in self.__dict__:
            try:
                elem_predicate = OntoUML.get_term(obj_predicate)
                elem_object = getattr(self, obj_predicate)
                if elem_object:
                    graph.add((self.id, elem_predicate, elem_object))
            except OUUnavailableOUTerm:
                logger.debug(f"OntoUML.get_term({obj_predicate}) generated an OUUnavailableOUTerm exception.")

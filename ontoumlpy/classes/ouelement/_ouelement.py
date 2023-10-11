"""This module provides foundational classes for representing elements in OntoUML models.

The module contains the `_OUElement` class, which serves as a foundational class for OntoUML models. Designed to be
abstract and protected, it prevents direct instantiation, requiring subclassing to provide specific functionalities and
representations for OntoUML models.

While managing elements within the model by keeping track of their ID, type, name, and description using
URI references, `_OUElement` does not perform checks for the existence or the validity of the ID within an OntoUML
graph. Such checks and additional logic for managing OntoUML models should be implemented within
subclasses.

Note that the implementation assumes URI references are utilized for model element identification, ensuring
compatibility with RDF data structures and semantics.
"""
from abc import abstractmethod

from rdflib import URIRef


class _OUElement:
    """Abstract and protected foundational class for elements in OntoUML models.

    The `_OUElement` class encapsulates common attributes like ID, name, type, and description using URI references,
    and is intended to be subclassed to provide specific functionalities and representations for OntoUML models.
    Direct instantiation is discouraged and, therefore, the class is marked as abstract.

    :ivar id: The URI reference of the object.
    :vartype id: URIRef
    :ivar description: A textual description of the object being created.
    :vartype description: URIRef
    :ivar type: The type of the object as a URI reference.
    :vartype type: URIRef
    :ivar name: The name of the object.
    :vartype name: URIRef
    """

    element_term_mapping = {}

    @abstractmethod
    def __init__(self, object_id: URIRef, related_type: URIRef, name: URIRef, description: URIRef):
        """Initialize an instance of the _OUElement class, intended to be overridden by child classes.

        Declared as abstract, it indicates that the class should not be used to instantiate objects directly and should
        be implemented by subclasses. However, it includes logic to set up basic properties, allowing for attribute
        setup in derived classes.

        :param object_id: The URI reference of the object being created.
        :type object_id: URIRef
        :param related_type: The URI reference indicating the OntoUML type for the object.
        :type related_type: URIRef
        :param name: The name of the object being created, optional, default is None.
        :type name: URIRef, optional
        :param description: A textual description of the object being created, optional, default is None.
        :type description: URIRef, optional
        """

        # If valid, instantiate
        self.id: URIRef = object_id
        self.name: URIRef = name
        self.description: URIRef = description
        self.type: URIRef = related_type

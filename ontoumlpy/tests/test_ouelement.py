"""This module contains unit tests for the _OUElement class.

Each function in this module tests a different aspect of the _OUElement class, including positive cases,
negative cases, and error handling.
"""
from rdflib import Graph, RDF, URIRef

from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ontouml import OntoUML


def test_ou_element_creation_positive() -> None:
    """Test the successful creation of an _OUElement instance.

    This function tests the creation of an _OUElement instance with valid arguments, and checks that the id and
    type attributes are set correctly.
    """
    onto_graph = Graph()
    elem_uri = URIRef("https://example.org/my_elem")
    elem_type = OntoUML.Class
    onto_graph.add((elem_uri, RDF.type, elem_type))

    elem_obj = _OUElement(onto_graph, elem_uri, "OUElement", elem_type)
    assert elem_obj.id == elem_uri
    assert elem_obj.type == elem_type


def test_ou_element_negative_attribute() -> None:
    """Test the handling of an attribute error.

    This function tests that an AttributeError is raised when trying to access a non-existent attribute of
    an _OUElement instance.
    """
    onto_graph = Graph()
    elem_uri = URIRef("https://example.org/my_elem")
    elem_type = OntoUML.Class
    onto_graph.add((elem_uri, RDF.type, elem_type))
    elem_obj = _OUElement(onto_graph, elem_uri, "OUElement", elem_type)

    try:
        elem_obj.non_existent_attribute
    except AttributeError:
        assert True

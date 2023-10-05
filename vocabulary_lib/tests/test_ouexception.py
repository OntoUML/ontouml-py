"""Module for testing custom exceptions related to OntoUML."""
import pytest
from icecream import ic
from rdflib import Graph, URIRef, RDF

from vocabulary_lib.classes.ouelement_types import OUCardinality, OURectangle, OUPath, OUNoteView, OUText, OUClass
from vocabulary_lib.classes.ouexception import OUIDNotInGraph, OUIDTypeMismatchError
from vocabulary_lib.classes.outerm import OUTerm


def test_ouid_not_in_graph_exception_positive() -> None:
    """Test case for the 'OUIDNotInGraph' exception when the ID does not exist in the OntoUML graph.

    :raises OUIDNotInGraph: When the provided ID does not exist in the OntoUML graph.
    """
    absent_id = URIRef("http://example.com/nonexistent_id")
    graph = Graph()

    try:
        x = OUClass(graph, absent_id)
        assert False
    except OUIDNotInGraph:
        assert True
    except Exception:
        assert False


def test_ouid_not_in_graph_exception_negative() -> None:
    """Test case for the 'OUIDNotInGraph' exception when the ID exists in the OntoUML graph.

    :raises OUIDNotInGraph: When the provided ID exists in the OntoUML graph.
    """
    present_id = URIRef("http://example.com/nonexistent_id")
    graph = Graph()
    graph.add((present_id, RDF.type, OUTerm.Class))

    try:
        x = OUClass(graph, present_id)
        assert True
    except OUIDNotInGraph:
        assert False
    except Exception:
        assert False


@pytest.mark.parametrize("ouclass, outerm", [(OUClass, OUTerm.Cardinality), (), (), (), ()])
def test_ouid_type_mismatch_error_positive(ouclass, outerm) -> None:
    """Test case for the 'OUIDTypeMismatchError' exception when the ID has a type mismatch.

    :raises OUIDTypeMismatchError: When the provided ID has a type mismatch with the expected type.
    """
    elem_id = URIRef("http://example.com/elem_id")
    graph = Graph()
    graph.add((elem_id, RDF.type, outerm))

    ic(ouclass)
    ic(outerm)

    try:
        x = ouclass(graph, elem_id)
        assert False
    except OUIDTypeMismatchError:
        assert True
    except Exception:
        assert False


def test_ouid_type_mismatch_error_negative() -> None:
    """Test case for the 'OUIDTypeMismatchError' exception when the ID has the expected type.

    :raises OUIDTypeMismatchError: When the provided ID has the expected type.
    """
    elem_id1 = URIRef("http://example.com/elem_id1")
    elem_id2 = URIRef("http://example.com/elem_id2")
    elem_id3 = URIRef("http://example.com/elem_id3")
    elem_id4 = URIRef("http://example.com/elem_id4")
    elem_id5 = URIRef("http://example.com/elem_id5")
    graph = Graph()
    graph.add((elem_id1, RDF.type, OUTerm.Cardinality))
    graph.add((elem_id2, RDF.type, OUTerm.Rectangle))
    graph.add((elem_id3, RDF.type, OUTerm.Path))
    graph.add((elem_id4, RDF.type, OUTerm.NoteView))
    graph.add((elem_id5, RDF.type, OUTerm.Text))

    try:
        x1 = OUCardinality(graph, elem_id1)
        x2 = OURectangle(graph, elem_id2)
        x3 = OUPath(graph, elem_id3)
        x4 = OUNoteView(graph, elem_id4)
        x5 = OUText(graph, elem_id5)
        assert True
    except OUIDTypeMismatchError:
        assert False
    except Exception:
        assert False


def test_ou_invalid_attribute_positive() -> None:
    pass


def test_ou_invalid_attribute_negative() -> None:
    pass

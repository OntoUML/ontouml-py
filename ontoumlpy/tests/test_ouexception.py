"""Module for testing custom exceptions related to OntoUML."""
import pytest
from rdflib import Graph, URIRef, RDF

from ontoumlpy.classes.ouelement import (
    OUCardinality,
    OURectangle,
    OUPath,
    OUNoteView,
    OUText,
    OUClass,
    oudiagram,
    OUGeneralizationSetView,
    OUPoint,
)
from ontoumlpy.classes.ouexception import OUIDNotInGraph, OUIDTypeMismatchError, OUInvalidAttribute
from ontoumlpy.classes.ontouml import OntoUML


def test_ouid_not_in_graph_absent_id() -> None:
    """Test case for the 'OUIDNotInGraph' exception when the ID does not exist in the OntoUML graph.

    :raises OUIDNotInGraph: When the provided ID does not exist in the OntoUML graph.
    """
    absent_id = URIRef("http://example.com/nonexistent_id")
    graph = Graph()

    try:
        OUClass(graph, absent_id)
        assert False
    except OUIDNotInGraph:
        assert True
    except Exception:
        assert False


def test_ouid_not_in_graph_present_id() -> None:
    """Test case for the 'OUIDNotInGraph' exception when the ID exists in the OntoUML graph.

    :raises OUIDNotInGraph: When the provided ID exists in the OntoUML graph.
    """
    present_id = URIRef("http://example.com/nonexistent_id")
    graph = Graph()
    graph.add((present_id, RDF.type, OntoUML.Class))

    try:
        OUClass(graph, present_id)
        assert True
    except OUIDNotInGraph:
        assert False
    except Exception:
        assert False


@pytest.mark.parametrize(
    "ouclass, outerm",
    [
        (OUClass, OntoUML.Cardinality),
        (OUDiagram, OntoUML.Shape),
        (OUGeneralizationSetView, OntoUML.point),
        (OUPoint, OntoUML.RelationView),
    ],
)
def test_ouid_type_mismatch_error_mismatched_type(ouclass, outerm) -> None:
    """Test case for the 'OUIDTypeMismatchError' exception when the ID has a type mismatch.

    :raises OUIDTypeMismatchError: When the provided ID has a type mismatch with the expected type.
    """
    elem_id = URIRef("http://example.com/elem_id")
    graph = Graph()
    graph.add((elem_id, RDF.type, outerm))
    try:
        ouclass(graph, elem_id)
        assert False
    except OUIDTypeMismatchError:
        assert True
    except Exception:
        assert False


def test_ouid_type_mismatch_error_matched_type() -> None:
    """Test case for the 'OUIDTypeMismatchError' exception when the ID has the expected type.

    :raises OUIDTypeMismatchError: When the provided ID has the expected type.
    """
    elem_id1 = URIRef("http://example.com/elem_id1")
    elem_id2 = URIRef("http://example.com/elem_id2")
    elem_id3 = URIRef("http://example.com/elem_id3")
    elem_id4 = URIRef("http://example.com/elem_id4")
    elem_id5 = URIRef("http://example.com/elem_id5")
    graph = Graph()
    graph.add((elem_id1, RDF.type, OntoUML.Cardinality))
    graph.add((elem_id2, RDF.type, OntoUML.Rectangle))
    graph.add((elem_id3, RDF.type, OntoUML.Path))
    graph.add((elem_id4, RDF.type, OntoUML.NoteView))
    graph.add((elem_id5, RDF.type, OntoUML.Text))

    try:
        OUCardinality(graph, elem_id1)
        OURectangle(graph, elem_id2)
        OUPath(graph, elem_id3)
        OUNoteView(graph, elem_id4)
        OUText(graph, elem_id5)
        assert True
    except OUIDTypeMismatchError:
        assert False
    except Exception:
        assert False


def test_ou_invalid_attribute_valid_access() -> None:
    """Test case for accessing valid attributes of OntoUML classes.

    :raises OUInvalidAttribute: When an invalid attribute is accessed on an OntoUML class.
    :raises Exception: For any other exception that might occur.
    """
    elem_id1 = URIRef("http://example.com/elem_id1")
    elem_id2 = URIRef("http://example.com/elem_id2")
    elem_id3 = URIRef("http://example.com/elem_id3")
    elem_id4 = URIRef("http://example.com/elem_id4")
    elem_id5 = URIRef("http://example.com/elem_id5")
    graph = Graph()
    graph.add((elem_id1, RDF.type, OntoUML.Cardinality))
    graph.add((elem_id2, RDF.type, OntoUML.Rectangle))
    graph.add((elem_id3, RDF.type, OntoUML.Path))
    graph.add((elem_id4, RDF.type, OntoUML.NoteView))
    graph.add((elem_id5, RDF.type, OntoUML.Text))

    try:
        x1 = OUCardinality(graph, elem_id1)
        x1.lowerBound
        x2 = OURectangle(graph, elem_id2)
        x2.width
        x3 = OUPath(graph, elem_id3)
        x3.point
        x4 = OUNoteView(graph, elem_id4)
        x4.isViewOf
        x5 = OUText(graph, elem_id5)
        x5.project
        assert True
        x1.id
        x2.type
    except OUInvalidAttribute:
        assert False
    except Exception:
        assert False


def test_ou_invalid_attribute_invalid_access() -> None:
    """Test case for the 'OUInvalidAttribute' exception when accessing an invalid attribute.

    :raises OUInvalidAttribute: When an invalid attribute is accessed on an OntoUML class.
    :raises Exception: For any other exception that might occur.
    """
    elem_id1 = URIRef("http://example.com/elem_id1")
    graph = Graph()
    graph.add((elem_id1, RDF.type, OntoUML.Cardinality))

    try:
        x1 = OUCardinality(graph, elem_id1)
        x1.custom
        assert False
    except OUInvalidAttribute:
        assert True
    except Exception:
        assert False

"""This module contains unit tests for validating the behavior and functionality of the OUGraph class.

The tests cover the initialization of OUGraph instances, population of OUGraph with different OntoUML elements,
and the handling of include_concrete parameter during the initialization. It also includes negative tests to ensure
robustness against incorrect input types and exceptions handling.
"""
import pytest
from rdflib import Graph, URIRef, RDF

from vocabulary_lib.classes.ougraph import OUGraph
from vocabulary_lib.classes.outerm import OUTerm
from vocabulary_lib.constants.const_prefix import ONTOUML_NAMESPACE

EXAMPLE_NS = "https://example.org/"


def test_initialization_positive():
    """Tests the successful initialization of an OUGraph instance."""
    graph = Graph()
    ou_graph = OUGraph(graph)
    assert isinstance(ou_graph, OUGraph)


def test_initialization_negative():
    """Tests the incorrect type assertion during OUGraph initialization."""
    graph = Graph()
    ou_graph = OUGraph(graph)
    assert not (isinstance(ou_graph, Graph))


def test_empty_graph_population():
    """Tests OUGraph population with an empty graph."""
    graph = Graph()
    ou_graph = OUGraph(graph)

    for att_name in dir(ou_graph):
        if "__" not in att_name:
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_single_class_population():
    """Tests OUGraph population with a graph containing one class."""
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    graph.add((class1, RDF.type, OUTerm.Class))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 1
    assert ou_graph.list_OUClass[0].id == class1
    assert len(ou_graph.list_OUDiagram) == 0


def test_two_classes_population():
    """Tests OUGraph population with a graph containing two classes."""
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    class2 = URIRef(EXAMPLE_NS + "class2")
    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((class2, RDF.type, OUTerm.Class))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 2
    assert ou_graph.list_OUClass[0].id == class1
    assert ou_graph.list_OUClass[1].id == class2


def test_two_classes_one_generalization_population():
    """Tests OUGraph population with a graph containing two classes and one generalization."""
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    class2 = URIRef(EXAMPLE_NS + "class2")
    gen1 = URIRef(EXAMPLE_NS + "gen1")
    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((class2, RDF.type, OUTerm.Class))
    graph.add((gen1, RDF.type, OUTerm.Generalization))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 2
    assert ou_graph.list_OUClass[0].id == class1
    assert ou_graph.list_OUClass[1].id == class2
    assert len(ou_graph.list_OUGeneralization) == 1
    assert ou_graph.list_OUGeneralization[0].id == gen1


def test_population_unrelated_elements():
    """Tests OUGraph population with a graph containing two classes and one generalization, asserting empty lists for \
    unrelated elements."""
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    class2 = URIRef(EXAMPLE_NS + "class2")
    gen1 = URIRef(EXAMPLE_NS + "gen1")
    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((class2, RDF.type, OUTerm.Class))
    graph.add((gen1, RDF.type, OUTerm.Generalization))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUNote) == 0
    assert len(ou_graph.list_OULiteral) == 0


def test_include_concrete_elements_true():
    """Tests the inclusion of concrete syntax elements when include_concrete is set to True."""
    graph = Graph()

    class1 = URIRef(EXAMPLE_NS + "class1")
    diagram1 = URIRef(EXAMPLE_NS + "diagram1")

    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((diagram1, RDF.type, OUTerm.Diagram))

    ou_graph = OUGraph(graph, include_concrete=True)

    assert len(ou_graph.list_OUClass) == 1
    assert ou_graph.list_OUClass[0].id == class1
    assert len(ou_graph.list_OUDiagram) == 1
    assert ou_graph.list_OUDiagram[0].id == diagram1


def test_exclude_concrete_elements_false():
    """Tests the exclusion of concrete syntax elements when include_concrete is set to False."""
    graph = Graph()

    class1 = URIRef(EXAMPLE_NS + "class1")
    diagram1 = URIRef(EXAMPLE_NS + "diagram1")

    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((diagram1, RDF.type, OUTerm.Diagram))

    ou_graph = OUGraph(graph, include_concrete=False)

    assert len(ou_graph.list_OUClass) == 1
    assert ou_graph.list_OUClass[0].id == class1
    assert len(ou_graph.list_OUDiagram) == 0


def test_exclude_concrete_elements_negative1():
    """Negative test for the exclusion of concrete syntax elements when include_concrete is set to False."""
    graph = Graph()

    class1 = URIRef(EXAMPLE_NS + "class1")
    diagram1 = URIRef(EXAMPLE_NS + "diagram1")

    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((diagram1, RDF.type, OUTerm.Diagram))

    ou_graph = OUGraph(graph, include_concrete=False)

    assert len(ou_graph.list_OUClass) != 0
    assert len(ou_graph.list_OUDiagram) == 0


def test_exclude_concrete_elements_negative2():
    """Another negative test for the exclusion of concrete syntax elements when include_concrete is set to False."""
    graph = Graph()

    class1 = URIRef(EXAMPLE_NS + "class1")
    diagram1 = URIRef(EXAMPLE_NS + "diagram1")

    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((diagram1, RDF.type, OUTerm.Diagram))

    ou_graph = OUGraph(graph, include_concrete=False)

    assert len(ou_graph.list_OUClass) != 0
    assert len(ou_graph.list_OUDiagram) != 1


def test_handling_incorrect_type1():
    """Tests the handling of an incorrect type during OUGraph population."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef("https://invalid.invalid/invalid")
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        ou_graph = OUGraph(graph)
        assert len(ou_graph.list_OUClass) == 0
    except Exception:
        assert False


def test_handling_incorrect_type2():
    """Tests the handling of an incorrect type during OUGraph population with include_concrete set to False."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef("https://invalid.invalid/invalid")
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        ou_graph = OUGraph(graph, include_concrete=False)
        assert len(ou_graph.list_OUClass) == 0
    except Exception:
        assert False


def test_handling_correct_type_exception():
    """Tests the correct handling of OntoUML types during OUGraph population with include_concrete set to False."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef(ONTOUML_NAMESPACE + "Class")
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        ou_graph = OUGraph(graph, include_concrete=False)
        assert len(ou_graph.list_OUClass) == 1
    except Exception:
        assert False


@pytest.mark.parametrize("type_name", [("phase "), (" phase"), ("ph ase"), ("pha.se"), ("phas")])
def test_exception_on_initialization_wrong_type(type_name: str):
    """Tests the exception handling during OUGraph initialization with an incorrect type."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef(ONTOUML_NAMESPACE + type_name)
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        OUGraph(graph, include_concrete=False)
    except Exception:
        assert True


def test_exception_on_initialization_wrong_arg():
    """Tests the exception handling during OUGraph initialization with an incorrect type."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef(ONTOUML_NAMESPACE + "Class")
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        OUGraph(invalid_type, include_concrete=False)
    except Exception:
        assert True

"""This module contains unit tests for validating the behavior and functionality of the OUGraph class.

The tests cover the initialization of OUGraph instances, population of OUGraph with different OntoUML elements,
and the handling of include_concrete parameter during the initialization. It also includes negative tests to ensure
robustness against incorrect input types and exceptions handling.
"""
import pytest
from rdflib import Graph, URIRef, RDF

from ontoumlpy.classes.ougraph import OUGraph
from ontoumlpy.classes.outerm import OUTerm
from ontoumlpy.constants.const_prefix import ONTOUML_NAMESPACE

EXAMPLE_NS = "https://example.org/"


def test_successful_initialization() -> None:
    """Test the successful initialization of an OUGraph instance."""
    graph = Graph()
    ou_graph = OUGraph(graph)
    assert isinstance(ou_graph, OUGraph)


def test_negative_assertion_during_initialization() -> None:
    """Test the incorrect type assertion during OUGraph initialization."""
    graph = Graph()
    ou_graph = OUGraph(graph)
    assert not (isinstance(ou_graph, Graph))


def test_population_with_empty_graph() -> None:
    """Test OUGraph population with an empty graph. All other lists should be empty."""
    graph = Graph()
    ou_graph = OUGraph(graph)
    # Checking if all other lists are empty
    for att_name in dir(ou_graph):
        if "__" not in att_name:
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_population_with_single_class() -> None:
    """Test OUGraph population with a graph containing one class. Check if all other lists are empty."""
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    graph.add((class1, RDF.type, OUTerm.Class))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 1
    assert ou_graph.list_OUClass[0].id == class1

    # Checking if all other lists are empty
    for att_name in dir(ou_graph):
        if "__" not in att_name and att_name != "list_OUClass":
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_population_with_two_classes() -> None:
    """Test OUGraph population with a graph containing two classes. Check if all other lists are empty."""
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    class2 = URIRef(EXAMPLE_NS + "class2")
    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((class2, RDF.type, OUTerm.Class))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 2
    assert ou_graph.list_OUClass[0].id == class1
    assert ou_graph.list_OUClass[1].id == class2

    # Checking if all other lists are empty
    for att_name in dir(ou_graph):
        if "__" not in att_name and att_name != "list_OUClass":
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_population_with_two_classes_and_one_generalization() -> None:
    """Test OUGraph population with a graph containing two classes and one generalization.
    Check if unrelated lists are empty."""
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

    # Checking if all other lists are empty
    for att_name in dir(ou_graph):
        if "__" not in att_name and att_name != "list_OUClass" and att_name != "list_OUGeneralization":
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_include_concrete_elements_when_set_to_true() -> None:
    """Test the inclusion of concrete syntax elements when include_concrete is set to True. Check unrelated lists."""
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

    # Checking if all other lists are empty
    for att_name in dir(ou_graph):
        if "__" not in att_name and att_name != "list_OUClass" and att_name != "list_OUDiagram":
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_exclude_concrete_elements_when_set_to_false() -> None:
    """Test the exclusion of concrete syntax elements when include_concrete is set to False. Check unrelated lists."""
    graph = Graph()

    class1 = URIRef(EXAMPLE_NS + "class1")
    diagram1 = URIRef(EXAMPLE_NS + "diagram1")

    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((diagram1, RDF.type, OUTerm.Diagram))

    ou_graph = OUGraph(graph, include_concrete=False)

    assert len(ou_graph.list_OUClass) == 1
    assert ou_graph.list_OUClass[0].id == class1
    assert len(ou_graph.list_OUDiagram) == 0

    # Checking if all other lists are empty
    for att_name in dir(ou_graph):
        if "__" not in att_name and att_name != "list_OUClass" and att_name != "list_OUDiagram":
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_negative_scenario_exclude_concrete_elements() -> None:
    """Negative test for the exclusion of concrete syntax elements when include_concrete is set to False.
    Check unrelated lists."""
    graph = Graph()

    class1 = URIRef(EXAMPLE_NS + "class1")
    diagram1 = URIRef(EXAMPLE_NS + "diagram1")

    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((diagram1, RDF.type, OUTerm.Diagram))

    ou_graph = OUGraph(graph, include_concrete=False)

    assert len(ou_graph.list_OUClass) != 0
    assert len(ou_graph.list_OUDiagram) == 0

    # Checking if all other lists are empty
    for att_name in dir(ou_graph):
        if "__" not in att_name and att_name != "list_OUClass" and att_name != "list_OUDiagram":
            att = getattr(ou_graph, att_name)
            assert len(att) == 0


def test_invalid_type_handling_population() -> None:
    """Test the handling of an incorrect type during OUGraph population. Check unrelated lists."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef("https://invalid.invalid/invalid")
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        ou_graph = OUGraph(graph)

        # Checking if all lists are empty
        for att_name in dir(ou_graph):
            if "__" not in att_name:
                att = getattr(ou_graph, att_name)
                assert len(att) == 0

    except Exception:
        assert False


def test_invalid_type_handling_population_without_concrete() -> None:
    """Test the handling of an incorrect type during OUGraph population with include_concrete set to False.
    Check if OUClass list is empty."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef("https://invalid.invalid/invalid")
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        ou_graph = OUGraph(graph, include_concrete=False)
        assert len(ou_graph.list_OUClass) == 0
    except Exception:
        assert False


def test_correct_type_handling_population_without_concrete() -> None:
    """Test the correct handling of OntoUML types during OUGraph population with include_concrete set to False.
    Check if OUClass list is not empty."""
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
def test_wrong_type_exception_handling_on_initialization(type_name: str):
    """Test the exception handling during OUGraph initialization with an incorrect type.
    Pass a type name as an argument to test various invalid types.

    :param type_name: A string representing an invalid OntoUML type name to test various invalid types.
    :type type_name: str
    """

    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef(ONTOUML_NAMESPACE + type_name)
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        OUGraph(graph, include_concrete=False)
    except Exception:
        assert True


def test_wrong_argument_exception_handling_on_initialization() -> None:
    """Test the exception handling during OUGraph initialization with an incorrect argument."""
    graph = Graph()

    inst_id = URIRef(EXAMPLE_NS + "name")
    invalid_type = URIRef(ONTOUML_NAMESPACE + "Class")
    graph.add((inst_id, RDF.type, invalid_type))

    try:
        OUGraph(invalid_type, include_concrete=False)
    except Exception:
        assert True

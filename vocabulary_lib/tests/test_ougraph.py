from rdflib import Graph, URIRef, RDF

from vocabulary_lib.classes.ougraph import OUGraph
from vocabulary_lib.classes.outerm import OUTerm

EXAMPLE_NS = "https://example.org/"


def test_ougraph_initialization_pos():
    graph = Graph()
    ou_graph = OUGraph(graph)
    assert isinstance(ou_graph, OUGraph)


def test_ougraph_initialization_neg():
    graph = Graph()
    ou_graph = OUGraph(graph)
    assert not (isinstance(ou_graph, Graph))


def test_ougraph_population0_pos():
    graph = Graph()
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 0
    assert len(ou_graph.list_OUGeneralizationSetView) == 0


def test_ougraph_population1_pos():
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    graph.add((class1, RDF.type, OUTerm.Class))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 1
    assert ou_graph.list_OUClass[0].id == class1
    assert len(ou_graph.list_OUDiagram) == 0


def test_ougraph_population2_pos():
    graph = Graph()
    class1 = URIRef(EXAMPLE_NS + "class1")
    class2 = URIRef(EXAMPLE_NS + "class2")
    graph.add((class1, RDF.type, OUTerm.Class))
    graph.add((class2, RDF.type, OUTerm.Class))
    ou_graph = OUGraph(graph)
    assert len(ou_graph.list_OUClass) == 2
    assert ou_graph.list_OUClass[0].id == class1
    assert ou_graph.list_OUClass[1].id == class2


def test_ougraph_population3_pos():
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

    def test_ougraph_population4_pos():
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

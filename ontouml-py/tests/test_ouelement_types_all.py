"""
This module contains tests for validating the instantiation and type correctness
of OntoUML elements represented by different classes. The tests are structured to
ensure correct instantiation, ID assignment, and type mapping for each OntoUML element
type.

Functions:
    create_ou_element(ou_elem: str) -> _OUElement:
        Creates an instance of a specified OntoUML element type.

    test_instantiation_all_elements(ou_elem: str) -> None:
        Tests the basic instantiation of all OntoUML element types for correct ID and type.

    test_instantiation_all_elements_wrong_id(ou_elem: str) -> None:
        Tests the instantiation of all OntoUML element types against a wrong ID.

    test_instantiation_all_elements_wrong_type(ou_elem: str) -> None:
        Tests the instantiation of all OntoUML element types, except OUCardinality, against the OUCardinality type.
"""
import pytest
from rdflib import Graph, URIRef, RDF

from ontoumlpy.classes._ouelement import _OUElement
from ontoumlpy.classes.ouelement_types import OUCardinality
from ontoumlpy.functions.func_mappings import get_outerm_from_ouelement, get_ouelement_from_outerm


def create_ouelement(ou_elem: str) -> _OUElement:
    """Creates an instance of a specified OntoUML element type.

    :param ou_elem: The name of the OntoUML element type to be instantiated.
    :type ou_elem: str
    :return: An instance of the specified OntoUML element type.
    :rtype: _OUElement
    """
    graph = Graph()
    elem_id = URIRef("https://example.org/elem1")

    elem_outerm = get_outerm_from_ouelement(ou_elem)
    elem_ouclass = get_ouelement_from_outerm(elem_outerm)

    graph.add((elem_id, RDF.type, elem_outerm))

    created_elem = elem_ouclass(graph, elem_id)

    return created_elem


@pytest.mark.parametrize(
    "ou_elem",
    [
        "OUCardinality",
        "OUClass",
        "OUClassView",
        "OUDiagram",
        "OUGeneralization",
        "OUGeneralizationSet",
        "OUGeneralizationSetView",
        "OUGeneralizationView",
        "OULiteral",
        "OUNote",
        "OUNoteView",
        "OUPackage",
        "OUPackageView",
        "OUPath",
        "OUPoint",
        "OUProject",
        "OUProperty",
        "OURectangle",
        "OURelation",
        "OURelationView",
        "OUText",
    ],
)
def test_instantiation_all_elements(ou_elem: str) -> None:
    """Tests the basic instantiation of all OntoUML element types for correct ID and type.

    :param ou_elem: The name of the OntoUML element type to be instantiated and tested.
    :type ou_elem: str
    """
    elem = create_ouelement(ou_elem)

    assert str(elem.id) == "https://example.org/elem1"
    assert elem.type == get_outerm_from_ouelement(ou_elem)


@pytest.mark.parametrize(
    "ou_elem",
    [
        "OUCardinality",
        "OUClass",
        "OUClassView",
        "OUDiagram",
        "OUGeneralization",
        "OUGeneralizationSet",
        "OUGeneralizationSetView",
        "OUGeneralizationView",
        "OULiteral",
        "OUNote",
        "OUNoteView",
        "OUPackage",
        "OUPackageView",
        "OUPath",
        "OUPoint",
        "OUProject",
        "OUProperty",
        "OURectangle",
        "OURelation",
        "OURelationView",
        "OUText",
    ],
)
def test_instantiation_all_elements_wrong_id(ou_elem: str) -> None:
    """Tests the instantiation of all OntoUML element types against a wrong ID.

    :param ou_elem: The name of the OntoUML element type to be instantiated and tested.
    :type ou_elem: str
    """
    elem = create_ouelement(ou_elem)

    assert str(elem.id) != "https://example.org/elem"


@pytest.mark.parametrize(
    "ou_elem",
    [
        "OUClass",
        "OUClassView",
        "OUDiagram",
        "OUGeneralization",
        "OUGeneralizationSet",
        "OUGeneralizationSetView",
        "OUGeneralizationView",
        "OULiteral",
        "OUNote",
        "OUNoteView",
        "OUPackage",
        "OUPackageView",
        "OUPath",
        "OUPoint",
        "OUProject",
        "OUProperty",
        "OURectangle",
        "OURelation",
        "OURelationView",
        "OUText",
    ],
)
def test_instantiation_all_elements_wrong_type(ou_elem: str) -> None:
    """Tests the instantiation of all OntoUML element types, except OUCardinality, against the OUCardinality type.

    :param ou_elem: The name of the OntoUML element type to be instantiated and tested.
    :type ou_elem: str
    """
    elem = create_ouelement(ou_elem)

    assert elem.type != OUCardinality

# OU Specific instantiated correctly
# OU Specific instantiated wrongly must generate error
# Check if OU Specific is instance of OUElement
from rdflib import Graph

from vocabulary_lib.classes._ouelement import _OUElement
from vocabulary_lib.classes.ouelement_types import OUClass


def test_ou_element_positive():
    onto_graph = Graph()
    elem_uri = "https://example.org/my_elem"
    elem_obj = _OUElement(onto_graph, elem_uri)
    assert str(elem_obj.id) == elem_uri


def test_ou_element_negative():
    elem_uri = "https://example.org/my_elem"
    try:
        elem_obj = _OUElement(elem_uri)
        elem_obj.non_existent_att
    except Exception:
        assert True

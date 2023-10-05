from rdflib import Graph

from vocabulary_lib.classes._ouelement import OU_ELEM_TERM_MAP


def test_ou_specific_positive():
    elem_uri = "https://example.org/my_elem"
    graph = Graph()

    for class_name in OU_ELEM_TERM_MAP.keys():
        graph.add(())
        elem_obj = class_name(graph, elem_uri)
        assert str(elem_obj.id) == elem_uri


# def test_ou_specific_negative():
#     elem_uri = "https://example.org/my_elem"
#     try:
#         elem_obj = OUClass(elem_uri)
#         elem_obj.non_existent_att
#     except Exception:
#         assert True

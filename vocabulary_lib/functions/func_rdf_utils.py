from rdflib import Graph, URIRef


def create_list_subjects(graph: Graph, graph_predicate: URIRef, graph_object: URIRef) -> list[URIRef]:
    return_list = []

    for element in graph.subjects(graph_predicate, graph_object):
        return_list.append(element)

    return return_list


def create_list_predicates(graph: Graph, graph_subject: URIRef, graph_object: URIRef) -> list[URIRef]:
    return_list = []

    for element in graph.predicates(graph_subject, graph_object):
        return_list.append(element)

    return return_list


def create_list_objects(graph: Graph, graph_subject: URIRef, graph_predicate: URIRef) -> list[URIRef]:
    return_list = []

    for element in graph.objects(graph_subject, graph_predicate):
        return_list.append(element)

    return return_list

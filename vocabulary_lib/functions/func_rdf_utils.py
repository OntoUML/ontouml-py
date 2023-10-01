from rdflib import Graph, URIRef


def create_list_subjects(graph: Graph, predicate: URIRef, object: URIRef) -> list[URIRef]:
    return_list = []

    for element in graph.subjects(predicate, object):
        return_list.append(element)

    return return_list


def create_list_predicates(graph: Graph, subject: URIRef, object: URIRef) -> list[URIRef]:
    return_list = []

    for element in graph.predicates(subject, object):
        return_list.append(element)

    return return_list


def create_list_objects(graph: Graph, subject: URIRef, predicate: URIRef) -> list[URIRef]:
    return_list = []

    for element in graph.objects(subject, predicate):
        return_list.append(element)

    return return_list

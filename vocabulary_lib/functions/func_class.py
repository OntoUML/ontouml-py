from rdflib import Graph, URIRef

from vocabulary_lib.classes.class_term import OUTerm


def ou_get_direct_superclasses(ontouml_graph: Graph, ontouml_class: URIRef) -> list[URIRef]:
    """Retrieve direct superclasses of a specified OntoUML class from a given OntoUML RDF graph.

    Allows the user to specify a list of restricted types.
    Superclasses of those types will not be included in the returned list.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve superclasses.
    :type ontouml_class: str
    :return: A list of URIRefs representing the direct superclasses of the specified OntoUML class. The list may be empty.
    :rtype: list[URIRef]
    """
    superclasses: list[URIRef] = []

    for gen in ontouml_graph.subjects(OUTerm.specific, ontouml_class):
        for superclass in ontouml_graph.objects(gen, OUTerm.general):
            superclasses.append(superclass)

    return superclasses


def ou_get_direct_subclasses(ontouml_graph: Graph, ontouml_class: URIRef) -> list[URIRef]:
    """Retrieve direct subclasses of a specified OntoUML class from a given OntoUML RDF graph.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve subclasses.
    :type ontouml_class: str
    :return: A list of URIRefs representing the direct subclasses of the specified OntoUML class.
    :rtype: list[URIRef]
    """
    subclasses: list[URIRef] = []

    for gen in ontouml_graph.subjects(OUTerm.general, ontouml_class):
        for subclass in ontouml_graph.objects(gen, OUTerm.specific):
            subclasses.append(subclass)

    return subclasses


def ou_get_all_superclasses(ontouml_graph: Graph, ontouml_class: URIRef) -> list[URIRef]:
    """Retrieve all (direct and indirect) superclasses of a specified OntoUML class from a given OntoUML RDF graph.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve superclasses.
    :type ontouml_class: URIRef
    :return: A list of URIRefs representing the direct superclasses of the specified OntoUML class.
    :rtype: list[URIRef]
    """
    direct_super = ou_get_direct_superclasses(ontouml_graph, ontouml_class)
    all_superclasses = []
    all_superclasses.extend(direct_super)

    for superclass in direct_super:
        sub_direct = ou_get_direct_superclasses(ontouml_graph, superclass)
        all_superclasses.extend(sub_direct)

    return all_superclasses


def ou_get_all_subclasses(ontouml_graph: Graph, ontouml_class: URIRef) -> list[URIRef]:
    """Retrieve all (direct and indirect) subclasses of a specified OntoUML class from a given OntoUML RDF graph.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve subclasses.
    :type ontouml_class: URIRef
    :return: A list of URIRefs representing the direct subclasses of the specified OntoUML class.
    :rtype: list[URIRef]
    """
    direct_sub = ou_get_direct_subclasses(ontouml_graph, ontouml_class)
    all_subclasses = []
    all_subclasses.extend(direct_sub)

    for subclass in direct_sub:
        sub_direct = ou_get_direct_subclasses(ontouml_graph, subclass)
        all_subclasses.extend(sub_direct)

    return all_subclasses

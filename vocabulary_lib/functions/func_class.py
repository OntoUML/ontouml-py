from rdflib import Graph, URIRef

from vocabulary_lib.classes.outerm import OUTerm


def ou_get_direct_superclasses(ontouml_graph: Graph, ou_class_id: URIRef) -> list[URIRef]:
    """Retrieve a list of IDs (as URIRefs) of the direct superclasses of a specified OntoUML class from a \
    given OntoUML RDF graph.

    Allows the user to specify a list of restricted types.
    Superclasses of those types will not be included in the returned list.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: rdflib.Graph
    :param ou_class_id: The URI of the OntoUML class for which to retrieve superclasses.
    :type ou_class_id: str
    :return: A list of URIRefs representing the direct superclasses of the specified OntoUML class. The list \
    may be empty.
    :rtype: list[URIRef]
    """
    superclasses: list[URIRef] = []

    for gen in ontouml_graph.subjects(OUTerm.specific, ou_class_id):
        for superclass in ontouml_graph.objects(gen, OUTerm.general):
            superclasses.append(superclass)

    return superclasses


def ou_get_direct_subclasses(ontouml_graph: Graph, ou_class_id: URIRef) -> list[URIRef]:
    """Retrieve a list of IDs (as URIRefs) of the direct subclasses of a specified OntoUML class from a given \
    OntoUML RDF graph.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: rdflib.Graph
    :param ou_class_id: The URI of the OntoUML class for which to retrieve subclasses.
    :type ou_class_id: str
    :return: A list of URIRefs representing the direct subclasses of the specified OntoUML class.
    :rtype: list[URIRef]
    """
    subclasses: list[URIRef] = []

    for gen in ontouml_graph.subjects(OUTerm.general, ou_class_id):
        for subclass in ontouml_graph.objects(gen, OUTerm.specific):
            subclasses.append(subclass)

    return subclasses


def ou_get_all_superclasses(ontouml_graph: Graph, ou_class_id: URIRef) -> list[URIRef]:
    """Retrieve a list of IDs (as URIRefs) of the all (direct and indirect) superclasses of a specified OntoUML \
    class from a given OntoUML RDF graph.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: Graph
    :param ou_class_id: The URI of the OntoUML class for which to retrieve superclasses.
    :type ou_class_id: URIRef
    :return: A list of URIRefs representing the direct superclasses of the specified OntoUML class.
    :rtype: list[URIRef]
    """
    direct_super = ou_get_direct_superclasses(ontouml_graph, ou_class_id)
    all_superclasses = []
    all_superclasses.extend(direct_super)

    for superclass in direct_super:
        sub_direct = ou_get_direct_superclasses(ontouml_graph, superclass)
        all_superclasses.extend(sub_direct)

    return all_superclasses


def ou_get_all_subclasses(ontouml_graph: Graph, ou_class_id: URIRef) -> list[URIRef]:
    """Retrieve a list of IDs (as URIRefs) of the all (direct and indirect) subclasses of a specified OntoUML \
    class from a given OntoUML RDF graph.

    :param ontouml_graph: The RDF graph containing OntoUML model data.
    :type ontouml_graph: rdflib.Graph
    :param ou_class_id: The URI of the OntoUML class for which to retrieve subclasses.
    :type ou_class_id: URIRef
    :return: A list of URIRefs representing the direct subclasses of the specified OntoUML class.
    :rtype: list[URIRef]
    """
    direct_sub = ou_get_direct_subclasses(ontouml_graph, ou_class_id)
    all_subclasses = []
    all_subclasses.extend(direct_sub)

    for subclass in direct_sub:
        sub_direct = ou_get_direct_subclasses(ontouml_graph, subclass)
        all_subclasses.extend(sub_direct)

    return all_subclasses


def ou_create_list_classes_sts(ontouml_graph: Graph, include_st: URIRef | list[URIRef]) -> list[URIRef]:
    list_classes_st = []

    # Case a single stereotype is received as argument
    if type(include_st) is str:
        list_stereotypes = [include_st]

    for stereotype in list_stereotypes:
        for ou_class in ontouml_graph.subjects(None, OUTerm.stereotype, stereotype):
            list_classes_st.append(ou_class)

    return list_classes_st

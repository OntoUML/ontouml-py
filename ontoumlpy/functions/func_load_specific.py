from ontoumlpy.classes._ouelement import (
    _OUElement,
    OUCardinality,
    OUClass,
    OUClassView,
    OUDiagram,
    OUGeneralization,
    OUGeneralizationSet,
    OUGeneralizationSetView,
    OUGeneralizationView,
    OULiteral,
    OUNote,
    OUNoteView,
    OUPackage,
    OUPackageView,
    OUPath,
    OUPoint,
    OUProject,
    OUProperty,
    OURectangle,
    OURelation,
    OURelationView,
    OUText,
)
from ontoumlpy.classes.outerm import OUTerm
from rdflib import Graph, RDF, URIRef


class InvalidOntoUMLTypeException(Exception):
    """Exception raised when an individual is not from a valid OntoUML type."""

    pass


def create_ouelement(ontouml_graph: Graph, individual_id: URIRef) -> _OUElement:
    map_type_element = {
        OUTerm.Cardinality: OUCardinality,
        OUTerm.Class: OUClass,
        OUTerm.ClassView: OUClassView,
        OUTerm.Diagram: OUDiagram,
        OUTerm.Generalization: OUGeneralization,
        OUTerm.GeneralizationSet: OUGeneralizationSet,
        OUTerm.GeneralizationSetView: OUGeneralizationSetView,
        OUTerm.GeneralizationView: OUGeneralizationView,
        OUTerm.Literal: OULiteral,
        OUTerm.Note: OUNote,
        OUTerm.NoteView: OUNoteView,
        OUTerm.Package: OUPackage,
        OUTerm.PackageView: OUPackageView,
        OUTerm.Path: OUPath,
        OUTerm.Point: OUPoint,
        OUTerm.Project: OUProject,
        OUTerm.Property: OUProperty,
        OUTerm.Rectangle: OURectangle,
        OUTerm.Relation: OURelation,
        OUTerm.RelationView: OURelationView,
        OUTerm.Text: OUText,
    }

    individual_type = ontouml_graph.value(individual_id, RDF.type)
    if individual_type in map_type_element.keys():
        individual_obj = map_type_element[individual_type](individual_id)
    else:
        raise InvalidOntoUMLTypeException("Individual is not from valid OntoUML type.")
    return individual_obj


def create_list_uriref(ontouml_graph: Graph, object_type: URIRef) -> list[URIRef]:
    return_list = []
    for element in ontouml_graph.subjects(RDF.type, object_type):
        return_list.append(element)
    return return_list


def create_list_ouelement_from_graph(ontouml_graph: Graph, object_type: URIRef) -> list[_OUElement]:
    return_list = []

    for element in ontouml_graph.subjects(RDF.type, object_type):
        element_obj = create_ouelement(ontouml_graph, element)
        return_list.append(element_obj)
    return return_list

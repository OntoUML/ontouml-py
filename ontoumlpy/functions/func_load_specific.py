from rdflib import Graph, RDF, URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouelement.oucardinality import OUCardinality
from ontoumlpy.classes.ouelement.oudiagram import OUDiagram
from ontoumlpy.classes.ouelement.oudiagramelement.ouelementview.ouconnectorview.ougeneralizationview import (
    OUGeneralizationView,
)
from ontoumlpy.classes.ouelement.oudiagramelement.ouelementview.ouconnectorview.ourelationview import OURelationView
from ontoumlpy.classes.ouelement.oudiagramelement.ouelementview.ougeneralizationsetview import OUGeneralizationSetView
from ontoumlpy.classes.ouelement.oudiagramelement.ouelementview.ounodeview.ouclassview import OUClassView
from ontoumlpy.classes.ouelement.oudiagramelement.ouelementview.ounodeview.ounoteview import OUNoteView
from ontoumlpy.classes.ouelement.oudiagramelement.ouelementview.ounodeview.oupackageview import OUPackageView
from ontoumlpy.classes.ouelement.oudiagramelement.shape.oupath import OUPath
from ontoumlpy.classes.ouelement.oudiagramelement.shape.ourectangularshape.ourectangle import OURectangle
from ontoumlpy.classes.ouelement.oudiagramelement.shape.ourectangularshape.outext import OUText
from ontoumlpy.classes.ouelement.oumodelelement.ouclassifier.ouclass import OUClass
from ontoumlpy.classes.ouelement.oumodelelement.ouclassifier.ourelation import OURelation
from ontoumlpy.classes.ouelement.oumodelelement.ougeneralization import OUGeneralization
from ontoumlpy.classes.ouelement.oumodelelement.ougeneralizationset import OUGeneralizationSet
from ontoumlpy.classes.ouelement.oumodelelement.ouliteral import OULiteral
from ontoumlpy.classes.ouelement.oumodelelement.ounote import OUNote
from ontoumlpy.classes.ouelement.oumodelelement.oupackage import OUPackage
from ontoumlpy.classes.ouelement.oumodelelement.ouproperty import OUProperty
from ontoumlpy.classes.ouelement.oupoint import OUPoint
from ontoumlpy.classes.ouelement.ouproject import OUProject


class InvalidOntoUMLTypeException(Exception):
    """Exception raised when an individual is not from a valid OntoUML type."""

    pass


def create_ouelement(individual_id: URIRef, individual_type: URIRef) -> _OUElement:
    map_type_element = {
        OntoUML.Cardinality: OUCardinality,
        OntoUML.Class: OUClass,
        OntoUML.ClassView: OUClassView,
        OntoUML.Diagram: OUDiagram,
        OntoUML.Generalization: OUGeneralization,
        OntoUML.GeneralizationSet: OUGeneralizationSet,
        OntoUML.GeneralizationSetView: OUGeneralizationSetView,
        OntoUML.GeneralizationView: OUGeneralizationView,
        OntoUML.Literal: OULiteral,
        OntoUML.Note: OUNote,
        OntoUML.NoteView: OUNoteView,
        OntoUML.Package: OUPackage,
        OntoUML.PackageView: OUPackageView,
        OntoUML.Path: OUPath,
        OntoUML.Point: OUPoint,
        OntoUML.Project: OUProject,
        OntoUML.Property: OUProperty,
        OntoUML.Rectangle: OURectangle,
        OntoUML.Relation: OURelation,
        OntoUML.RelationView: OURelationView,
        OntoUML.Text: OUText,
    }

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

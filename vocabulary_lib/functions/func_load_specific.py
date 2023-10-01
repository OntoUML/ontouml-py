from rdflib import Graph, RDF

from vocabulary_lib.classes.class_elements import (
    OUCardinality,
    OUClass,
    OUClassView,
    OUDiagram,
    OUGeneralization,
    OUGeneralizationSet,
    OUGeneralizationView,
    OUGeneralizationSetView,
    OUNote,
    OUPackage,
    OUPath,
    OUPoint,
    OUProject,
    OUProperty,
    OURectangle,
    OURelation,
    OURelationView,
    OUText,
    OUNoteView,
)
from vocabulary_lib.classes.class_term import OUTerm
from vocabulary_lib.functions.func_rdf_utils import create_list_subjects


def create_list_ou_cardinality(ontouml_graph: Graph) -> list[OUCardinality]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Cardinality)
    for element in all_elements:
        element_obj = OUCardinality(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_class(ontouml_graph: Graph) -> list[OUClass]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Class)
    for element in all_elements:
        element_obj = OUClass(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_classview(ontouml_graph: Graph) -> list[OUClassView]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.ClassView)
    for element in all_elements:
        element_obj = OUClassView(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_diagram(ontouml_graph: Graph) -> list[OUDiagram]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Diagram)
    for element in all_elements:
        element_obj = OUDiagram(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_generalization(ontouml_graph: Graph) -> list[OUGeneralization]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Generalization)
    for element in all_elements:
        element_obj = OUGeneralization(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_generalizationset(ontouml_graph: Graph) -> list[OUGeneralizationSet]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.GeneralizationSet)
    for element in all_elements:
        element_obj = OUGeneralizationSet(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_generalizationsetview(ontouml_graph: Graph) -> list[OUGeneralizationSetView]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.GeneralizationSetView)
    for element in all_elements:
        element_obj = OUGeneralizationSetView(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_generalizationview(ontouml_graph: Graph) -> list[OUGeneralizationView]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.GeneralizationView)
    for element in all_elements:
        element_obj = OUGeneralizationView(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_note(ontouml_graph: Graph) -> list[OUNote]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Note)
    for element in all_elements:
        element_obj = OUNote(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_noteview(ontouml_graph: Graph) -> list[OUNoteView]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.NoteView)
    for element in all_elements:
        element_obj = OUNoteView(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_package(ontouml_graph: Graph) -> list[OUPackage]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Package)
    for element in all_elements:
        element_obj = OUPackage(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_path(ontouml_graph: Graph) -> list[OUPath]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Path)
    for element in all_elements:
        element_obj = OUPath(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_point(ontouml_graph: Graph) -> list[OUPoint]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Point)
    for element in all_elements:
        element_obj = OUPoint(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_project(ontouml_graph: Graph) -> list[OUProject]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Project)
    for element in all_elements:
        element_obj = OUProject(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_property(ontouml_graph: Graph) -> list[OUProperty]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Property)
    for element in all_elements:
        element_obj = OUProperty(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_rectangle(ontouml_graph: Graph) -> list[OURectangle]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Rectangle)
    for element in all_elements:
        element_obj = OURectangle(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_relation(ontouml_graph: Graph) -> list[OURelation]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Relation)
    for element in all_elements:
        element_obj = OURelation(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_relationview(ontouml_graph: Graph) -> list[OURelationView]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.RelationView)
    for element in all_elements:
        element_obj = OURelationView(element)
        list_elements.append(element_obj)
    return list_elements


def create_list_ou_text(ontouml_graph: Graph) -> list[OUText]:
    list_elements = []
    all_elements = create_list_subjects(ontouml_graph, RDF.type, OUTerm.Text)
    for element in all_elements:
        element_obj = OUText(element)
        list_elements.append(element_obj)
    return list_elements

from rdflib import Graph

from vocabulary_lib.classes.class_elements import (
    OUCardinality,
    OUClass,
    OUClassView,
    OUDiagram,
    OUGeneralization,
    OUGeneralizationSet,
    OUGeneralizationSetView,
    OUGeneralizationView,
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
from vocabulary_lib.functions.func_load_specific import (
    create_list_ou_cardinality,
    create_list_ou_class,
    create_list_ou_classview,
    create_list_ou_diagram,
    create_list_ou_generalization,
    create_list_ou_generalizationset,
    create_list_ou_generalizationsetview,
    create_list_ou_generalizationview,
    create_list_ou_note,
    create_list_ou_package,
    create_list_ou_path,
    create_list_ou_point,
    create_list_ou_project,
    create_list_ou_property,
    create_list_ou_rectangle,
    create_list_ou_relation,
    create_list_ou_relationview,
    create_list_ou_text,
    create_list_ou_noteview,
)


class OUGraph:
    def __init__(self, ontouml_graph: Graph):
        self.list_OUCardinality: list[OUCardinality] = create_list_ou_cardinality(ontouml_graph)
        self.list_OUClass: list[OUClass] = create_list_ou_class(ontouml_graph)
        self.list_OUClassView: list[OUClassView] = create_list_ou_classview(ontouml_graph)
        self.list_OUDiagram: list[OUDiagram] = create_list_ou_diagram(ontouml_graph)
        self.list_OUGeneralization: list[OUGeneralization] = create_list_ou_generalization(ontouml_graph)
        self.list_OUGeneralizationSet: list[OUGeneralizationSet] = create_list_ou_generalizationset(ontouml_graph)
        self.list_OUGeneralizationSetView: list[OUGeneralizationSetView] = create_list_ou_generalizationsetview(
            ontouml_graph
        )
        self.list_OUGeneralizationView: list[OUGeneralizationView] = create_list_ou_generalizationview(ontouml_graph)
        self.list_OUNote: list[OUNote] = create_list_ou_note(ontouml_graph)
        self.list_OUNoteView: list[OUNoteView] = create_list_ou_noteview(ontouml_graph)
        self.list_OUPackage: list[OUPackage] = create_list_ou_package(ontouml_graph)
        self.list_OUPath: list[OUPath] = create_list_ou_path(ontouml_graph)
        self.list_OUPoint: list[OUPoint] = create_list_ou_point(ontouml_graph)
        self.list_OUProject: list[OUProject] = create_list_ou_project(ontouml_graph)
        self.list_OUProperty: list[OUProperty] = create_list_ou_property(ontouml_graph)
        self.list_OURectangle: list[OURectangle] = create_list_ou_rectangle(ontouml_graph)
        self.list_OURelation: list[OURelation] = create_list_ou_relation(ontouml_graph)
        self.list_OURelationView: list[OURelationView] = create_list_ou_relationview(ontouml_graph)
        self.list_OUText: list[OUText] = create_list_ou_text(ontouml_graph)

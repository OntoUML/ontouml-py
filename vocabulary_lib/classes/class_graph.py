from loguru import logger
from rdflib import Graph, RDF

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
    OULiteral,
)
from vocabulary_lib.classes.class_term import OUTerm


class OUGraph:
    def __init__(self, ontouml_graph: Graph):
        self.list_OUCardinality = []
        self.list_OUClass = []
        self.list_OUClassView = []
        self.list_OUDiagram = []
        self.list_OUGeneralization = []
        self.list_OUGeneralizationSet = []
        self.list_OUGeneralizationSetView = []
        self.list_OUGeneralizationView = []
        self.list_OULiteral = []
        self.list_OUNote = []
        self.list_OUNoteView = []
        self.list_OUPackage = []
        self.list_OUPath = []
        self.list_OUPoint = []
        self.list_OUProject = []
        self.list_OUProperty = []
        self.list_OURectangle = []
        self.list_OURelation = []
        self.list_OURelationView = []
        self.list_OUText = []

        for s, _, o in ontouml_graph.triples((None, RDF.type, None)):
            if o == OUTerm.Cardinality:
                self.list_OUCardinality.append(OUCardinality(ontouml_graph, s))
            elif o == OUTerm.Class:
                self.list_OUClass.append(OUClass(ontouml_graph, s))
            elif o == OUTerm.ClassView:
                self.list_OUClassView.append(OUClassView(ontouml_graph, s))
            elif o == OUTerm.Diagram:
                self.list_OUDiagram.append(OUDiagram(ontouml_graph, s))
            elif o == OUTerm.Generalization:
                self.list_OUGeneralization.append(OUGeneralization(ontouml_graph, s))
            elif o == OUTerm.GeneralizationSet:
                self.list_OUGeneralizationSet.append(OUGeneralizationSet(ontouml_graph, s))
            elif o == OUTerm.GeneralizationSetView:
                self.list_OUGeneralizationSetView.append(OUGeneralizationSetView(ontouml_graph, s))
            elif o == OUTerm.GeneralizationView:
                self.list_OUGeneralizationView.append(OUGeneralizationView(ontouml_graph, s))
            elif o == OUTerm.Literal:
                self.list_OULiteral.append(OULiteral(ontouml_graph, s))
            elif o == OUTerm.Note:
                self.list_OUNote.append(OUNote(ontouml_graph, s))
            elif o == OUTerm.NoteView:
                self.list_OUNoteView.append(OUNoteView(ontouml_graph, s))
            elif o == OUTerm.Package:
                self.list_OUPackage.append(OUPackage(ontouml_graph, s))
            elif o == OUTerm.Path:
                self.list_OUPath.append(OUPath(ontouml_graph, s))
            elif o == OUTerm.Point:
                self.list_OUPoint.append(OUPoint(ontouml_graph, s))
            elif o == OUTerm.Project:
                self.list_OUProject.append(OUProject(ontouml_graph, s))
            elif o == OUTerm.Property:
                self.list_OUProperty.append(OUProperty(ontouml_graph, s))
            elif o == OUTerm.Rectangle:
                self.list_OURectangle.append(OURectangle(ontouml_graph, s))
            elif o == OUTerm.Relation:
                self.list_OURelation.append(OURelation(ontouml_graph, s))
            elif o == OUTerm.RelationView:
                self.list_OURelationView.append(OURelationView(ontouml_graph, s))
            elif o == OUTerm.Text:
                self.list_OUText.append(OUText(ontouml_graph, s))
            else:
                logger.warning(
                    f"Graph's element {s} of type {o} was not loaded into any OUGraph's list "
                    f"because it is not an OntoUML element."
                )

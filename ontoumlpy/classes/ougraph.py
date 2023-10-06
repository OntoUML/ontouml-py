"""This module provides a Python class, OUGraph, for creating and managing lists of various OntoUML vocabulary elements
based on an RDF graph. It allows users to load OntoUML elements from an RDF graph and organize them into separate lists
for different element types.

The OUGraph class can be used to process OntoUML RDF data and make it accessible for further analysis or manipulation.

Classes:
    - OUGraph: A class for loading OntoUML vocabulary elements from an RDF graph and organizing them into lists.

Usage:
    To use this module, instantiate the OUGraph class with an RDF graph and optionally specify whether to include
    concrete syntax elements. After instantiation, you can access various lists containing OntoUML elements.

Example:
    from rdflib import Graph
    from ontology_vocabulary import OUGraph

    # Load an RDF graph containing OntoUML data
    ontouml_graph = Graph()
    ontouml_graph.parse("ontouml_data.rdf")

    # Instantiate the OUGraph class
    ou_graph = OUGraph(ontouml_graph)

    # Access OntoUML element lists
    class_elements = ou_graph.list_OUClass
    generalization_elements = ou_graph.list_OUGeneralization

    # Process and analyze OntoUML data"""
from loguru import logger
from rdflib import Graph, RDF

from ontoumlpy.classes._ouelement import _OUElement
from ontoumlpy.classes.ouelement_types import (
    OUCardinality,
    OUClass,
    OUGeneralization,
    OUGeneralizationSet,
    OULiteral,
    OUNote,
    OUPackage,
    OUProject,
    OUProperty,
    OURelation,
    OUText,
    OUClassView,
    OUDiagram,
    OUGeneralizationSetView,
    OUGeneralizationView,
    OUNoteView,
    OUPath,
    OUPoint,
    OURectangle,
    OURelationView,
)
from ontoumlpy.classes.outerm import OUTerm
from ontoumlpy.functions.func_mappings import get_outerm_from_ouelement


class OUGraph:
    """OntoUML Vocabulary Graph Class.

    This class provides a Python interface for managing OntoUML vocabulary elements based on an RDF graph. It allows you
    to load OntoUML elements from the graph and organize them into separate lists by their types.

    :param ontouml_graph: An RDF graph containing OntoUML vocabulary data.
    :type ontouml_graph: Graph
    :param include_concrete: Flag indicating whether to include concrete syntax elements.
    :type include_concrete: bool, optional

    :ivar list_OUCardinality: A list of OntoUML Cardinality objects.
    :vartype list_OUCardinality: list
    :ivar list_OUClass: A list of OntoUML Class objects.
    :vartype list_OUClass: list
    :ivar list_OUClassView: A list of OntoUML ClassView objects.
    :vartype list_OUClassView: list
    :ivar list_OUDiagram: A list of OntoUML Diagram objects.
    :vartype list_OUDiagram: list
    :ivar list_OUGeneralization: A list of OntoUML Generalization objects.
    :vartype list_OUGeneralization: list
    :ivar list_OUGeneralizationSet: A list of OntoUML GeneralizationSet objects.
    :vartype list_OUGeneralizationSet: list
    :ivar list_OUGeneralizationSetView: A list of OntoUML GeneralizationSetView objects.
    :vartype list_OUGeneralizationSetView: list
    :ivar list_OUGeneralizationView: A list of OntoUML GeneralizationView objects.
    :vartype list_OUGeneralizationView: list
    :ivar list_OULiteral: A list of OntoUML Literal objects.
    :vartype list_OULiteral: list
    :ivar list_OUNote: A list of OntoUML Note objects.
    :vartype list_OUNote: list
    :ivar list_OUNoteView: A list of OntoUML NoteView objects.
    :vartype list_OUNoteView: list
    :ivar list_OUPackage: A list of OntoUML Package objects.
    :vartype list_OUPackage: list
    :ivar list_OUPath: A list of OntoUML Path objects.
    :vartype list_OUPath: list
    :ivar list_OUPoint: A list of OntoUML Point objects.
    :vartype list_OUPoint: list
    :ivar list_OUProject: A list of OntoUML Project objects.
    :vartype list_OUProject: list
    :ivar list_OUProperty: A list of OntoUML Property objects.
    :vartype list_OUProperty: list
    :ivar list_OURectangle: A list of OntoUML Rectangle objects.
    :vartype list_OURectangle: list
    :ivar list_OURelation: A list of OntoUML Relation objects.
    :vartype list_OURelation: list
    :ivar list_OURelationView: A list of OntoUML RelationView objects.
    :vartype list_OURelationView: list
    :ivar list_OUText: A list of OntoUML Text objects.
    :vartype list_OUText: list
    """

    def __init__(self, ontouml_graph: Graph, include_concrete: bool = True) -> None:
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
            # ABSTRACT SYNTAX ELEMENTS
            if o == OUTerm.Cardinality:
                elem = OUCardinality(ontouml_graph, s)
            elif o == OUTerm.Class:
                elem = OUClass(ontouml_graph, s)
            elif o == OUTerm.Generalization:
                elem = OUGeneralization(ontouml_graph, s)
            elif o == OUTerm.GeneralizationSet:
                elem = OUGeneralizationSet(ontouml_graph, s)
            elif o == OUTerm.Literal:
                elem = OULiteral(ontouml_graph, s)
            elif o == OUTerm.Note:
                elem = OUNote(ontouml_graph, s)
            elif o == OUTerm.Package:
                elem = OUPackage(ontouml_graph, s)
            elif o == OUTerm.Project:
                elem = OUProject(ontouml_graph, s)
            elif o == OUTerm.Property:
                elem = OUProperty(ontouml_graph, s)
            elif o == OUTerm.Relation:
                elem = OURelation(ontouml_graph, s)
            elif o == OUTerm.Text:
                elem = OUText(ontouml_graph, s)

            # CONCRETE SYNTAX ELEMENTS
            elif include_concrete:
                if o == OUTerm.ClassView:
                    elem = OUClassView(ontouml_graph, s)
                elif o == OUTerm.Diagram:
                    elem = OUDiagram(ontouml_graph, s)
                elif o == OUTerm.GeneralizationSetView:
                    elem = OUGeneralizationSetView(ontouml_graph, s)
                elif o == OUTerm.GeneralizationView:
                    elem = OUGeneralizationView(ontouml_graph, s)
                elif o == OUTerm.NoteView:
                    elem = OUNoteView(ontouml_graph, s)
                elif o == OUTerm.Path:
                    elem = OUPath(ontouml_graph, s)
                elif o == OUTerm.Point:
                    elem = OUPoint(ontouml_graph, s)
                elif o == OUTerm.Rectangle:
                    elem = OURectangle(ontouml_graph, s)
                elif o == OUTerm.RelationView:
                    elem = OURelationView(ontouml_graph, s)
                else:
                    logger.debug(
                        f"Graph's element {s} of type {o} was not loaded into any OUGraph's list "
                        f"because it is not an OntoUML element."
                    )
            else:
                logger.debug(
                    f"Graph's element {s} of type {o} was not loaded into any OUGraph's list "
                    f"because it is part of the OntoUML's concrete syntax or it is not an OntoUML element."
                )

            if elem is not None:
                self.add_element(elem, include_concrete)

    def update(self, ontouml_graph: Graph, include_concrete: bool = False) -> None:
        """Calls the __init__ method to re-initialize the OUGraph instance with the new parameters.

        :param ontouml_graph: An RDF graph containing OntoUML vocabulary data.
        :type ontouml_graph: Graph
        :param include_concrete: Flag indicating whether to include concrete syntax elements.
        :type include_concrete: bool, optional
        """
        self.__init__(ontouml_graph, include_concrete)

    def add_element(self, element: _OUElement, include_concrete: bool = False) -> None:
        term = get_outerm_from_ouelement(element)

        # ABSTRACT SYNTAX ELEMENTS
        if term == OUTerm.Cardinality:
            self.list_OUCardinality.append(element)
        elif term == OUTerm.Class:
            self.list_OUClass.append(element)
        elif term == OUTerm.Generalization:
            self.list_OUGeneralization.append(element)
        elif term == OUTerm.GeneralizationSet:
            self.list_OUGeneralizationSet.append(element)
        elif term == OUTerm.Literal:
            self.list_OULiteral.append(element)
        elif term == OUTerm.Note:
            self.list_OUNote.append(element)
        elif term == OUTerm.Package:
            self.list_OUPackage.append(element)
        elif term == OUTerm.Project:
            self.list_OUProject.append(element)
        elif term == OUTerm.Property:
            self.list_OUProperty.append(element)
        elif term == OUTerm.Relation:
            self.list_OURelation.append(element)
        elif term == OUTerm.Text:
            self.list_OUText.append(element)

        # CONCRETE SYNTAX ELEMENTS
        elif include_concrete:
            if term == OUTerm.ClassView:
                self.list_OUClassView.append(element)
            elif term == OUTerm.Diagram:
                self.list_OUDiagram.append(element)
            elif term == OUTerm.GeneralizationSetView:
                self.list_OUGeneralizationSetView.append(element)
            elif term == OUTerm.GeneralizationView:
                self.list_OUGeneralizationView.append(element)
            elif term == OUTerm.NoteView:
                self.list_OUNoteView.append(element)
            elif term == OUTerm.Path:
                self.list_OUPath.append(element)
            elif term == OUTerm.Point:
                self.list_OUPoint.append(element)
            elif term == OUTerm.Rectangle:
                self.list_OURectangle.append(element)
            elif term == OUTerm.RelationView:
                self.list_OURelationView.append(element)
            else:
                logger.debug(
                    f"Graph'element element {element} of type {term} was not loaded into any OUGraph'element list "
                    f"because it is not an OntoUML element."
                )
        else:
            logger.debug(
                f"Graph'element element {element} of type {term} was not loaded into any OUGraph'element list "
                f"because it is part of the OntoUML'element concrete syntax or it is not an OntoUML element."
            )

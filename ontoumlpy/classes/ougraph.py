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
    class_elements = ou_graph.all_OUClass
    generalization_elements = ou_graph.all_OUGeneralization

    # Process and analyze OntoUML data"""
from loguru import logger
from rdflib import Graph, RDF

from ontoumlpy.classes._ouelement import _OUElement
from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.functions.func_mappings import get_outerm_from_ouelement, get_ouelement_from_outerm


class OUGraph:
    """OntoUML Vocabulary Graph Class.

    This class provides a Python interface for managing OntoUML vocabulary elements based on an RDF graph. It allows you
    to load OntoUML elements from the graph and organize them into separate lists by their types.

    :param ontouml_graph: An RDF graph containing OntoUML vocabulary data.
    :type ontouml_graph: Graph
    :param include_concrete: Flag indicating whether to include concrete syntax elements.
    :type include_concrete: bool, optional

    :ivar all_OUCardinality: A list of OntoUML Cardinality objects.
    :vartype all_OUCardinality: list
    :ivar all_OUClass: A list of OntoUML Class objects.
    :vartype all_OUClass: list
    :ivar all_OUClassView: A list of OntoUML ClassView objects.
    :vartype all_OUClassView: list
    :ivar all_OUDiagram: A list of OntoUML Diagram objects.
    :vartype all_OUDiagram: list
    :ivar all_OUGeneralization: A list of OntoUML Generalization objects.
    :vartype all_OUGeneralization: list
    :ivar all_OUGeneralizationSet: A list of OntoUML GeneralizationSet objects.
    :vartype all_OUGeneralizationSet: list
    :ivar all_OUGeneralizationSetView: A list of OntoUML GeneralizationSetView objects.
    :vartype all_OUGeneralizationSetView: list
    :ivar all_OUGeneralizationView: A list of OntoUML GeneralizationView objects.
    :vartype all_OUGeneralizationView: list
    :ivar all_OULiteral: A list of OntoUML Literal objects.
    :vartype all_OULiteral: list
    :ivar all_OUNote: A list of OntoUML Note objects.
    :vartype all_OUNote: list
    :ivar all_OUNoteView: A list of OntoUML NoteView objects.
    :vartype all_OUNoteView: list
    :ivar all_OUPackage: A list of OntoUML Package objects.
    :vartype all_OUPackage: list
    :ivar all_OUPath: A list of OntoUML Path objects.
    :vartype all_OUPath: list
    :ivar all_OUPoint: A list of OntoUML Point objects.
    :vartype all_OUPoint: list
    :ivar all_OUProject: A list of OntoUML Project objects.
    :vartype all_OUProject: list
    :ivar all_OUProperty: A list of OntoUML Property objects.
    :vartype all_OUProperty: list
    :ivar all_OURectangle: A list of OntoUML Rectangle objects.
    :vartype all_OURectangle: list
    :ivar all_OURelation: A list of OntoUML Relation objects.
    :vartype all_OURelation: list
    :ivar all_OURelationView: A list of OntoUML RelationView objects.
    :vartype all_OURelationView: list
    :ivar all_OUText: A list of OntoUML Text objects.
    :vartype all_OUText: list
    """

    def __init__(self, ontouml_graph: Graph, include_concrete: bool = True) -> None:
        self.all_OUCardinality = []
        self.all_OUClass = []
        self.all_OUClassView = []
        self.all_OUDiagram = []
        self.all_OUGeneralization = []
        self.all_OUGeneralizationSet = []
        self.all_OUGeneralizationSetView = []
        self.all_OUGeneralizationView = []
        self.all_OULiteral = []
        self.all_OUNote = []
        self.all_OUNoteView = []
        self.all_OUPackage = []
        self.all_OUPath = []
        self.all_OUPoint = []
        self.all_OUProject = []
        self.all_OUProperty = []
        self.all_OURectangle = []
        self.all_OURelation = []
        self.all_OURelationView = []
        self.all_OUText = []

        for s, _, o in ontouml_graph.triples((None, RDF.type, None)):
            # ABSTRACT SYNTAX ELEMENTS

            elem_type = get_ouelement_from_outerm(o)

            # TODO(@pedropaulofb): create list of syntax elements (Conc vs Abst) and filter before attributing type.

            if elem_type in list_abstract_types:
                elem_inst = elem_type(ontouml_graph, s)
                self.add_element(elem_inst)
            elif elem_type in list_concrete_types:
                if include_concrete:
                    elem_inst = elem_type(ontouml_graph, s)
                    self.add_element(elem_inst)
                else:
                    logger.debug(f"Graph's element {s} of type {o} was not loaded into any OUGraph's list "
                                 f"because it is not an OntoUML element.")
            else:
                logger.debug(f"Graph's element {s} of type {o} was not loaded into any OUGraph's list "
                             f"because it is part of the OntoUML's concrete syntax or it is not an OntoUML element.")

    def update(self, ontouml_graph: Graph, include_concrete: bool = False) -> None:
        """Calls the __init__ method to re-initialize the OUGraph instance with the new parameters.

        :param ontouml_graph: An RDF graph containing OntoUML vocabulary data.
        :type ontouml_graph: Graph
        :param include_concrete: Flag indicating whether to include concrete syntax elements.
        :type include_concrete: bool, optional
        """
        self.__init__(ontouml_graph, include_concrete)

    def add_element(self, element: _OUElement) -> None:
        term = get_outerm_from_ouelement(element)

        # ABSTRACT SYNTAX ELEMENTS
        if term == OntoUML.Cardinality:
            self.all_OUCardinality.append(element)
        elif term == OntoUML.Class:
            self.all_OUClass.append(element)
        elif term == OntoUML.Generalization:
            self.all_OUGeneralization.append(element)
        elif term == OntoUML.GeneralizationSet:
            self.all_OUGeneralizationSet.append(element)
        elif term == OntoUML.Literal:
            self.all_OULiteral.append(element)
        elif term == OntoUML.Note:
            self.all_OUNote.append(element)
        elif term == OntoUML.Package:
            self.all_OUPackage.append(element)
        elif term == OntoUML.Project:
            self.all_OUProject.append(element)
        elif term == OntoUML.Property:
            self.all_OUProperty.append(element)
        elif term == OntoUML.Relation:
            self.all_OURelation.append(element)
        elif term == OntoUML.Text:
            self.all_OUText.append(element)

        # CONCRETE SYNTAX ELEMENTS
        elif include_concrete:
            if term == OntoUML.ClassView:
                self.all_OUClassView.append(element)
            elif term == OntoUML.Diagram:
                self.all_OUDiagram.append(element)
            elif term == OntoUML.GeneralizationSetView:
                self.all_OUGeneralizationSetView.append(element)
            elif term == OntoUML.GeneralizationView:
                self.all_OUGeneralizationView.append(element)
            elif term == OntoUML.NoteView:
                self.all_OUNoteView.append(element)
            elif term == OntoUML.Path:
                self.all_OUPath.append(element)
            elif term == OntoUML.Point:
                self.all_OUPoint.append(element)
            elif term == OntoUML.Rectangle:
                self.all_OURectangle.append(element)
            elif term == OntoUML.RelationView:
                self.all_OURelationView.append(element)

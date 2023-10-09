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
    class_elements = ou_graph.OUClass
    generalization_elements = ou_graph.OUGeneralization

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

    :ivar OUCardinality_list: A list of OntoUML Cardinality objects.
    :vartype OUCardinality_list: list
    :ivar OUClass_list: A list of OntoUML Class objects.
    :vartype OUClass_list: list
    :ivar OUClassView_list: A list of OntoUML ClassView objects.
    :vartype OUClassView_list: list
    :ivar OUDiagram_list: A list of OntoUML Diagram objects.
    :vartype OUDiagram_list: list
    :ivar OUGeneralization_list: A list of OntoUML Generalization objects.
    :vartype OUGeneralization_list: list
    :ivar OUGeneralizationSet_list: A list of OntoUML GeneralizationSet objects.
    :vartype OUGeneralizationSet_list: list
    :ivar OUGeneralizationSetView_list: A list of OntoUML GeneralizationSetView objects.
    :vartype OUGeneralizationSetView_list: list
    :ivar OUGeneralizationView_list: A list of OntoUML GeneralizationView objects.
    :vartype OUGeneralizationView_list: list
    :ivar OULiteral_list: A list of OntoUML Literal objects.
    :vartype OULiteral_list: list
    :ivar OUNote_list: A list of OntoUML Note objects.
    :vartype OUNote_list: list
    :ivar OUNoteView_list: A list of OntoUML NoteView objects.
    :vartype OUNoteView_list: list
    :ivar OUPackage_list: A list of OntoUML Package objects.
    :vartype OUPackage_list: list
    :ivar OUPath_list: A list of OntoUML Path objects.
    :vartype OUPath_list: list
    :ivar OUPoint_list: A list of OntoUML Point objects.
    :vartype OUPoint_list: list
    :ivar OUProject_list: A list of OntoUML Project objects.
    :vartype OUProject_list: list
    :ivar OUProperty_list: A list of OntoUML Property objects.
    :vartype OUProperty_list: list
    :ivar OURectangle_list: A list of OntoUML Rectangle objects.
    :vartype OURectangle_list: list
    :ivar OURelation_list: A list of OntoUML Relation objects.
    :vartype OURelation_list: list
    :ivar OURelationView_list: A list of OntoUML RelationView objects.
    :vartype OURelationView_list: list
    :ivar OUText_list: A list of OntoUML Text objects.
    :vartype OUText_list: list
    """

    def __init__(self, ontouml_graph: Graph, include_concrete: bool = True) -> None:
        self.OUCardinality_list = []
        self.OUClass_list = []
        self.OUClassView_list = []
        self.OUDiagram_list = []
        self.OUGeneralization_list = []
        self.OUGeneralizationSet_list = []
        self.OUGeneralizationSetView_list = []
        self.OUGeneralizationView_list = []
        self.OULiteral_list = []
        self.OUNote_list = []
        self.OUNoteView_list = []
        self.OUPackage_list = []
        self.OUPath_list = []
        self.OUPoint_list = []
        self.OUProject_list = []
        self.OUProperty_list = []
        self.OURectangle_list = []
        self.OURelation_list = []
        self.OURelationView_list = []
        self.OUText_list = []

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
            self.OUCardinality_list.append(element)
        elif term == OntoUML.Class:
            self.OUClass_list.append(element)
        elif term == OntoUML.Generalization:
            self.OUGeneralization_list.append(element)
        elif term == OntoUML.GeneralizationSet:
            self.OUGeneralizationSet_list.append(element)
        elif term == OntoUML.Literal:
            self.OULiteral_list.append(element)
        elif term == OntoUML.Note:
            self.OUNote_list.append(element)
        elif term == OntoUML.Package:
            self.OUPackage_list.append(element)
        elif term == OntoUML.Project:
            self.OUProject_list.append(element)
        elif term == OntoUML.Property:
            self.OUProperty_list.append(element)
        elif term == OntoUML.Relation:
            self.OURelation_list.append(element)
        elif term == OntoUML.Text:
            self.OUText_list.append(element)
        elif term == OntoUML.ClassView:
            self.OUClassView_list.append(element)
        elif term == OntoUML.Diagram:
            self.OUDiagram_list.append(element)
        elif term == OntoUML.GeneralizationSetView:
            self.OUGeneralizationSetView_list.append(element)
        elif term == OntoUML.GeneralizationView:
            self.OUGeneralizationView_list.append(element)
        elif term == OntoUML.NoteView:
            self.OUNoteView_list.append(element)
        elif term == OntoUML.Path:
            self.OUPath_list.append(element)
        elif term == OntoUML.Point:
            self.OUPoint_list.append(element)
        elif term == OntoUML.Rectangle:
            self.OURectangle_list.append(element)
        elif term == OntoUML.RelationView:
            self.OURelationView_list.append(element)

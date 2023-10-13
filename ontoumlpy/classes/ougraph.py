"""This module provides a Python class, OUGraph, for creating and managing lists of various OntoUML vocabulary elements
based on an RDF graph. It allows users to load OntoUML elements from an RDF graph and organize them into separate lists
for different element types.

The OUGraph class can be used to process OntoUML RDF data and make it accessible for further analysis or manipulation.

Classes:
    - OUGraph: A class for loading OntoUML vocabulary elements from an RDF graph and organizing them into lists.

Usage:
    To use this module, instantiate the OUGraph class with an RDF graph and optionally specify whether to include
    concrete syntax elements. After instantiation, you can access various lists containing OntoUML elements.
"""
from loguru import logger
from rdflib import Graph, RDF

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
from ontoumlpy.classes.ouenumeration.enumerations_misc import OUAbstractElements, OUConcreteElements
from ontoumlpy.classes.ouexception import OUInvalidElementType
from ontoumlpy.functions.func_load_specific import ou_create_element


class OUGraph:
    """OntoUML Vocabulary Graph Class.

    This class provides a Python interface for managing OntoUML vocabulary elements based on an RDF graph. It allows you
    to load OntoUML elements from the graph and organize them into separate lists by their types.

    :ivar ou_cardinality_list: A list of OntoUML Cardinality objects.
    :vartype ou_cardinality_list: list
    :ivar ou_class_list: A list of OntoUML Class objects.
    :vartype ou_class_list: list
    :ivar ou_classView_list: A list of OntoUML ClassView objects.
    :vartype ou_classView_list: list
    :ivar ou_diagram_list: A list of OntoUML Diagram objects.
    :vartype ou_diagram_list: list
    :ivar ou_generalization_list: A list of OntoUML Generalization objects.
    :vartype ou_generalization_list: list
    :ivar ou_generalizationSet_list: A list of OntoUML GeneralizationSet objects.
    :vartype ou_generalizationSet_list: list
    :ivar ou_generalizationSetView_list: A list of OntoUML GeneralizationSetView objects.
    :vartype ou_generalizationSetView_list: list
    :ivar ou_generalizationView_list: A list of OntoUML GeneralizationView objects.
    :vartype ou_generalizationView_list: list
    :ivar ou_literal_list: A list of OntoUML Literal objects.
    :vartype ou_literal_list: list
    :ivar ou_note_list: A list of OntoUML Note objects.
    :vartype ou_note_list: list
    :ivar ou_noteView_list: A list of OntoUML NoteView objects.
    :vartype ou_noteView_list: list
    :ivar ou_package_list: A list of OntoUML Package objects.
    :vartype ou_package_list: list
    :ivar ou_packageView_list: A list of OntoUML PackageView objects.
    :vartype ou_packageView_list: list
    :ivar ou_path_list: A list of OntoUML Path objects.
    :vartype ou_path_list: list
    :ivar ou_point_list: A list of OntoUML Point objects.
    :vartype ou_point_list: list
    :ivar ou_project_list: A list of OntoUML Project objects.
    :vartype ou_project_list: list
    :ivar ou_property_list: A list of OntoUML Property objects.
    :vartype ou_property_list: list
    :ivar ou_rectangle_list: A list of OntoUML Rectangle objects.
    :vartype ou_rectangle_list: list
    :ivar ou_relation_list: A list of OntoUML Relation objects.
    :vartype ou_relation_list: list
    :ivar ou_relationView_list: A list of OntoUML RelationView objects.
    :vartype ou_relationView_list: list
    :ivar ou_text_list: A list of OntoUML Text objects.
    :vartype ou_text_list: list
    """

    def __init__(self):
        self.ou_cardinality_list: list[OUCardinality] = []
        self.ou_class_list: list[OUClass] = []
        self.ou_classView_list: list[OUClassView] = []
        self.ou_diagram_list: list[OUDiagram] = []
        self.ou_generalization_list: list[OUGeneralization] = []
        self.ou_generalizationSet_list: list[OUGeneralizationSet] = []
        self.ou_generalizationSetView_list: list[OUGeneralizationSetView] = []
        self.ou_generalizationView_list: list[OUGeneralizationView] = []
        self.ou_literal_list: list[OULiteral] = []
        self.ou_note_list: list[OUNote] = []
        self.ou_noteView_list: list[OUNoteView] = []
        self.ou_package_list: list[OUPackage] = []
        self.ou_packageView_list: list[OUPackageView] = []
        self.ou_path_list: list[OUPath] = []
        self.ou_point_list: list[OUPoint] = []
        self.ou_project_list: list[OUProject] = []
        self.ou_property_list: list[OUProperty] = []
        self.ou_rectangle_list: list[OURectangle] = []
        self.ou_relation_list: list[OURelation] = []
        self.ou_relationView_list: list[OURelationView] = []
        self.ou_text_list: list[OUText] = []

    def add_element(self, element: _OUElement) -> None:
        """Add an OntoUML Element to its Corresponding List

        This method sorts the provided OntoUML element into its respective list within the OUGraph instance according
        to its type, facilitating an organized storage of diverse OntoUML elements.

        :param element: An OntoUML element to be added to the OUGraph.
        :type element: _OUElement
        """
        map_type_list = {
            OntoUML.Cardinality: self.ou_cardinality_list,
            OntoUML.Class: self.ou_class_list,
            OntoUML.ClassView: self.ou_classView_list,
            OntoUML.Diagram: self.ou_diagram_list,
            OntoUML.Generalization: self.ou_generalization_list,
            OntoUML.GeneralizationSet: self.ou_generalizationSet_list,
            OntoUML.GeneralizationSetView: self.ou_generalizationSetView_list,
            OntoUML.GeneralizationView: self.ou_generalizationView_list,
            OntoUML.Literal: self.ou_literal_list,
            OntoUML.Note: self.ou_note_list,
            OntoUML.NoteView: self.ou_noteView_list,
            OntoUML.Package: self.ou_package_list,
            OntoUML.PackageView: self.ou_packageView_list,
            OntoUML.Path: self.ou_path_list,
            OntoUML.Point: self.ou_point_list,
            OntoUML.Project: self.ou_project_list,
            OntoUML.Property: self.ou_property_list,
            OntoUML.Rectangle: self.ou_rectangle_list,
            OntoUML.Relation: self.ou_relation_list,
            OntoUML.RelationView: self.ou_relationView_list,
            OntoUML.Text: self.ou_text_list,
        }

        try:
            map_type_list[element.element_type].append(element)
        except:
            raise OUInvalidElementType(element.element_type)

    def read_graph(self, rdf_graph: Graph, include_concrete: bool = True) -> None:
        """Load OntoUML elements from an RDF graph into organized lists.

        This method iterates through all triples in the provided RDF graph, identifies OntoUML elements,
        and adds them to the respective lists based on their type.

        :param rdf_graph: An RDF graph containing OntoUML vocabulary data.
        :type rdf_graph: Graph
        :param include_concrete: Flag indicating whether to include concrete syntax elements.
        :type include_concrete: bool, optional
        """
        list_abstract_elements = OUAbstractElements.get_all()
        list_concrete_elements = OUConcreteElements.get_all()

        # s is the new OUElement id
        # o is the new OUElement type
        for s, _, o in rdf_graph.triples((None, RDF.type, None)):
            # ABSTRACT SYNTAX ELEMENTS
            if o in list_abstract_elements:
                new_element = ou_create_element(s, o)
                self.add_element(new_element)

            # CONCRETE SYNTAX ELEMENTS
            elif o in list_concrete_elements:
                if include_concrete:
                    new_element = ou_create_element(s, o)
                    self.add_element(new_element)
                else:
                    logger.debug(
                        f"Graph's element {s} of type {o} was not loaded into any OUGraph's list "
                        f"because it is part of OntoUML's concrete syntax ('include_concrete' is set to 'False')."
                    )
            else:
                logger.debug(
                    f"Graph's element {s} of type {o} was not loaded into any OUGraph's list "
                    f"because it is not an OntoUML element."
                )

    def write_graph(self, rdf_graph: Graph, include_concrete: bool = True) -> None:
        """Write OntoUML elements into an RDF graph.

        This method traverses through all stored OntoUML elements within the OUGraph and adds them to the provided
        RDF graph, either including or excluding concrete syntax elements based on the `include_concrete` parameter.

        :param rdf_graph: An RDF graph where OntoUML vocabulary data will be written.
        :type rdf_graph: Graph
        :param include_concrete: Flag indicating whether to include concrete syntax elements.
        :type include_concrete: bool, optional
        """
        list_abstract_elements = OUAbstractElements.get_all()

        for _, list_value in self.__dict__.items():
            for element in list_value:
                if include_concrete or (element.element_type in list_abstract_elements):
                    element.add_to_rdf_graph(rdf_graph)

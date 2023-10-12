"""Module for providing functions for manipulating concepts from the ontouml-py library."""
from rdflib import URIRef

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
from ontoumlpy.classes.ouexception import InvalidOntoUMLTypeException


def ou_create_element(individual_id: URIRef, individual_type: URIRef) -> _OUElement:
    """Creates an OntoUML element by mapping an RDF individual to its corresponding ontoumlpy class.

    This function takes as input the ID and type of an RDF individual and returns an instance of the appropriate
    OntoUML class from the `ontoumlpy` library. The function utilizes a predefined mapping between OntoUML types
    and `ontoumlpy` classes to determine which class to instantiate. If the provided RDF individual type does not
    correspond to a valid OntoUML type, an `InvalidOntoUMLTypeException` is raised.

    :param individual_id: The RDF ID of the individual to be mapped.
    :type individual_id: URIRef
    :param individual_type: The RDF type of the individual to be mapped.
    :type individual_type: URIRef
    :return: An instance of an ontoumlpy class corresponding to the RDF individual type provided.
    :rtype: _OUElement
    :raises InvalidOntoUMLTypeException: If the `individual_type` does not correspond to a valid OntoUML type.
    """
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
        raise InvalidOntoUMLTypeException(individual_type)
    return individual_obj

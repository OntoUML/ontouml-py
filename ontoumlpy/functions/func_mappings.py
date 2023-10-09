"""This module handles the mapping between OUTerm and OUElement objects.

It provides functions to retrieve OUElement objects from OUTerm objects and vice versa.
"""
from rdflib import URIRef

from ontoumlpy.classes._ouelement import _OUElement
from ontoumlpy.classes.ouelement_types import (
    OUCardinality,
    OUDiagram,
    OUGeneralizationSet,
    OUGeneralizationSetView,
    OUGeneralizationView,
    OUNoteView,
    OUPath,
    OUProperty,
    OURelationView,
    OUText,
    OURectangle,
    OUPackage,
    OUPoint,
    OUProject,
    OUClassView,
    OUClass,
    OUGeneralization,
    OULiteral,
    OUNote,
    OUPackageView,
    OURelation,
)
from ontoumlpy.classes.ouexception import OUUnmappedOUElement, OUUnmappedOUTerm
from ontoumlpy.classes.ontouml import OntoUML

_MAP_OUTERM_OUELEMENT = {
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


def get_ouelement_from_outerm(outerm: URIRef | str) -> _OUElement:
    """Return the corresponding OUElement object for a given OUTerm or URIRef/str object.

    If the input is a string, it's converted to a URIRef object before lookup.

    :param outerm: The OUTerm object or URIRef/str representing the term.
    :type outerm: Union[URIRef, str]
    :raises OUUnmappedOUTerm: If the OUTerm object is not found in the mapping.
    :return: The corresponding OUElement object.
    :rtype: _OUElement
    """
    if isinstance(outerm, str):
        outerm = URIRef(outerm)

    try:
        return _MAP_OUTERM_OUELEMENT[outerm]
    # Overwrites default KeyError
    except KeyError:
        raise OUUnmappedOUTerm(outerm)


def get_outerm_from_ouelement(ouelement: _OUElement | str) -> URIRef:
    """Return the corresponding OUTerm object for a given OUElement object or its class name as a string.

    This function iterates through the mapping dictionary to find the corresponding OUTerm object.
    Every OUElement object is assumed to be mapped to an OUTerm object.

    :param ouelement: The OUElement object or its class name as a string.
    :type ouelement: Union[_OUElement, str]
    :raises OUUnmappedOUElement: If the OUElement object is not found in the mapping.
    :return: The corresponding OUTerm object.
    :rtype: URIRef
    """

    if isinstance(ouelement, str):
        for key, value in _MAP_OUTERM_OUELEMENT.items():
            if value.__name__ == ouelement:
                return key
    elif isinstance(ouelement, _OUElement):
        ouelement_class = type(ouelement)  # Get the class of the ouelement instance
        for key, value in _MAP_OUTERM_OUELEMENT.items():
            if value == ouelement_class:
                return key

    # Every OUElement is mapped to an OUTerm, hence, this exception must never happen.
    # If the target value is not found, raise an exception.
    raise OUUnmappedOUElement(ouelement)

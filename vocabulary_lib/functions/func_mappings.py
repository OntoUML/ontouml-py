"""This module handles the mapping between OUTerm and OUElement objects.

It provides functions to retrieve OUElement objects from OUTerm objects and vice versa.
"""
from rdflib import URIRef

from vocabulary_lib.classes._ouelement import _OUElement
from vocabulary_lib.classes.ouelement_types import (
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
from vocabulary_lib.classes.ouexception import OUUnmappedOUElement, OUUnmappedOUTerm
from vocabulary_lib.classes.outerm import OUTerm

_MAP_OUTERM_OUELEMENT = {
    OUTerm.Cardinality: OUCardinality,
    OUTerm.Class: OUClass,
    OUTerm.ClassView: OUClassView,
    OUTerm.Diagram: OUDiagram,
    OUTerm.Generalization: OUGeneralization,
    OUTerm.GeneralizationSet: OUGeneralizationSet,
    OUTerm.GeneralizationSetView: OUGeneralizationSetView,
    OUTerm.GeneralizationView: OUGeneralizationView,
    OUTerm.Literal: OULiteral,
    OUTerm.Note: OUNote,
    OUTerm.NoteView: OUNoteView,
    OUTerm.Package: OUPackage,
    OUTerm.PackageView: OUPackageView,
    OUTerm.Path: OUPath,
    OUTerm.Point: OUPoint,
    OUTerm.Project: OUProject,
    OUTerm.Property: OUProperty,
    OUTerm.Rectangle: OURectangle,
    OUTerm.Relation: OURelation,
    OUTerm.RelationView: OURelationView,
    OUTerm.Text: OUText,
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
    else:
        for key, value in _MAP_OUTERM_OUELEMENT.items():
            if value == ouelement.__class__:
                return key

    # Every OUElement is mapped to an OUTerm, hence, this exception must never happen.
    # If the target value is not found, raise an exception.
    raise OUUnmappedOUElement(ouelement)

from rdflib import URIRef

from vocabulary_lib.classes._ouelement import _OUElement
from vocabulary_lib.classes.ouelement_types import (OUCardinality, OUDiagram, OUGeneralizationSet,
                                                    OUGeneralizationSetView, OUGeneralizationView, OUNoteView, OUPath,
                                                    OUProperty, OURelationView, OUText, OURectangle, OUPackage, OUPoint,
                                                    OUProject, OUClassView, OUClass, OUGeneralization, OULiteral,
                                                    OUNote, OUPackageView, OURelation, )
from vocabulary_lib.classes.ouexception import OUUnmappedOUElement, OUUnmappedOUTerm
from vocabulary_lib.classes.outerm import OUTerm

map_outerm_ouelement = {OUTerm.Cardinality: OUCardinality, OUTerm.Class: OUClass, OUTerm.ClassView: OUClassView,
                        OUTerm.Diagram: OUDiagram, OUTerm.Generalization: OUGeneralization,
                        OUTerm.GeneralizationSet: OUGeneralizationSet,
                        OUTerm.GeneralizationSetView: OUGeneralizationSetView,
                        OUTerm.GeneralizationView: OUGeneralizationView, OUTerm.Literal: OULiteral, OUTerm.Note: OUNote,
                        OUTerm.NoteView: OUNoteView, OUTerm.Package: OUPackage, OUTerm.PackageView: OUPackageView,
                        OUTerm.Path: OUPath, OUTerm.Point: OUPoint, OUTerm.Project: OUProject,
                        OUTerm.Property: OUProperty, OUTerm.Rectangle: OURectangle, OUTerm.Relation: OURelation,
                        OUTerm.RelationView: OURelationView, OUTerm.Text: OUText, }


def get_ouelement_from_outerm(outerm: URIRef | str) -> _OUElement:
    if isinstance(outerm, str):
        outerm = URIRef(outerm)

    try:
        return map_outerm_ouelement[outerm]
    # Overwrites default KeyError
    except Exception:
        raise OUUnmappedOUTerm(outerm)


def get_outerm_from_ouelement(ouelement: _OUElement) -> URIRef:
    for key, value in map_outerm_ouelement.items():
        if value == ouelement:
            return key

    # Every OUElement is mapped to an OUTerm, hence, this exception must never happen.
    # If the target value is not found, raise an exception.
    raise OUUnmappedOUElement(ouelement)

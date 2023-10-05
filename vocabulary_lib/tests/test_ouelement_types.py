from icecream import ic
from rdflib import RDF

from vocabulary_lib.classes.ouelement_types import *
from vocabulary_lib.classes.outerm import OUTerm
from vocabulary_lib.functions.func_mappings import get_outerm_from_ouelement


def test_class_OUCardinality() -> None:
    elem_type = OUCardinality
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.cardinalityValue, URIRef("x1")))
    g.add((elem_id, OUTerm.lowerBound, URIRef("x2")))
    g.add((elem_id, OUTerm.upperBound, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.cardinalityValue,URIRef)
    assert str(elem.cardinalityValue) == "x1"
    assert isinstance(elem.lowerBound,URIRef)
    assert str(elem.lowerBound) == "x2"
    assert isinstance(elem.upperBound,URIRef)
    assert str(elem.upperBound) == "x3"


def test_class_OUClass() -> None:
    elem_type = OUClass
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.name, URIRef("x1")))
    g.add((elem_id, OUTerm.description, URIRef("x3")))
    g.add((elem_id, OUTerm.isAbstract, URIRef("x4")))
    g.add((elem_id, OUTerm.isDerived, URIRef("x5")))
    g.add((elem_id, OUTerm.isPowertype, URIRef("x6")))
    g.add((elem_id, OUTerm.literal, URIRef("x7")))
    g.add((elem_id, OUTerm.order, URIRef("x8")))
    g.add((elem_id, OUTerm.project, URIRef("x9")))
    g.add((elem_id, OUTerm.stereotype, URIRef("x11")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name,URIRef)
    assert str(elem.name) == "x1"
    assert isinstance(elem.description,URIRef)
    assert str(elem.description) == "x3"
    assert isinstance(elem.isAbstract,URIRef)
    assert str(elem.isAbstract) == "x4"
    assert isinstance(elem.isDerived,URIRef)
    assert str(elem.isDerived) == "x5"
    assert isinstance(elem.isPowertype,URIRef)
    assert str(elem.isPowertype) == "x6"
    assert isinstance(elem.literal,URIRef)
    assert str(elem.literal) == "x7"
    assert isinstance(elem.order,URIRef)
    assert str(elem.order) == "x8"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x9"
    assert isinstance(elem.stereotype,URIRef)
    assert str(elem.stereotype) == "x11"


def test_class_OUClassView() -> None:
    elem_type = OUClassView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.isViewOf, URIRef("x1")))
    g.add((elem_id, OUTerm.project, URIRef("x2")))
    g.add((elem_id, OUTerm.shape, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf,URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape,URIRef)
    assert str(elem.shape) == "x3"


def test_class_OUDiagram() -> None:
    elem_type = OUDiagram
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.name, URIRef("x1")))
    g.add((elem_id, OUTerm.owner, URIRef("x3")))
    g.add((elem_id, OUTerm.project, URIRef("x4")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name,URIRef)
    assert str(elem.name) == "x1"
    assert isinstance(elem.owner,URIRef)
    assert str(elem.owner) == "x3"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x4"


def test_class_OUGeneralization() -> None:
    elem_type = OUGeneralization
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.general, URIRef("x1")))
    g.add((elem_id, OUTerm.specific, URIRef("x2")))
    g.add((elem_id, OUTerm.project, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.general,URIRef)
    assert str(elem.general) == "x1"
    assert isinstance(elem.specific,URIRef)
    assert str(elem.specific) == "x2"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x3"


def test_class_OUGeneralizationSet() -> None:
    elem_type = OUGeneralizationSet
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.isComplete, URIRef("x2")))
    g.add((elem_id, OUTerm.isDisjoint, URIRef("x3")))
    g.add((elem_id, OUTerm.name, URIRef("x4")))
    g.add((elem_id, OUTerm.project, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isComplete,URIRef)
    assert str(elem.isComplete) == "x2"
    assert isinstance(elem.isDisjoint,URIRef)
    assert str(elem.isDisjoint) == "x3"
    assert isinstance(elem.name,URIRef)
    assert str(elem.name) == "x4"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x5"


def test_class_OUGeneralizationSetView() -> None:
    elem_type = OUGeneralizationSetView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.isViewOf, URIRef("x1")))
    g.add((elem_id, OUTerm.project, URIRef("x2")))
    g.add((elem_id, OUTerm.shape, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf,URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape,URIRef)
    assert str(elem.shape) == "x3"


def test_class_OUGeneralizationView() -> None:
    elem_type = OUGeneralizationView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.isViewOf, URIRef("x1")))
    g.add((elem_id, OUTerm.project, URIRef("x2")))
    g.add((elem_id, OUTerm.shape, URIRef("x3")))
    g.add((elem_id, OUTerm.sourceView, URIRef("x4")))
    g.add((elem_id, OUTerm.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf,URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape,URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView,URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView,URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OULiteral() -> None:
    elem_type = OULiteral
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.project, URIRef("x1")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x1"


# def test_class_OUNote() -> None:
#     elem_type = OUNote
#     term = get_outerm_from_ouelement(elem_type)
#
#     g = Graph()
#     elem_id = URIRef("elem")
#
#     g.add((elem_id, OUTerm.text, URIRef("x1")))
#
#     g.add((elem_id, RDF.type, term))
#     elem = elem_type(g, elem_id)
#
#     assert isinstance(elem.text,URIRef)
#     assert str(elem.text) == "x1"


def test_class_OUNoteView() -> None:
    elem_type = OUNoteView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.isViewOf, URIRef("x1")))
    g.add((elem_id, OUTerm.project, URIRef("x2")))
    g.add((elem_id, OUTerm.shape, URIRef("x3")))
    g.add((elem_id, OUTerm.sourceView, URIRef("x4")))
    g.add((elem_id, OUTerm.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf,URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape,URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView,URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView,URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OUPackage() -> None:
    elem_type = OUPackage
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.name, URIRef("x2")))
    g.add((elem_id, OUTerm.project, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name,URIRef)
    assert str(elem.name) == "x2"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x3"


def test_class_OUPackageView() -> None:
    elem_type = OUPackageView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.isViewOf, URIRef("x1")))
    g.add((elem_id, OUTerm.project, URIRef("x2")))
    g.add((elem_id, OUTerm.shape, URIRef("x3")))
    g.add((elem_id, OUTerm.sourceView, URIRef("x4")))
    g.add((elem_id, OUTerm.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf,URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape,URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView,URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView,URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OUPath() -> None:
    elem_type = OUPath
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.project, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"


def test_class_OUPoint() -> None:
    elem_type = OUPoint
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.xCoordinate, URIRef("x1")))
    g.add((elem_id, OUTerm.yCoordinate, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.xCoordinate,URIRef)
    assert str(elem.xCoordinate) == "x1"
    assert isinstance(elem.yCoordinate,URIRef)
    assert str(elem.yCoordinate) == "x2"


def test_class_OUProject() -> None:
    elem_type = OUProject
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.name, URIRef("x1")))
    g.add((elem_id, OUTerm.model, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name,URIRef)
    assert str(elem.name) == "x1"
    assert isinstance(elem.model,URIRef)
    assert str(elem.model) == "x3"


def test_class_OUProperty() -> None:
    elem_type = OUProperty
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.aggregationKind, URIRef("x1")))
    g.add((elem_id, OUTerm.cardinality, URIRef("x2")))
    g.add((elem_id, OUTerm.isDerived, URIRef("x3")))
    g.add((elem_id, OUTerm.isOrdered, URIRef("x4")))
    g.add((elem_id, OUTerm.isReadOnly, URIRef("x5")))
    g.add((elem_id, OUTerm.name, URIRef("x6")))
    g.add((elem_id, OUTerm.propertyType, URIRef("x7")))
    g.add((elem_id, OUTerm.project, URIRef("x8")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.aggregationKind,URIRef)
    assert str(elem.aggregationKind) == "x1"
    assert isinstance(elem.cardinality,URIRef)
    assert str(elem.cardinality) == "x2"
    assert isinstance(elem.isDerived,URIRef)
    assert str(elem.isDerived) == "x3"
    assert isinstance(elem.isOrdered,URIRef)
    assert str(elem.isOrdered) == "x4"
    assert isinstance(elem.isReadOnly,URIRef)
    assert str(elem.isReadOnly) == "x5"
    assert isinstance(elem.name,URIRef)
    assert str(elem.name) == "x6"
    assert isinstance(elem.propertyType,URIRef)
    assert str(elem.propertyType) == "x7"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x8"


def test_class_OURectangle() -> None:
    elem_type = OURectangle
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.topLeftPosition, URIRef("x1")))
    g.add((elem_id, OUTerm.height, URIRef("x2")))
    g.add((elem_id, OUTerm.width, URIRef("x3")))
    g.add((elem_id, OUTerm.project, URIRef("x4")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.topLeftPosition,URIRef)
    assert str(elem.topLeftPosition) == "x1"
    assert isinstance(elem.height,URIRef)
    assert str(elem.height) == "x2"
    assert isinstance(elem.width,URIRef)
    assert str(elem.width) == "x3"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x4"


def test_class_OURelation() -> None:
    elem_type = OURelation
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.description, URIRef("x1")))
    g.add((elem_id, OUTerm.isAbstract, URIRef("x2")))
    g.add((elem_id, OUTerm.isDerived, URIRef("x3")))
    g.add((elem_id, OUTerm.name, URIRef("x4")))
    g.add((elem_id, OUTerm.sourceEnd, URIRef("x6")))
    g.add((elem_id, OUTerm.stereotype, URIRef("x7")))
    g.add((elem_id, OUTerm.targetEnd, URIRef("x8")))
    g.add((elem_id, OUTerm.project, URIRef("x9")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.description,URIRef)
    assert str(elem.description) == "x1"
    assert isinstance(elem.isAbstract,URIRef)
    assert str(elem.isAbstract) == "x2"
    assert isinstance(elem.isDerived,URIRef)
    assert str(elem.isDerived) == "x3"
    assert isinstance(elem.name,URIRef)
    assert str(elem.name) == "x4"
    assert isinstance(elem.sourceEnd,URIRef)
    assert str(elem.sourceEnd) == "x6"
    assert isinstance(elem.stereotype,URIRef)
    assert str(elem.stereotype) == "x7"
    assert isinstance(elem.targetEnd,URIRef)
    assert str(elem.targetEnd) == "x8"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x9"


def test_class_OURelationView() -> None:
    elem_type = OURelationView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.isViewOf, URIRef("x1")))
    g.add((elem_id, OUTerm.project, URIRef("x2")))
    g.add((elem_id, OUTerm.shape, URIRef("x3")))
    g.add((elem_id, OUTerm.sourceView, URIRef("x4")))
    g.add((elem_id, OUTerm.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf,URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape,URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView,URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView,URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OUText() -> None:
    term = OUTerm.Text
    elem_type = OUText

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OUTerm.height, URIRef("x1")))
    g.add((elem_id, OUTerm.project, URIRef("x2")))
    g.add((elem_id, OUTerm.text, URIRef("x3")))
    g.add((elem_id, OUTerm.topLeftPosition, URIRef("x4")))
    g.add((elem_id, OUTerm.width, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.height,URIRef)
    assert str(elem.height) == "x1"
    assert isinstance(elem.project,URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.text,URIRef)
    assert str(elem.text) == "x3"
    assert isinstance(elem.topLeftPosition,URIRef)
    assert str(elem.topLeftPosition) == "x4"
    assert isinstance(elem.width,URIRef)
    assert str(elem.width) == "x5"

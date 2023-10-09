"""
Module for testing classes related to the each specific type ou OUElement.

This module provides tests for the classes defined in the ontouml-py classes/ouelement_types module.


"""
from rdflib import RDF, URIRef, Graph

from ontoumlpy.classes.ouelement_types import (
    OUCardinality,
    OUClass,
    OUClassView,
    OUDiagram,
    OUGeneralization,
    OUGeneralizationSet,
    OUGeneralizationSetView,
    OUGeneralizationView,
    OULiteral,
    OUNote,
    OUNoteView,
    OUPackage,
    OUPackageView,
    OUPath,
    OUPoint,
    OUProject,
    OUProperty,
    OURectangle,
    OURelation,
    OURelationView,
    OUText,
)
from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.functions.func_mappings import get_outerm_from_ouelement


def test_class_OUCardinality() -> None:
    """Test the OUCardinality class by creating a new instance and verifying its attributes."""
    elem_type = OUCardinality
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.cardinalityValue, URIRef("x1")))
    g.add((elem_id, OntoUML.lowerBound, URIRef("x2")))
    g.add((elem_id, OntoUML.upperBound, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.cardinalityValue, URIRef)
    assert str(elem.cardinalityValue) == "x1"
    assert isinstance(elem.lowerBound, URIRef)
    assert str(elem.lowerBound) == "x2"
    assert isinstance(elem.upperBound, URIRef)
    assert str(elem.upperBound) == "x3"


def test_class_OUClass() -> None:
    """Test the OUClass class by creating a new instance and verifying its attributes."""
    elem_type = OUClass
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.name, URIRef("x1")))
    g.add((elem_id, OntoUML.description, URIRef("x3")))
    g.add((elem_id, OntoUML.isAbstract, URIRef("x4")))
    g.add((elem_id, OntoUML.isDerived, URIRef("x5")))
    g.add((elem_id, OntoUML.isPowertype, URIRef("x6")))
    g.add((elem_id, OntoUML.literal, URIRef("x7")))
    g.add((elem_id, OntoUML.order, URIRef("x8")))
    g.add((elem_id, OntoUML.project, URIRef("x9")))
    g.add((elem_id, OntoUML.stereotype, URIRef("x11")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name, URIRef)
    assert str(elem.name) == "x1"
    assert isinstance(elem.description, URIRef)
    assert str(elem.description) == "x3"
    assert isinstance(elem.isAbstract, URIRef)
    assert str(elem.isAbstract) == "x4"
    assert isinstance(elem.isDerived, URIRef)
    assert str(elem.isDerived) == "x5"
    assert isinstance(elem.isPowertype, URIRef)
    assert str(elem.isPowertype) == "x6"
    assert isinstance(elem.literal, URIRef)
    assert str(elem.literal) == "x7"
    assert isinstance(elem.order, URIRef)
    assert str(elem.order) == "x8"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x9"
    assert isinstance(elem.stereotype, URIRef)
    assert str(elem.stereotype) == "x11"


def test_class_OUClass_lists() -> None:
    """Test the list attributes of the OUClass class by creating a new instance and verifying its attributes."""
    elem_type = OUClass
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.attribute, URIRef("x1a")))
    g.add((elem_id, OntoUML.attribute, URIRef("x1b")))

    g.add((elem_id, OntoUML.restrictedTo, URIRef("x2a")))
    g.add((elem_id, OntoUML.restrictedTo, URIRef("x2b")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.attribute, list)
    assert isinstance(elem.attribute[0], URIRef)
    assert isinstance(elem.attribute[1], URIRef)
    assert str(elem.attribute[0]) == "x1a"
    assert str(elem.attribute[1]) == "x1b"
    assert isinstance(elem.restrictedTo, list)


def test_class_OUClassView() -> None:
    """Test the OUClassView class by creating a new instance and verifying its attributes."""
    elem_type = OUClassView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.isViewOf, URIRef("x1")))
    g.add((elem_id, OntoUML.project, URIRef("x2")))
    g.add((elem_id, OntoUML.shape, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf, URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape, URIRef)
    assert str(elem.shape) == "x3"


def test_class_OUDiagram() -> None:
    """Test the OUDiagram class by creating a new instance and verifying its attributes."""
    elem_type = OUDiagram
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.name, URIRef("x1")))
    g.add((elem_id, OntoUML.owner, URIRef("x3")))
    g.add((elem_id, OntoUML.project, URIRef("x4")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name, URIRef)
    assert str(elem.name) == "x1"
    assert isinstance(elem.owner, URIRef)
    assert str(elem.owner) == "x3"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x4"


def test_class_OUDiagram_list() -> None:
    """Test the list attributes of the OUDiagram class by creating a new instance and verifying its attributes."""
    elem_type = OUDiagram
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.containsView, URIRef("x1")))
    g.add((elem_id, OntoUML.containsView, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.containsView, list)
    assert isinstance(elem.containsView[0], URIRef)
    assert isinstance(elem.containsView[1], URIRef)
    assert str((elem.containsView)[0]) == "x1"
    assert str((elem.containsView)[1]) == "x2"


def test_class_OUGeneralization() -> None:
    """Test the OUGeneralization class by creating a new instance and verifying its attributes."""
    elem_type = OUGeneralization
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.general, URIRef("x1")))
    g.add((elem_id, OntoUML.specific, URIRef("x2")))
    g.add((elem_id, OntoUML.project, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.general, URIRef)
    assert str(elem.general) == "x1"
    assert isinstance(elem.specific, URIRef)
    assert str(elem.specific) == "x2"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x3"


def test_class_OUGeneralizationSet() -> None:
    """Test the OUGeneralizationSet class by creating a new instance and verifying its attributes."""
    elem_type = OUGeneralizationSet
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.isComplete, URIRef("x2")))
    g.add((elem_id, OntoUML.isDisjoint, URIRef("x3")))
    g.add((elem_id, OntoUML.name, URIRef("x4")))
    g.add((elem_id, OntoUML.project, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isComplete, URIRef)
    assert str(elem.isComplete) == "x2"
    assert isinstance(elem.isDisjoint, URIRef)
    assert str(elem.isDisjoint) == "x3"
    assert isinstance(elem.name, URIRef)
    assert str(elem.name) == "x4"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x5"


def test_class_OUGeneralizationSet_list() -> None:
    """Test the list attributes of the OUGeneralizationSet class by creating a new instance and verifying its \
    attributes."""
    elem_type = OUGeneralizationSet
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.generalization, URIRef("x1")))
    g.add((elem_id, OntoUML.generalization, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.generalization, list)
    assert isinstance(elem.generalization[0], URIRef)
    assert isinstance(elem.generalization[1], URIRef)
    assert str((elem.generalization)[0]) == "x1"
    assert str((elem.generalization)[1]) == "x2"


def test_class_OUGeneralizationSetView() -> None:
    """Test the OUGeneralizationSetView class by creating a new instance and verifying its attributes."""
    elem_type = OUGeneralizationSetView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.isViewOf, URIRef("x1")))
    g.add((elem_id, OntoUML.project, URIRef("x2")))
    g.add((elem_id, OntoUML.shape, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf, URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape, URIRef)
    assert str(elem.shape) == "x3"


def test_class_OUGeneralizationView() -> None:
    """Test the OUGeneralizationView class by creating a new instance and verifying its attributes."""
    elem_type = OUGeneralizationView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.isViewOf, URIRef("x1")))
    g.add((elem_id, OntoUML.project, URIRef("x2")))
    g.add((elem_id, OntoUML.shape, URIRef("x3")))
    g.add((elem_id, OntoUML.sourceView, URIRef("x4")))
    g.add((elem_id, OntoUML.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf, URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape, URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView, URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView, URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OULiteral() -> None:
    """Test the OULiteral class by creating a new instance and verifying its attributes."""
    elem_type = OULiteral
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.project, URIRef("x1")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x1"


def test_class_OUNote() -> None:
    """Test the OUNote class by creating a new instance and verifying its attributes."""
    elem_type = OUNote
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.text, URIRef("x1")))
    g.add((elem_id, OntoUML.text, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.text, list)
    assert isinstance(elem.text[0], URIRef)
    assert isinstance(elem.text[1], URIRef)
    assert str((elem.text)[0]) == "x1"
    assert str((elem.text)[1]) == "x2"


def test_class_OUNoteView() -> None:
    """Test the OUNoteView class by creating a new instance and verifying its attributes."""
    elem_type = OUNoteView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.isViewOf, URIRef("x1")))
    g.add((elem_id, OntoUML.project, URIRef("x2")))
    g.add((elem_id, OntoUML.shape, URIRef("x3")))
    g.add((elem_id, OntoUML.sourceView, URIRef("x4")))
    g.add((elem_id, OntoUML.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf, URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape, URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView, URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView, URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OUPackage() -> None:
    """Test the OUPackage class by creating a new instance and verifying its attributes."""
    elem_type = OUPackage
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.name, URIRef("x2")))
    g.add((elem_id, OntoUML.project, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name, URIRef)
    assert str(elem.name) == "x2"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x3"


def test_class_OUPackage_list() -> None:
    """Test the list attributes of the OUPackage class by creating a new instance and verifying its attributes."""
    elem_type = OUPackage
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.containsModelElement, URIRef("x1")))
    g.add((elem_id, OntoUML.containsModelElement, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.containsModelElement, list)
    assert isinstance(elem.containsModelElement[0], URIRef)
    assert isinstance(elem.containsModelElement[1], URIRef)
    assert str((elem.containsModelElement)[0]) == "x1"
    assert str((elem.containsModelElement)[1]) == "x2"


def test_class_OUPackageView() -> None:
    """Test the OUPackageView class by creating a new instance and verifying its attributes."""
    elem_type = OUPackageView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.isViewOf, URIRef("x1")))
    g.add((elem_id, OntoUML.project, URIRef("x2")))
    g.add((elem_id, OntoUML.shape, URIRef("x3")))
    g.add((elem_id, OntoUML.sourceView, URIRef("x4")))
    g.add((elem_id, OntoUML.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf, URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape, URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView, URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView, URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OUPath() -> None:
    """Test the OUPath class by creating a new instance and verifying its attributes."""
    elem_type = OUPath
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.project, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"


def test_class_OUPath_list() -> None:
    """Test the list attributes of the OUPath class by creating a new instance and verifying its attributes."""
    elem_type = OUPath
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.point, URIRef("x1")))
    g.add((elem_id, OntoUML.point, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.point, list)
    assert isinstance(elem.point[0], URIRef)
    assert isinstance(elem.point[1], URIRef)
    assert str((elem.point)[0]) == "x1"
    assert str((elem.point)[1]) == "x2"


def test_class_OUPoint() -> None:
    """Test the OUPoint class by creating a new instance and verifying its attributes."""
    elem_type = OUPoint
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.xCoordinate, URIRef("x1")))
    g.add((elem_id, OntoUML.yCoordinate, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.xCoordinate, URIRef)
    assert str(elem.xCoordinate) == "x1"
    assert isinstance(elem.yCoordinate, URIRef)
    assert str(elem.yCoordinate) == "x2"


def test_class_OUProject() -> None:
    """Test the OUProject class by creating a new instance and verifying its attributes."""
    elem_type = OUProject
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.name, URIRef("x1")))
    g.add((elem_id, OntoUML.model, URIRef("x3")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.name, URIRef)
    assert str(elem.name) == "x1"
    assert isinstance(elem.model, URIRef)
    assert str(elem.model) == "x3"


def test_class_OUProject_list() -> None:
    """Test the list attributes of the OUProject class by creating a new instance and verifying its attributes."""
    elem_type = OUProject
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.diagram, URIRef("x1")))
    g.add((elem_id, OntoUML.diagram, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.diagram, list)
    assert isinstance(elem.diagram[0], URIRef)
    assert isinstance(elem.diagram[1], URIRef)
    assert str((elem.diagram)[0]) == "x1"
    assert str((elem.diagram)[1]) == "x2"


def test_class_OUProperty() -> None:
    """Test the OUProperty class by creating a new instance and verifying its attributes."""
    elem_type = OUProperty
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.aggregationKind, URIRef("x1")))
    g.add((elem_id, OntoUML.cardinality, URIRef("x2")))
    g.add((elem_id, OntoUML.isDerived, URIRef("x3")))
    g.add((elem_id, OntoUML.isOrdered, URIRef("x4")))
    g.add((elem_id, OntoUML.isReadOnly, URIRef("x5")))
    g.add((elem_id, OntoUML.name, URIRef("x6")))
    g.add((elem_id, OntoUML.propertyType, URIRef("x7")))
    g.add((elem_id, OntoUML.project, URIRef("x8")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.aggregationKind, URIRef)
    assert str(elem.aggregationKind) == "x1"
    assert isinstance(elem.cardinality, URIRef)
    assert str(elem.cardinality) == "x2"
    assert isinstance(elem.isDerived, URIRef)
    assert str(elem.isDerived) == "x3"
    assert isinstance(elem.isOrdered, URIRef)
    assert str(elem.isOrdered) == "x4"
    assert isinstance(elem.isReadOnly, URIRef)
    assert str(elem.isReadOnly) == "x5"
    assert isinstance(elem.name, URIRef)
    assert str(elem.name) == "x6"
    assert isinstance(elem.propertyType, URIRef)
    assert str(elem.propertyType) == "x7"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x8"


def test_class_OURectangle() -> None:
    """Test the OURectangle class by creating a new instance and verifying its attributes."""
    elem_type = OURectangle
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.topLeftPosition, URIRef("x1")))
    g.add((elem_id, OntoUML.height, URIRef("x2")))
    g.add((elem_id, OntoUML.width, URIRef("x3")))
    g.add((elem_id, OntoUML.project, URIRef("x4")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.topLeftPosition, URIRef)
    assert str(elem.topLeftPosition) == "x1"
    assert isinstance(elem.height, URIRef)
    assert str(elem.height) == "x2"
    assert isinstance(elem.width, URIRef)
    assert str(elem.width) == "x3"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x4"


def test_class_OURelation() -> None:
    """Test the OURelation class by creating a new instance and verifying its attributes."""
    elem_type = OURelation
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.description, URIRef("x1")))
    g.add((elem_id, OntoUML.isAbstract, URIRef("x2")))
    g.add((elem_id, OntoUML.isDerived, URIRef("x3")))
    g.add((elem_id, OntoUML.name, URIRef("x4")))
    g.add((elem_id, OntoUML.sourceEnd, URIRef("x6")))
    g.add((elem_id, OntoUML.stereotype, URIRef("x7")))
    g.add((elem_id, OntoUML.targetEnd, URIRef("x8")))
    g.add((elem_id, OntoUML.project, URIRef("x9")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.description, URIRef)
    assert str(elem.description) == "x1"
    assert isinstance(elem.isAbstract, URIRef)
    assert str(elem.isAbstract) == "x2"
    assert isinstance(elem.isDerived, URIRef)
    assert str(elem.isDerived) == "x3"
    assert isinstance(elem.name, URIRef)
    assert str(elem.name) == "x4"
    assert isinstance(elem.sourceEnd, URIRef)
    assert str(elem.sourceEnd) == "x6"
    assert isinstance(elem.stereotype, URIRef)
    assert str(elem.stereotype) == "x7"
    assert isinstance(elem.targetEnd, URIRef)
    assert str(elem.targetEnd) == "x8"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x9"


def test_class_OURelation_list() -> None:
    """Test the list attributes of the OURelation class by creating a new instance and verifying its attributes."""
    elem_type = OURelation
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.relationEnd, URIRef("x1")))
    g.add((elem_id, OntoUML.relationEnd, URIRef("x2")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.relationEnd, list)
    assert isinstance(elem.relationEnd[0], URIRef)
    assert isinstance(elem.relationEnd[1], URIRef)
    assert str((elem.relationEnd)[0]) == "x1"
    assert str((elem.relationEnd)[1]) == "x2"


def test_class_OURelationView() -> None:
    """Test the OURelationView class by creating a new instance and verifying its attributes."""
    elem_type = OURelationView
    term = get_outerm_from_ouelement(elem_type)

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.isViewOf, URIRef("x1")))
    g.add((elem_id, OntoUML.project, URIRef("x2")))
    g.add((elem_id, OntoUML.shape, URIRef("x3")))
    g.add((elem_id, OntoUML.sourceView, URIRef("x4")))
    g.add((elem_id, OntoUML.targetView, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.isViewOf, URIRef)
    assert str(elem.isViewOf) == "x1"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.shape, URIRef)
    assert str(elem.shape) == "x3"
    assert isinstance(elem.sourceView, URIRef)
    assert str(elem.sourceView) == "x4"
    assert isinstance(elem.targetView, URIRef)
    assert str(elem.targetView) == "x5"


def test_class_OUText() -> None:
    """Test the OUText class by creating a new instance and verifying its attributes."""
    term = OntoUML.Text
    elem_type = OUText

    g = Graph()
    elem_id = URIRef("elem")

    g.add((elem_id, OntoUML.height, URIRef("x1")))
    g.add((elem_id, OntoUML.project, URIRef("x2")))
    g.add((elem_id, OntoUML.text, URIRef("x3")))
    g.add((elem_id, OntoUML.topLeftPosition, URIRef("x4")))
    g.add((elem_id, OntoUML.width, URIRef("x5")))

    g.add((elem_id, RDF.type, term))
    elem = elem_type(g, elem_id)

    assert isinstance(elem.height, URIRef)
    assert str(elem.height) == "x1"
    assert isinstance(elem.project, URIRef)
    assert str(elem.project) == "x2"
    assert isinstance(elem.text, URIRef)
    assert str(elem.text) == "x3"
    assert isinstance(elem.topLeftPosition, URIRef)
    assert str(elem.topLeftPosition) == "x4"
    assert isinstance(elem.width, URIRef)
    assert str(elem.width) == "x5"

"""This module defines various OntoUML Stereotypes related to relations, properties, aggregation kinds, and ontological
natures used in OntoUML modeling.

Each enumeration represents a specific grouping of stereotypes, providing a convenient and semantically meaningful way to
access and utilize the stereotypes in OntoUML modeling.
"""

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouenumeration._ouenumeration import _OUEnumeration


class OURelationStereotypes(_OUEnumeration):
    """Enumeration of OntoUML relation stereotypes."""

    bringsAbout = OntoUML.bringsAbout
    characterization = OntoUML.characterization
    comparative = OntoUML.comparative
    componentOf = OntoUML.componentOf
    creation = OntoUML.creation
    derivation = OntoUML.derivation
    externalDependence = OntoUML.externalDependence
    historicalDependence = OntoUML.historicalDependence
    instantiation = OntoUML.instantiation
    manifestation = OntoUML.manifestation
    material = OntoUML.material
    mediation = OntoUML.mediation
    memberOf = OntoUML.memberOf
    participation = OntoUML.participation
    participational = OntoUML.participational
    subCollectionOf = OntoUML.subCollectionOf
    subQuantityOf = OntoUML.subQuantityOf
    termination = OntoUML.termination
    triggers = OntoUML.triggers


class OUPropertyStereotypes(_OUEnumeration):
    """Enumeration of OntoUML property stereotypes."""

    begin = OntoUML.begin
    end = OntoUML.end


class OUAggregationKinds(_OUEnumeration):
    """Enumeration of OntoUML aggregation kinds."""

    composite = OntoUML.composite
    none = OntoUML.none
    shared = OntoUML.shared


class OUOntologicalNatures(_OUEnumeration):
    """Enumeration of OntoUML ontological natures."""

    abstractNature = OntoUML.abstractNature
    collectiveNature = OntoUML.collectiveNature
    eventNature = OntoUML.eventNature
    extrinsicModeNature = OntoUML.extrinsicModeNature
    functionalComplexNature = OntoUML.functionalComplexNature
    intrinsicModeNature = OntoUML.intrinsicModeNature
    qualityNature = OntoUML.qualityNature
    quantityNature = OntoUML.quantityNature
    relatorNature = OntoUML.relatorNature
    situationNature = OntoUML.situationNature
    typeNature = OntoUML.typeNature


class OUAbstractElements(_OUEnumeration):
    # Model Elements
    Class = OntoUML.Class
    Generalization = OntoUML.Generalization
    GeneralizationSet = OntoUML.GeneralizationSet
    Literal = OntoUML.Literal
    Note = OntoUML.Note
    Package = OntoUML.Package
    Property = OntoUML.Property
    Relation = OntoUML.Relation

    # Other
    Cardinality = OntoUML.Cardinality
    Diagram = OntoUML.Diagram
    Project = OntoUML.Project


class OUConcreteElements(_OUEnumeration):
    # Diagram Elements
    ## Shapes
    Path = OntoUML.Path
    Rectangle = OntoUML.Rectangle
    Text = OntoUML.Text

    ## Views
    ClassView = OntoUML.ClassView
    GeneralizationSetView = OntoUML.GeneralizationSetView
    GeneralizationView = OntoUML.GeneralizationView
    NoteView = OntoUML.NoteView
    PackageView = OntoUML.PackageView
    RelationView = OntoUML.RelationView

    # Other
    Point = OntoUML.Point

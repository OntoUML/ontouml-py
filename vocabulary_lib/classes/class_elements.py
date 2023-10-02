from rdflib import URIRef, Graph

from vocabulary_lib.classes.class_term import OUTerm
from vocabulary_lib.functions.func_rdf_utils import create_list_objects


class OUCardinality:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.cardinality_value: URIRef = ontouml_model.value(object_id, OUTerm.cardinalityValue)
        self.lower_bound: URIRef = ontouml_model.value(object_id, OUTerm.lowerBound)
        self.upper_bound: URIRef = ontouml_model.value(object_id, OUTerm.upperBound)


class OUClass:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.name: URIRef = ontouml_model.value(object_id, OUTerm.name)
        self.attribute: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.attribute)
        self.description: URIRef = ontouml_model.value(object_id, OUTerm.description)
        self.is_abstract: URIRef = ontouml_model.value(object_id, OUTerm.isAbstract)
        self.is_derived: URIRef = ontouml_model.value(object_id, OUTerm.isDerived)
        self.is_powertype: URIRef = ontouml_model.value(object_id, OUTerm.isPowertype)
        self.literal: URIRef = ontouml_model.value(object_id, OUTerm.literal)
        self.order: URIRef = ontouml_model.value(object_id, OUTerm.order)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.restricted_to: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.restrictedTo)
        self.stereotype: URIRef = ontouml_model.value(object_id, OUTerm.stereotype)


class OUClassView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ontouml_model.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_model.value(object_id, OUTerm.shape)


class OUDiagram:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.name: URIRef = ontouml_model.value(object_id, OUTerm.name)
        self.containsView: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.containsView)
        self.owner: URIRef = ontouml_model.value(object_id, OUTerm.owner)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OUGeneralization:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.general: URIRef = ontouml_model.value(object_id, OUTerm.general)
        self.specific: URIRef = ontouml_model.value(object_id, OUTerm.specific)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OUGeneralizationSet:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.generalization: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.generalization)
        self.is_complete: URIRef = ontouml_model.value(object_id, OUTerm.isComplete)
        self.is_disjoint: URIRef = ontouml_model.value(object_id, OUTerm.isDisjoint)
        self.name: URIRef = ontouml_model.value(object_id, OUTerm.name)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OUGeneralizationSetView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ontouml_model.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_model.value(object_id, OUTerm.shape)


class OULiteral:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OUGeneralizationView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ontouml_model.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_model.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_model.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_model.value(object_id, OUTerm.targetView)


class OUNote:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.text: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.text)


class OUNoteView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ontouml_model.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_model.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_model.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_model.value(object_id, OUTerm.targetView)


class OUPackage:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.contains_model_element: list[URIRef] = create_list_objects(
            ontouml_model, object_id, OUTerm.containsModelElement
        )
        self.name: URIRef = ontouml_model.value(object_id, OUTerm.name)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OUPackageView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ontouml_model.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_model.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_model.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_model.value(object_id, OUTerm.targetView)


class OUPath:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.point: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.point)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OUPoint:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.x_coordinate: URIRef = ontouml_model.value(object_id, OUTerm.xCoordinate)
        self.y_coordinate: URIRef = ontouml_model.value(object_id, OUTerm.yCoordinate)


class OUProject:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.name: URIRef = ontouml_model.value(object_id, OUTerm.name)
        self.diagram: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.diagram)
        self.model: URIRef = ontouml_model.value(object_id, OUTerm.model)


class OUProperty:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.aggregation_kind: URIRef = ontouml_model.value(object_id, OUTerm.aggregationKind)
        self.cardinality: URIRef = ontouml_model.value(object_id, OUTerm.cardinality)
        self.is_derived: URIRef = ontouml_model.value(object_id, OUTerm.isDerived)
        self.is_ordered: URIRef = ontouml_model.value(object_id, OUTerm.isOrdered)
        self.is_read_only: URIRef = ontouml_model.value(object_id, OUTerm.isReadOnly)
        self.name: URIRef = ontouml_model.value(object_id, OUTerm.name)
        self.property_type: URIRef = ontouml_model.value(object_id, OUTerm.propertyType)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OURectangle:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.top_left_position: URIRef = ontouml_model.value(object_id, OUTerm.topLeftPosition)
        self.height: URIRef = ontouml_model.value(object_id, OUTerm.height)
        self.width: URIRef = ontouml_model.value(object_id, OUTerm.width)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OURelation:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.description: URIRef = ontouml_model.value(object_id, OUTerm.description)
        self.is_abstract: URIRef = ontouml_model.value(object_id, OUTerm.isAbstract)
        self.is_derived: URIRef = ontouml_model.value(object_id, OUTerm.isDerived)
        self.name: URIRef = ontouml_model.value(object_id, OUTerm.name)
        self.relation_end: list[URIRef] = create_list_objects(ontouml_model, object_id, OUTerm.relationEnd)
        self.source_end: URIRef = ontouml_model.value(object_id, OUTerm.sourceEnd)
        self.stereotype: URIRef = ontouml_model.value(object_id, OUTerm.stereotype)
        self.target_end: URIRef = ontouml_model.value(object_id, OUTerm.targetEnd)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)


class OURelationView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ontouml_model.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_model.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_model.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_model.value(object_id, OUTerm.targetView)


class OUText:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.height: URIRef = ontouml_model.value(object_id, OUTerm.height)
        self.project: URIRef = ontouml_model.value(object_id, OUTerm.project)
        self.text: URIRef = ontouml_model.value(object_id, OUTerm.text)
        self.top_left_position: URIRef = ontouml_model.value(object_id, OUTerm.topLeftPosition)
        self.width: URIRef = ontouml_model.value(object_id, OUTerm.width)

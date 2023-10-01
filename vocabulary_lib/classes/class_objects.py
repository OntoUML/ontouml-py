from rdflib import URIRef, Graph

from vocabulary_lib.classes.class_term import OUTerm


class OUProject:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.name: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.name)
        self.diagram: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.diagram)
        self.model: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.model)


class OUDiagram:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.name: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.name)
        self.containsView: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.containsView)
        self.owner: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.owner)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OUCardinality:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.cardinality_value: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.cardinalityValue)
        self.lower_bound: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.lowerBound)
        self.upper_bound: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.upperBound)


class OUClass:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.name: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.name)
        self.attributes: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.attribute)
        self.description: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.description)
        self.is_abstract: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isAbstract)
        self.is_derived: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isDerived)
        self.is_powertype: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isPowertype)
        self.order: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.order)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)
        self.restricted_to: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.restrictedTo)
        self.stereotype: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.stereotype)


class OUGeneralization:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.general: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.general)
        self.specific: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.specific)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OUGeneralizationSet:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.generalization: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.generalization)
        self.is_complete: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isComplete)
        self.is_disjoint: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isDisjoint)
        self.name: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.name)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OUPackage:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.contains_model_element: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.containsModelElement)
        self.name: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.name)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OUProperty:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.aggregation_kind: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.aggregationKind)
        self.cardinality: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.cardinality)
        self.is_derived: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isDerived)
        self.is_ordered: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isOrdered)
        self.is_read_only: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isReadOnly)
        self.name: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.name)
        self.property_type: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.propertyType)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OURelation:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.description: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.description)
        self.is_abstract: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isAbstract)
        self.is_derived: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isDerived)
        self.name: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.name)
        self.relation_end: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.relationEnd)
        self.source_end: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.sourceEnd)
        self.stereotype: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.stereotype)
        self.target_end: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.targetEnd)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OUClassView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isViewOf)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)
        self.shape: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.shape)


class OUGeneralizationSetView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isViewOf)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)
        self.shape: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.shape)


class OUGeneralizationView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isViewOf)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)
        self.shape: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.shape)
        self.source_view: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.sourceView)
        self.target_view: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.targetView)


class OURelationView:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.is_view_of: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.isViewOf)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)
        self.shape: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.shape)
        self.source_view: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.sourceView)
        self.target_view: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.targetView)


class OUPath:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.point: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.point)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OUPoint:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.x_coordinate: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.xCoordinate)
        self.y_coordinate: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.yCoordinate)


class OURectangle:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.top_left_position: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.topLeftPosition)
        self.height: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.height)
        self.width: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.width)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)


class OUText:
    def __init__(self, ontouml_model: Graph, object_id: URIRef):
        self.id: URIRef = object_id
        self.height: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.height)
        self.project: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.project)
        self.text: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.text)
        self.top_left_position: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.topLeftPosition)
        self.width: URIRef = ou_get_element(ontouml_model, object_id, OUTerm.width)

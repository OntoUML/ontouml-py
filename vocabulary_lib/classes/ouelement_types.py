"""This module provides Python classes that represent concepts defined in the OntoUML Vocabulary.
This module provides Python classes for representing and manipulating concepts from the OntoUML Vocabulary.
These Python classes facilitate working with OntoUML concepts and enable you to interact with OntoUML-based data.
Usage:
# Instantiate a class concept from the OntoUML model
person_class = OUClass(ontouml_graph, URIRef("https://example.org/Person"))
# Access attributes of the class
print(f"Class Name: {person_class.name}")
print(f"Description: {person_class.description}")
print(f"Attributes: {person_class.attribute}")
You can perform similar operations for other OntoUML concepts using their respective classes.
"""
from rdflib import URIRef, Graph

from vocabulary_lib.classes._ouelement import _OUElement
from vocabulary_lib.classes.ouexception import OUInvalidAttribute
from vocabulary_lib.classes.outerm import OUTerm

class_map = {
    "OUCardinality": OUTerm.Cardinality,
    "OUClass": OUTerm.Class,
    "OUClassView": OUTerm.ClassView,
    "OUDiagram": OUTerm.Diagram,
    "OUGeneralization": OUTerm.Generalization,
    "OUGeneralizationSet": OUTerm.GeneralizationSet,
    "OUGeneralizationSetView": OUTerm.GeneralizationSetView,
    "OUGeneralizationView": OUTerm.GeneralizationView,
    "OULiteral": OUTerm.Literal,
    "OUNote": OUTerm.Note,
    "OUNoteView": OUTerm.NoteView,
    "OUPackage": OUTerm.Package,
    "OUPackageView": OUTerm.PackageView,
    "OUPath": OUTerm.Path,
    "OUPoint": OUTerm.Point,
    "OUProject": OUTerm.Project,
    "OUProperty": OUTerm.Property,
    "OURectangle": OUTerm.Rectangle,
    "OURelation": OUTerm.Relation,
    "OURelationView": OUTerm.RelationView,
    "OUText": OUTerm.Text,
}


class OUCardinality(_OUElement):
    """Represents cardinality information for a property.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the cardinality object.
    :type object_id: URIRef

    :ivar cardinality_value: The cardinality value.
    :vartype cardinality_value: URIRef
    :ivar lower_bound: The lower bound of the cardinality.
    :vartype lower_bound: URIRef
    :ivar upper_bound: The upper bound of the cardinality.
    :vartype upper_bound: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.cardinality_value: URIRef = ontouml_graph.value(object_id, OUTerm.cardinalityValue)
        self.lower_bound: URIRef = ontouml_graph.value(object_id, OUTerm.lowerBound)
        self.upper_bound: URIRef = ontouml_graph.value(object_id, OUTerm.upperBound)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUClass(_OUElement):
    """Represents a class in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the class.
    :type object_id: URIRef

    :ivar name: The name of the class.
    :vartype name: URIRef
    :ivar attribute: A list of attributes associated with the class.
    :vartype attribute: List[URIRef]
    :ivar description: The description of the class.
    :vartype description: URIRef
    :ivar is_abstract: Indicates if the class is abstract.
    :vartype is_abstract: URIRef
    :ivar is_derived: Indicates if the class is derived.
    :vartype is_derived: URIRef
    :ivar is_powertype: Indicates if the class is a powertype.
    :vartype is_powertype: URIRef
    :ivar literal: The literal associated with the class.
    :vartype literal: URIRef
    :ivar order: The order of the class.
    :vartype order: URIRef
    :ivar project: The project to which the class belongs.
    :vartype project: URIRef
    :ivar restricted_to: A list of classes restricted to this class.
    :vartype restricted_to: List[URIRef]
    :ivar stereotype: The stereotype of the class.
    :vartype stereotype: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.name: URIRef = ontouml_graph.value(object_id, OUTerm.name)
        self.attribute: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.attribute)
        self.description: URIRef = ontouml_graph.value(object_id, OUTerm.description)
        self.is_abstract: URIRef = ontouml_graph.value(object_id, OUTerm.isAbstract)
        self.is_derived: URIRef = ontouml_graph.value(object_id, OUTerm.isDerived)
        self.is_powertype: URIRef = ontouml_graph.value(object_id, OUTerm.isPowertype)
        self.literal: URIRef = ontouml_graph.value(object_id, OUTerm.literal)
        self.order: URIRef = ontouml_graph.value(object_id, OUTerm.order)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.restricted_to: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.restrictedTo)
        self.stereotype: URIRef = ontouml_graph.value(object_id, OUTerm.stereotype)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUClassView(_OUElement):
    """Represents a view of a class in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the class view.
    :type object_id: URIRef

    :ivar is_view_of: The class that this view is associated with.
    :vartype is_view_of: URIRef
    :ivar project: The project to which the class view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the class view.
    :vartype shape: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.is_view_of: URIRef = ontouml_graph.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OUTerm.shape)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUDiagram(_OUElement):
    """Represents a diagram in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the diagram.
    :type object_id: URIRef

    :ivar name: The name of the diagram.
    :vartype name: URIRef
    :ivar containsView: A list of views contained within the diagram.
    :vartype containsView: List[URIRef]
    :ivar owner: The owner of the diagram.
    :vartype owner: URIRef
    :ivar project: The project to which the diagram belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.name: URIRef = ontouml_graph.value(object_id, OUTerm.name)
        self.containsView: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.containsView)
        self.owner: URIRef = ontouml_graph.value(object_id, OUTerm.owner)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUGeneralization(_OUElement):
    """Represents a generalization relationship in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization.
    :type object_id: URIRef

    :ivar general: The general class in the generalization.
    :vartype general: URIRef
    :ivar specific: The specific class in the generalization.
    :vartype specific: URIRef
    :ivar project: The project to which the generalization belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.general: URIRef = ontouml_graph.value(object_id, OUTerm.general)
        self.specific: URIRef = ontouml_graph.value(object_id, OUTerm.specific)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUGeneralizationSet(_OUElement):
    """Represents a generalization set in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization set.
    :type object_id: URIRef

    :ivar generalization: A list of generalizations included in the set.
    :vartype generalization: List[URIRef]
    :ivar is_complete: Indicates if the generalization set is complete.
    :vartype is_complete: URIRef
    :ivar is_disjoint: Indicates if the generalization set is disjoint.
    :vartype is_disjoint: URIRef
    :ivar name: The name of the generalization set.
    :vartype name: URIRef
    :ivar project: The project to which the generalization set belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.generalization: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.generalization)
        self.is_complete: URIRef = ontouml_graph.value(object_id, OUTerm.isComplete)
        self.is_disjoint: URIRef = ontouml_graph.value(object_id, OUTerm.isDisjoint)
        self.name: URIRef = ontouml_graph.value(object_id, OUTerm.name)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUGeneralizationSetView(_OUElement):
    """Represents a view of a generalization set in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization set view.
    :type object_id: URIRef

    :ivar is_view_of: The generalization set that this view is associated with.
    :vartype is_view_of: URIRef
    :ivar project: The project to which the generalization set view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the generalization set view.
    :vartype shape: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.is_view_of: URIRef = ontouml_graph.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OUTerm.shape)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUGeneralizationView(_OUElement):
    """Represents a view of a generalization in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization view.
    :type object_id: URIRef

    :ivar is_view_of: The generalization that this view is associated with.
    :vartype is_view_of: URIRef
    :ivar project: The project to which the generalization view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the generalization view.
    :vartype shape: URIRef
    :ivar source_view: The source view of the generalization.
    :vartype source_view: URIRef
    :ivar target_view: The target view of the generalization.
    :vartype target_view: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.is_view_of: URIRef = ontouml_graph.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_graph.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_graph.value(object_id, OUTerm.targetView)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OULiteral(_OUElement):
    """Represents a literal in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the literal.
    :type object_id: URIRef

    :ivar project: The project to which the literal belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUNote(_OUElement):
    """Represents a note in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the note.
    :type object_id: URIRef

    :ivar text: The text content of the note.
    :vartype text: List[URIRef]
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.text: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.text)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUNoteView(_OUElement):
    """Represents a view of a note in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the note view.
    :type object_id: URIRef

    :ivar is_view_of: The note that this view is associated with.
    :vartype is_view_of: URIRef
    :ivar project: The project to which the note view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the note view.
    :vartype shape: URIRef
    :ivar source_view: The source view of the note.
    :vartype source_view: URIRef
    :ivar target_view: The target view of the note.
    :vartype target_view: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.is_view_of: URIRef = ontouml_graph.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_graph.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_graph.value(object_id, OUTerm.targetView)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUPackage(_OUElement):
    """Represents a package in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the package.
    :type object_id: URIRef

    :ivar contains_model_element: A list of model elements contained within the package.
    :vartype contains_model_element: List[URIRef]
    :ivar name: The name of the package.
    :vartype name: URIRef
    :ivar project: The project to which the package belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.contains_model_element: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.containsModelElement)
        self.name: URIRef = ontouml_graph.value(object_id, OUTerm.name)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUPackageView(_OUElement):
    """Represents a view of a package in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the package view.
    :type object_id: URIRef

    :ivar is_view_of: The package that this view is associated with.
    :vartype is_view_of: URIRef
    :ivar project: The project to which the package view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the package view.
    :vartype shape: URIRef
    :ivar source_view: The source view of the package.
    :vartype source_view: URIRef
    :ivar target_view: The target view of the package.
    :vartype target_view: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.is_view_of: URIRef = ontouml_graph.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_graph.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_graph.value(object_id, OUTerm.targetView)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUPath(_OUElement):
    """Represents a path in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the path.
    :type object_id: URIRef

    :ivar point: A list of points that make up the path.
    :vartype point: List[URIRef]
    :ivar project: The project to which the path belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.point: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.point)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUPoint(_OUElement):
    """Represents a point in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the point.
    :type object_id: URIRef

    :ivar x_coordinate: The x-coordinate of the point.
    :vartype x_coordinate: URIRef
    :ivar y_coordinate: The y-coordinate of the point.
    :vartype y_coordinate: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.x_coordinate: URIRef = ontouml_graph.value(object_id, OUTerm.xCoordinate)
        self.y_coordinate: URIRef = ontouml_graph.value(object_id, OUTerm.yCoordinate)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUProject(_OUElement):
    """Represents a project in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the project.
    :type object_id: URIRef

    :ivar name: The name of the project.
    :vartype name: URIRef
    :ivar diagram: A list of diagrams associated with the project.
    :vartype diagram: List[URIRef]
    :ivar model: The model associated with the project.
    :vartype model: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.name: URIRef = ontouml_graph.value(object_id, OUTerm.name)
        self.diagram: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.diagram)
        self.model: URIRef = ontouml_graph.value(object_id, OUTerm.model)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUProperty(_OUElement):
    """Represents a property in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the property.
    :type object_id: URIRef

    :ivar aggregation_kind: The aggregation kind of the property.
    :vartype aggregation_kind: URIRef
    :ivar cardinality: The cardinality of the property.
    :vartype cardinality: URIRef
    :ivar is_derived: Indicates if the property is derived.
    :vartype is_derived: URIRef
    :ivar is_ordered: Indicates if the property is ordered.
    :vartype is_ordered: URIRef
    :ivar is_read_only: Indicates if the property is read-only.
    :vartype is_read_only: URIRef
    :ivar name: The name of the property.
    :vartype name: URIRef
    :ivar property_type: The type of the property.
    :vartype property_type: URIRef
    :ivar project: The project to which the property belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.aggregation_kind: URIRef = ontouml_graph.value(object_id, OUTerm.aggregationKind)
        self.cardinality: URIRef = ontouml_graph.value(object_id, OUTerm.cardinality)
        self.is_derived: URIRef = ontouml_graph.value(object_id, OUTerm.isDerived)
        self.is_ordered: URIRef = ontouml_graph.value(object_id, OUTerm.isOrdered)
        self.is_read_only: URIRef = ontouml_graph.value(object_id, OUTerm.isReadOnly)
        self.name: URIRef = ontouml_graph.value(object_id, OUTerm.name)
        self.property_type: URIRef = ontouml_graph.value(object_id, OUTerm.propertyType)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OURectangle(_OUElement):
    """Represents a rectangle in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the rectangle.
    :type object_id: URIRef

    :ivar top_left_position: The top-left position of the rectangle.
    :vartype top_left_position: URIRef
    :ivar height: The height of the rectangle.
    :vartype height: URIRef
    :ivar width: The width of the rectangle.
    :vartype width: URIRef
    :ivar project: The project to which the rectangle belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.top_left_position: URIRef = ontouml_graph.value(object_id, OUTerm.topLeftPosition)
        self.height: URIRef = ontouml_graph.value(object_id, OUTerm.height)
        self.width: URIRef = ontouml_graph.value(object_id, OUTerm.width)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OURelation(_OUElement):
    """Represents a relation in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the relation.
    :type object_id: URIRef

    :ivar description: The description of the relation.
    :vartype description: URIRef
    :ivar is_abstract: Indicates if the relation is abstract.
    :vartype is_abstract: URIRef
    :ivar is_derived: Indicates if the relation is derived.
    :vartype is_derived: URIRef
    :ivar name: The name of the relation.
    :vartype name: URIRef
    :ivar relation_end: A list of ends associated with the relation.
    :vartype relation_end: List[URIRef]
    :ivar source_end: The source end of the relation.
    :vartype source_end: URIRef
    :ivar stereotype: The stereotype of the relation.
    :vartype stereotype: URIRef
    :ivar target_end: The target end of the relation.
    :vartype target_end: URIRef
    :ivar project: The project to which the relation belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.description: URIRef = ontouml_graph.value(object_id, OUTerm.description)
        self.is_abstract: URIRef = ontouml_graph.value(object_id, OUTerm.isAbstract)
        self.is_derived: URIRef = ontouml_graph.value(object_id, OUTerm.isDerived)
        self.name: URIRef = ontouml_graph.value(object_id, OUTerm.name)
        self.relation_end: list[URIRef] = ontouml_graph.objects(object_id, OUTerm.relationEnd)
        self.source_end: URIRef = ontouml_graph.value(object_id, OUTerm.sourceEnd)
        self.stereotype: URIRef = ontouml_graph.value(object_id, OUTerm.stereotype)
        self.target_end: URIRef = ontouml_graph.value(object_id, OUTerm.targetEnd)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OURelationView(_OUElement):
    """Represents a view of a relation in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the relation view.
    :type object_id: URIRef

    :ivar is_view_of: The relation that this view is associated with.
    :vartype is_view_of: URIRef
    :ivar project: The project to which the relation view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the relation view.
    :vartype shape: URIRef
    :ivar source_view: The source view associated with the relation view.
    :vartype source_view: URIRef
    :ivar target_view: The target view associated with the relation view.
    :vartype target_view: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.is_view_of: URIRef = ontouml_graph.value(object_id, OUTerm.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OUTerm.shape)
        self.source_view: URIRef = ontouml_graph.value(object_id, OUTerm.sourceView)
        self.target_view: URIRef = ontouml_graph.value(object_id, OUTerm.targetView)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUText(_OUElement):
    """Represents text in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the text.
    :type object_id: URIRef

    :ivar height: The height of the text.
    :vartype height: URIRef
    :ivar project: The project to which the text belongs.
    :vartype project: URIRef
    :ivar text: The text content.
    :vartype text: URIRef
    :ivar top_left_position: The top-left position of the text.
    :vartype top_left_position: URIRef
    :ivar width: The width of the text.
    :vartype width: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.height: URIRef = ontouml_graph.value(object_id, OUTerm.height)
        self.project: URIRef = ontouml_graph.value(object_id, OUTerm.project)
        self.text: URIRef = ontouml_graph.value(object_id, OUTerm.text)
        self.top_left_position: URIRef = ontouml_graph.value(object_id, OUTerm.topLeftPosition)
        self.width: URIRef = ontouml_graph.value(object_id, OUTerm.width)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

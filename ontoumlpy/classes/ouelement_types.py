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
from icecream import ic
from rdflib import URIRef, Graph

from ontoumlpy.classes._ouelement import _OUElement
from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouexception import OUInvalidAttribute

class OUCardinality(_OUElement):
    """Represents cardinality information for a property.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the cardinality object.
    :type object_id: URIRef

    :ivar cardinalityValue: The cardinality value.
    :vartype cardinalityValue: URIRef
    :ivar lowerBound: The lower bound of the cardinality.
    :vartype lowerBound: URIRef
    :ivar upperBound: The upper bound of the cardinality.
    :vartype upperBound: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.cardinalityValue: URIRef = ontouml_graph.value(object_id, OntoUML.cardinalityValue)
        self.lowerBound: URIRef = ontouml_graph.value(object_id, OntoUML.lowerBound)
        self.upperBound: URIRef = ontouml_graph.value(object_id, OntoUML.upperBound)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)





class OUClassView(_OUElement):
    """Represents a view of a class in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the class view.
    :type object_id: URIRef

    :ivar isViewOf: The class that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the class view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the class view.
    :vartype shape: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)

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

        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.containsView: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.containsView))
        self.owner: URIRef = ontouml_graph.value(object_id, OntoUML.owner)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

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

        self.general: URIRef = ontouml_graph.value(object_id, OntoUML.general)
        self.specific: URIRef = ontouml_graph.value(object_id, OntoUML.specific)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

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
    :ivar isComplete: Indicates if the generalization set is complete.
    :vartype isComplete: URIRef
    :ivar isDisjoint: Indicates if the generalization set is disjoint.
    :vartype isDisjoint: URIRef
    :ivar name: The name of the generalization set.
    :vartype name: URIRef
    :ivar project: The project to which the generalization set belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.generalization: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.generalization))
        self.isComplete: URIRef = ontouml_graph.value(object_id, OntoUML.isComplete)
        self.isDisjoint: URIRef = ontouml_graph.value(object_id, OntoUML.isDisjoint)
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUGeneralizationSetView(_OUElement):
    """Represents a view of a generalization set in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization set view.
    :type object_id: URIRef

    :ivar isViewOf: The generalization set that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the generalization set view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the generalization set view.
    :vartype shape: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUGeneralizationView(_OUElement):
    """Represents a view of a generalization in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the generalization view.
    :type object_id: URIRef

    :ivar isViewOf: The generalization that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the generalization view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the generalization view.
    :vartype shape: URIRef
    :ivar sourceView: The source view of the generalization.
    :vartype sourceView: URIRef
    :ivar targetView: The target view of the generalization.
    :vartype targetView: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)
        self.sourceView: URIRef = ontouml_graph.value(object_id, OntoUML.sourceView)
        self.targetView: URIRef = ontouml_graph.value(object_id, OntoUML.targetView)

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

        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

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

        self.text: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.text))

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUNoteView(_OUElement):
    """Represents a view of a note in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the note view.
    :type object_id: URIRef

    :ivar isViewOf: The note that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the note view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the note view.
    :vartype shape: URIRef
    :ivar sourceView: The source view of the note.
    :vartype sourceView: URIRef
    :ivar targetView: The target view of the note.
    :vartype targetView: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)
        self.sourceView: URIRef = ontouml_graph.value(object_id, OntoUML.sourceView)
        self.targetView: URIRef = ontouml_graph.value(object_id, OntoUML.targetView)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUPackage(_OUElement):
    """Represents a package in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the package.
    :type object_id: URIRef

    :ivar containsModelElement: A list of model elements contained within the package.
    :vartype containsModelElement: List[URIRef]
    :ivar name: The name of the package.
    :vartype name: URIRef
    :ivar project: The project to which the package belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.containsModelElement: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.containsModelElement))
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUPackageView(_OUElement):
    """Represents a view of a package in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the package view.
    :type object_id: URIRef

    :ivar isViewOf: The package that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the package view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the package view.
    :vartype shape: URIRef
    :ivar sourceView: The source view of the package.
    :vartype sourceView: URIRef
    :ivar targetView: The target view of the package.
    :vartype targetView: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)
        self.sourceView: URIRef = ontouml_graph.value(object_id, OntoUML.sourceView)
        self.targetView: URIRef = ontouml_graph.value(object_id, OntoUML.targetView)

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

        self.point: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.point))
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUPoint(_OUElement):
    """Represents a point in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the point.
    :type object_id: URIRef

    :ivar xCoordinate: The x-coordinate of the point.
    :vartype xCoordinate: URIRef
    :ivar yCoordinate: The y-coordinate of the point.
    :vartype yCoordinate: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.xCoordinate: URIRef = ontouml_graph.value(object_id, OntoUML.xCoordinate)
        self.yCoordinate: URIRef = ontouml_graph.value(object_id, OntoUML.yCoordinate)

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

        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.diagram: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.diagram))
        self.model: URIRef = ontouml_graph.value(object_id, OntoUML.model)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OUProperty(_OUElement):
    """Represents a property in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the property.
    :type object_id: URIRef

    :ivar aggregationKind: The aggregation kind of the property.
    :vartype aggregationKind: URIRef
    :ivar cardinality: The cardinality of the property.
    :vartype cardinality: URIRef
    :ivar isDerived: Indicates if the property is derived.
    :vartype isDerived: URIRef
    :ivar isOrdered: Indicates if the property is ordered.
    :vartype isOrdered: URIRef
    :ivar isReadOnly: Indicates if the property is read-only.
    :vartype isReadOnly: URIRef
    :ivar name: The name of the property.
    :vartype name: URIRef
    :ivar propertyType: The type of the property.
    :vartype propertyType: URIRef
    :ivar project: The project to which the property belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.aggregationKind: URIRef = ontouml_graph.value(object_id, OntoUML.aggregationKind)
        self.cardinality: URIRef = ontouml_graph.value(object_id, OntoUML.cardinality)
        self.isDerived: URIRef = ontouml_graph.value(object_id, OntoUML.isDerived)
        self.isOrdered: URIRef = ontouml_graph.value(object_id, OntoUML.isOrdered)
        self.isReadOnly: URIRef = ontouml_graph.value(object_id, OntoUML.isReadOnly)
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.propertyType: URIRef = ontouml_graph.value(object_id, OntoUML.propertyType)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OURectangle(_OUElement):
    """Represents a rectangle in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the rectangle.
    :type object_id: URIRef

    :ivar topLeftPosition: The top-left position of the rectangle.
    :vartype topLeftPosition: URIRef
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

        self.topLeftPosition: URIRef = ontouml_graph.value(object_id, OntoUML.topLeftPosition)
        self.height: URIRef = ontouml_graph.value(object_id, OntoUML.height)
        self.width: URIRef = ontouml_graph.value(object_id, OntoUML.width)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

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
    :ivar isAbstract: Indicates if the relation is abstract.
    :vartype isAbstract: URIRef
    :ivar isDerived: Indicates if the relation is derived.
    :vartype isDerived: URIRef
    :ivar name: The name of the relation.
    :vartype name: URIRef
    :ivar relationEnd: A list of ends associated with the relation.
    :vartype relationEnd: List[URIRef]
    :ivar sourceEnd: The source end of the relation.
    :vartype sourceEnd: URIRef
    :ivar stereotype: The stereotype of the relation.
    :vartype stereotype: URIRef
    :ivar targetEnd: The target end of the relation.
    :vartype targetEnd: URIRef
    :ivar project: The project to which the relation belongs.
    :vartype project: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.description: URIRef = ontouml_graph.value(object_id, OntoUML.description)
        self.isAbstract: URIRef = ontouml_graph.value(object_id, OntoUML.isAbstract)
        self.isDerived: URIRef = ontouml_graph.value(object_id, OntoUML.isDerived)
        self.name: URIRef = ontouml_graph.value(object_id, OntoUML.name)
        self.relationEnd: list[URIRef] = list(ontouml_graph.objects(object_id, OntoUML.relationEnd))
        self.sourceEnd: URIRef = ontouml_graph.value(object_id, OntoUML.sourceEnd)
        self.stereotype: URIRef = ontouml_graph.value(object_id, OntoUML.stereotype)
        self.targetEnd: URIRef = ontouml_graph.value(object_id, OntoUML.targetEnd)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


class OURelationView(_OUElement):
    """Represents a view of a relation in OntoUML.

    :param ontouml_graph: The OntoUML model graph.
    :type ontouml_graph: Graph
    :param object_id: The URI reference of the relation view.
    :type object_id: URIRef

    :ivar isViewOf: The relation that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the relation view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the relation view.
    :vartype shape: URIRef
    :ivar sourceView: The source view associated with the relation view.
    :vartype sourceView: URIRef
    :ivar targetView: The target view associated with the relation view.
    :vartype targetView: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.isViewOf: URIRef = ontouml_graph.value(object_id, OntoUML.isViewOf)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.shape: URIRef = ontouml_graph.value(object_id, OntoUML.shape)
        self.sourceView: URIRef = ontouml_graph.value(object_id, OntoUML.sourceView)
        self.targetView: URIRef = ontouml_graph.value(object_id, OntoUML.targetView)

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
    :ivar topLeftPosition: The top-left position of the text.
    :vartype topLeftPosition: URIRef
    :ivar width: The width of the text.
    :vartype width: URIRef
    """

    def __init__(self, ontouml_graph: Graph, object_id: URIRef):
        class_name = self.__class__.__name__
        related_type = class_map[class_name]
        super().__init__(ontouml_graph, object_id, class_name, related_type)

        self.height: URIRef = ontouml_graph.value(object_id, OntoUML.height)
        self.project: URIRef = ontouml_graph.value(object_id, OntoUML.project)
        self.text: URIRef = ontouml_graph.value(object_id, OntoUML.text)
        self.topLeftPosition: URIRef = ontouml_graph.value(object_id, OntoUML.topLeftPosition)
        self.width: URIRef = ontouml_graph.value(object_id, OntoUML.width)

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)


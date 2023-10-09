from rdflib import URIRef

from ontoumlpy.classes._ouelement import _OUElement
from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouexception import OUInvalidAttribute


class OUClass(_OUElement):
    """A class representing an OntoUML Class element.

    The `OUClass` extends `_OUElement` and further specializes it for OntoUML Class elements. It gathers relevant data
    from the OntoUML graph and provides an interface to access the class-specific properties.


    :ivar name: The name of the class.
    :vartype name: URIRef
    :ivar attribute: A list of attributes associated with the class.
    :vartype attribute: List[URIRef]
    :ivar description: The description of the class.
    :vartype description: URIRef
    :ivar isAbstract: Indicates if the class is abstract.
    :vartype isAbstract: URIRef
    :ivar isDerived: Indicates if the class is derived.
    :vartype isDerived: URIRef
    :ivar isPowertype: Indicates if the class is a powertype.
    :vartype isPowertype: URIRef
    :ivar literal: The literal associated with the class.
    :vartype literal: URIRef
    :ivar order: The order of the class.
    :vartype order: URIRef
    :ivar project: The project to which the class belongs.
    :vartype project: URIRef
    :ivar restrictedTo: A list of classes restricted to this class.
    :vartype restrictedTo: List[URIRef]
    :ivar stereotype: The stereotype of the class.
    :vartype stereotype: URIRef
    """

    def __init__(self, object_id: URIRef, name: URIRef = None, description: URIRef = None, isAbstract: URIRef = None,
                 isDerived: URIRef = None, isPowertype: URIRef = None, literal: URIRef = None, order: URIRef = None,
                 project: URIRef = None, stereotype: URIRef = None, attribute: list[URIRef] = None,
                 restrictedTo: list[URIRef] = None, ):
        """
        :param ontouml_graph: The OntoUML model graph.
        :type ontouml_graph: Graph
        :param object_id: The URI reference of the class.
        :type object_id: URIRef
        """
        related_type = OntoUML.Class
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        # Attributes of type URIRef
        self.isAbstract: URIRef = isAbstract
        self.isDerived: URIRef = isDerived
        self.isPowertype: URIRef = isPowertype
        self.literal: URIRef = literal
        self.order: URIRef = order
        self.project: URIRef = project
        self.stereotype: URIRef = stereotype

        # Attributes of type list[URIRef]
        self.attribute: list[URIRef] = attribute
        self.restrictedTo: list[URIRef] = restrictedTo

    def __getattr__(self, invalid_att_name):
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

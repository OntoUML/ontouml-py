from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUClass(_OUElement):
    """Class representing an OntoUML Class element with facilities to manage and access class properties.

    `OUClass`, derived from `_OUElement`, further specializes the base class to facilitate representation and
    manipulation of OntoUML Class elements. It does not verify the existence or validity of the provided URI references
    within an OntoUML graph, delegating such checks to potential subclasses or external utility functions.

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

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        description: URIRef = None,
        isAbstract: URIRef = None,
        isDerived: URIRef = None,
        isPowertype: URIRef = None,
        literal: URIRef = None,
        order: URIRef = None,
        project: URIRef = None,
        stereotype: URIRef = None,
        attribute: list[URIRef] = None,
        restrictedTo: list[URIRef] = None,
    ) -> None:
        """Instantiate an OUClass with the given parameters, initializing all the object attributes.

        :param object_id: The URI reference representing the class.
        :type object_id: URIRef
        :param name: The name of the class, optional, default is None.
        :type name: URIRef, optional
        :param description: A textual description of the class, optional, default is None.
        :type description: URIRef, optional
        :param isAbstract: Indicates if the class is abstract, optional, default is None.
        :type isAbstract: URIRef, optional
        :param isDerived: Indicates if the class is derived, optional, default is None.
        :type isDerived: URIRef, optional
        :param isPowertype: Indicates if the class is a powertype, optional, default is None.
        :type isPowertype: URIRef, optional
        :param literal: The literal associated with the class, optional, default is None.
        :type literal: URIRef, optional
        :param order: The order of the class, optional, default is None.
        :type order: URIRef, optional
        :param project: The project to which the class belongs, optional, default is None.
        :type project: URIRef, optional
        :param stereotype: The stereotype of the class, optional, default is None.
        :type stereotype: URIRef, optional
        :param attribute: A list of attributes associated with the class, optional, default is None.
        :type attribute: List[URIRef], optional
        :param restrictedTo: A list of classes restricted to this class, optional, default is None.
        :type restrictedTo: List[URIRef], optional
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

    def __getattr__(self, invalid_att_name) -> None:
        """Override to raise an exception when attempting to access an invalid attribute.

        :param invalid_att_name: The name of the invalid attribute being accessed.
        :type invalid_att_name: str
        :raises OUInvalidAttribute: In all cases, as intended to flag invalid attribute access.
        """
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

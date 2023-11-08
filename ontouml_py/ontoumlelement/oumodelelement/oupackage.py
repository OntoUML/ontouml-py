from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUPackage(_OUElement):
    """Represents a package in OntoUML.

    :param object_id: The URI reference of the package.
    :type object_id: URIRef

    :ivar containsModelElement: A list of model elements contained within the package.
    :vartype containsModelElement: List[URIRef]
    :ivar name: The name of the package.
    :vartype name: URIRef
    :ivar project: The project to which the package belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        project: URIRef = None,
        containsModelElement: list[URIRef] = None,
        name: URIRef = None,
        description: URIRef = None,
    ) -> None:
        related_type = OntoUML.Package
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.containsModelElement: list[URIRef] = containsModelElement
        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

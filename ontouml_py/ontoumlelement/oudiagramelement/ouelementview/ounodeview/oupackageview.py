from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUPackageView(_OUElement):
    """Represents a view of a package in OntoUML.



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

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        description: URIRef = None,
        isViewOf: URIRef = None,
        project: URIRef = None,
        shape: URIRef = None,
        sourceView: URIRef = None,
        targetView: URIRef = None,
    ) -> None:
        related_type = OntoUML.PackageView
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.isViewOf: URIRef = isViewOf
        self.project: URIRef = project
        self.shape: URIRef = shape
        self.sourceView: URIRef = sourceView
        self.targetView: URIRef = targetView

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

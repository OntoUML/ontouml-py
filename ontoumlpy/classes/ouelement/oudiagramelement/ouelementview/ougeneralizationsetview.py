from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouexception import OUInvalidAttribute


class OUGeneralizationSetView(_OUElement):
    """Represents a view of a generalization set in OntoUML.



    :param object_id: The URI reference of the generalization set view.
    :type object_id: URIRef

    :ivar isViewOf: The generalization set that this view is associated with.
    :vartype isViewOf: URIRef
    :ivar project: The project to which the generalization set view belongs.
    :vartype project: URIRef
    :ivar shape: The shape of the generalization set view.
    :vartype shape: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        description: URIRef = None,
        isViewOf: URIRef = None,
        project: URIRef = None,
        shape: URIRef = None,
    ) -> None:
        related_type = OntoUML.GeneralizationView
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.isViewOf: URIRef = isViewOf
        self.project: URIRef = project
        self.shape: URIRef = shape

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)
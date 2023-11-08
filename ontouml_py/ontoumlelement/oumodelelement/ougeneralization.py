from rdflib import URIRef

from ontouml_py.classes.ontouml import OntoUML
from ontouml_py.classes.ontoumlelement import _OUElement
from ontouml_py.classes.ouexception import OUInvalidAttribute


class OUGeneralization(_OUElement):
    """Represents a generalization relationship in OntoUML.



    :param object_id: The URI reference of the generalization.
    :type object_id: URIRef

    :ivar general: The general class in the generalization.
    :vartype general: URIRef
    :ivar specific: The specific class in the generalization.
    :vartype specific: URIRef
    :ivar project: The project to which the generalization belongs.
    :vartype project: URIRef
    """

    def __init__(
        self,
        object_id: URIRef,
        name: URIRef = None,
        description: URIRef = None,
        general: URIRef = None,
        specific: URIRef = None,
        project: URIRef = None,
    ) -> None:
        related_type = OntoUML.Generalization
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.general: URIRef = general
        self.specific: URIRef = specific
        self.project: URIRef = project

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

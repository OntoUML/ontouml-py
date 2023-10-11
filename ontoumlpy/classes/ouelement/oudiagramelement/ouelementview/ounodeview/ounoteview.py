from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouexception import OUInvalidAttribute


class OUNoteView(_OUElement):
    """Represents a view of a note in OntoUML.



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

    def __init__(
        self,
        object_id: URIRef,
        isViewOf: URIRef = None,
        name: URIRef = None,
        description: URIRef = None,
        project: URIRef = None,
        shape: URIRef = None,
        sourceView: URIRef = None,
        targetView: URIRef = None,
    ) -> None:
        related_type = OntoUML.NoteView
        super().__init__(object_id=object_id, related_type=related_type, name=name, description=description)

        self.isViewOf: URIRef = isViewOf
        self.project: URIRef = project
        self.shape: URIRef = shape
        self.sourceView: URIRef = sourceView
        self.targetView: URIRef = targetView

    def __getattr__(self, invalid_att_name) -> None:
        raise OUInvalidAttribute(self.__class__.__name__, invalid_att_name)

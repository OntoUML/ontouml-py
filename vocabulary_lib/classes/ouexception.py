"""Module for handling custom exceptions related to OntoUML."""
from rdflib import URIRef


class OUIDNotInGraph(ValueError):
    """Custom exception for handling cases where the provided ID does not exist in the OntoUML graph.

    :param absent_ou_id: The ID that does not exist in the OntoUML graph.
    :type absent_ou_id: URIRef
    :param ou_class_name: The name of the OntoUML class being instantiated.
    :type ou_class_name: str
    """

    def __init__(self, absent_ou_id: URIRef, ou_class_name: str):
        message = (f"The id '{absent_ou_id}' used to instantiate '{ou_class_name}' does not "
                   f"exist in the OntoUML graph. Software execution aborted.")
        super().__init__(message)


class OUIDTypeMismatchError(ValueError):
    """Custom exception for handling cases where the provided ID exists but has a type mismatch with the expected type.

    :param absent_ou_id: The ID that exists but has a type mismatch.
    :type absent_ou_id: URIRef
    :param ou_class_name: The name of the OntoUML class being instantiated.
    :type ou_class_name: str
    :param related_type: The expected type for the ID.
    :type related_type: URIRef
    """

    def __init__(self, absent_ou_id: URIRef, ou_class_name: str, related_type: URIRef):
        message = (f"The id '{absent_ou_id}' used to instantiate '{ou_class_name}' is not "
                   f" an element of type '{related_type}'. Software execution aborted.")
        super().__init__(message)


class OUInvalidAttribute(NameError):
    def __init__(self, ou_class_name: str, invalid_att_name: str):
        message = (f"The '{ou_class_name}' does not have an attribute '{invalid_att_name}'. "
                   f"Software execution aborted.")
        super().__init__(message)

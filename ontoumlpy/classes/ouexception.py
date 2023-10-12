"""Module for handling custom exceptions related to OntoUML.

This module provides a set of custom exceptions designed for handling various error scenarios
that may occur in the manipulation and management of OntoUML graphs and related operations.
Each exception is designed to provide clear, user-friendly error messages to assist in
debugging and issue resolution.
"""
from icecream import ic
from rdflib import URIRef


class OUIDNotInGraph(ValueError):
    """Custom exception for handling cases where the provided ID does not exist in the OntoUML graph.

    :param absent_ou_id: The ID that does not exist in the OntoUML graph.
    :type absent_ou_id: URIRef
    :param ou_class_name: The name of the OntoUML class being instantiated.
    :type ou_class_name: str
    """

    def __init__(self, absent_ou_id: URIRef, ou_class_name: str):
        message = (
            f"The id '{absent_ou_id}' used to instantiate '{ou_class_name}' does not exist in the OntoUML graph. "
            f"Software execution aborted."
        )
        super().__init__(message)


class OUIDTypeMismatchError(ValueError):
    """Custom exception for handling cases where the provided ID exists but has a type mismatch with the expected type.

    :param mismatched_ou_id: The ID that exists but has a type mismatch.
    :type mismatched_ou_id: URIRef
    :param ou_class_name: The name of the OntoUML class being instantiated.
    :type ou_class_name: str
    :param related_type: The expected type for the ID.
    :type related_type: URIRef
    """

    def __init__(self, mismatched_ou_id: URIRef, ou_class_name: str, related_type: URIRef):
        message = (
            f"The id '{mismatched_ou_id}' used to instantiate '{ou_class_name}' is not an element of "
            f"type '{related_type}'. Software execution aborted."
        )
        super().__init__(message)


class OUInvalidAttribute(NameError):
    """Custom exception for handling cases where an invalid attribute is accessed on an OntoUML class.

    :param ou_class_name: The name of the OntoUML class where the invalid attribute was accessed.
    :type ou_class_name: str
    :param invalid_att_name: The name of the invalid attribute that was accessed.
    :type invalid_att_name: str
    """

    def __init__(self, ou_class_name: str, invalid_att_name: str):
        message = f"The '{ou_class_name}' does not have an attribute '{invalid_att_name}'. Software execution aborted."
        super().__init__(message)


class OUUnmappedOUElement(KeyError):
    """Custom exception for handling cases where an OUElement does not have a mapped OUTerm.

    :param ouelement: The OUElement that does not have a mapped OUTerm.
    :type ouelement: str
    """

    def __init__(self, ouelement):
        message = f"The OUElement '{ouelement}' does not have a mapped OUTerm. Software execution aborted."
        super().__init__(message)


class OUUnmappedOUTerm(Exception):
    """Custom exception for handling cases where an OUTerm does not have a mapped OUElement.

    :param outerm: The OUTerm that does not have a mapped OUElement.
    :type outerm: str
    """

    def __init__(self, outerm):
        message = f"The OUTerm '{outerm}' does not have a mapped OUElement. Software execution aborted."
        super().__init__(message)


class OUUnavailableOUTerm(ValueError):
    """Custom exception for handling cases where an OUTerm is unavailable in the OntoUML Vocabulary.

    This exception is raised when a given OUTerm does not exist or is not found in the OntoUML
    Vocabulary, providing clear feedback that the requested term is unavailable or incorrectly
    specified.

    :param outerm: The OUTerm that does not exist in the OntoUML Vocabulary.
    :type outerm: str
    """

    def __init__(self, outerm: str):
        ic("here")
        message = f"The OUTerm '{outerm}' does not exist in the OntoUML Vocabulary."
        super().__init__(message)

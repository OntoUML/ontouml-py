"""Module for handling custom exceptions related to OntoUML.

This module provides a set of custom exceptions designed for handling various error scenarios
that may occur in the manipulation and management of OntoUML graphs and related operations.
Each exception is designed to provide clear, user-friendly error messages to assist in
debugging and issue resolution.
"""
from rdflib import URIRef


class OUInvalidAttribute(NameError):
    """Custom exception for handling cases where an invalid attribute is accessed on an OntoUML class.

    :param ou_class_name: The name of the OntoUML class where the invalid attribute was accessed.
    :type ou_class_name: str
    :param invalid_att_name: The name of the invalid attribute that was accessed.
    :type invalid_att_name: str
    """

    def __init__(self, ou_class_name: str, invalid_att_name: str) -> None:
        message = f"The '{ou_class_name}' does not have an attribute '{invalid_att_name}'. Software execution aborted."
        super().__init__(message)


class OUUnmappedOUTerm(KeyError):
    """Custom exception for handling cases where an OUElement does not have a mapped OUTerm.

    :param ou_element: The OUElement that does not have a mapped OUTerm.
    :type ou_element: str
    """

    def __init__(self, ou_element) -> None:
        message = f"The OUElement '{ou_element}' does not have a mapped OUTerm. Software execution aborted."
        super().__init__(message)


class OUUnmappedOUElement(Exception):
    """Custom exception for handling cases where an OUTerm does not have a mapped OUElement.

    :param ou_term: The OUTerm that does not have a mapped OUElement.
    :type ou_term: str
    """

    def __init__(self, ou_term) -> None:
        message = f"The OUTerm '{ou_term}' does not have a mapped OUElement. Software execution aborted."
        super().__init__(message)


class OUUnavailableOUTerm(ValueError):
    """Custom exception for handling cases where an OUTerm is unavailable in the OntoUML Vocabulary.

    This exception is raised when a given OUTerm does not exist or is not found in the OntoUML
    Vocabulary, providing clear feedback that the requested term is unavailable or incorrectly
    specified.

    :param outerm: The OUTerm that does not exist in the OntoUML Vocabulary.
    :type outerm: str
    """

    def __init__(self, outerm: str) -> None:
        message = f"The OUTerm '{outerm}' does not exist in the OntoUML Vocabulary."
        super().__init__(message)


class OUInvalidOUElementType(KeyError):
    """Exception raised for unmapped OUElement types to OUGraph internal list.

    This exception is thrown when an OUElement is not mapped to an internal list within the OUGraph, indicating a
    misalignment or absence of mapping definitions within the graph management logic.

    :param ou_element: The OUElement that is not mapped in the OUGraph.
    :type ou_element: URIRef
    """

    def __init__(self, ou_element_type: URIRef) -> None:
        message = (
            f"The OUElement '{ou_element_type}' is not mapped to an OUGraph internal list."
            f"Software execution aborted."
        )
        super().__init__(message)

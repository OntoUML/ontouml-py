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
        message = f"The '{ou_class_name}' does not have an attribute '{invalid_att_name}'."
        super().__init__(message)


class OUUnavailableTerm(ValueError):
    """Custom exception for handling cases where an OUTerm is unavailable in the OntoUML Vocabulary.

    This exception is raised when a given OUTerm does not exist or is not found in the OntoUML
    Vocabulary, providing clear feedback that the requested term is unavailable or incorrectly
    specified.

    :param ou_term: The OUTerm that does not exist in the OntoUML Vocabulary.
    :type ou_term: str
    """

    def __init__(self, ou_term: str) -> None:
        message = f"The OUTerm '{ou_term}' does not exist in the OntoUML Vocabulary."
        super().__init__(message)


class OUInvalidElementType(KeyError):
    """Exception raised for unmapped OUElement types to OUGraph internal list.

    This exception is thrown when an OUElement is not mapped to an internal list within the OUGraph, indicating a
    misalignment or absence of mapping definitions within the graph management logic.

    :param ou_element_type: The OUElement that is not mapped in the OUGraph.
    :type ou_element_type: URIRef
    """

    def __init__(self, ou_element_type: URIRef) -> None:
        message = f"The OUElement '{ou_element_type}' is not mapped to an OUGraph internal list."
        super().__init__(message)


class InvalidOntoUMLTypeException(Exception):
    """Exception raised when an individual is not from a valid OntoUML type.

    This exception is designed to provide clear, actionable feedback about issues related to the usage of invalid
    OntoUML types within operations and manipulations of OntoUML graphs. The error message highlights the problematic
    OntoUML type, aiding in quick debugging and resolution.

    :param ou_element_type: The OntoUML element type that is invalid or not recognized.
    :type ou_element_type: URIRef
    """

    def __init__(self, ou_element_type: URIRef) -> None:
        message = f"The '{ou_element_type}' is not a valid OntoUML element type."
        super().__init__(message)

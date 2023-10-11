"""This module handles the mapping between OntoUML terms and OUElement objects.

It provides functions to retrieve OUElement objects from OntoUML terms and vice versa.
"""
from rdflib import URIRef

from ontoumlpy.classes.ouelement._ouelement import _OUElement
from ontoumlpy.classes.ouexception import OUUnmappedOUElement, OUUnmappedOUTerm


def ou_get_term_from_element(ouelement: _OUElement | str) -> URIRef:
    """Return the corresponding OUTerm object for a given OUElement object or its class name as a string.

    This function iterates through the mapping dictionary to find the corresponding OUTerm object.
    Every OUElement object is assumed to be mapped to an OUTerm object.

    :param ouelement: The OUElement object or its class name as a string.
    :type ouelement: Union[_OUElement, str]
    :raises OUUnmappedOUElement: If the OUElement object is not found in the mapping.
    :return: The corresponding OUTerm object.
    :rtype: URIRef
    """

    if isinstance(ouelement, str):
        for key, value in _OU_MAP_TERM_ELEMENT.items():
            if value.__name__ == ouelement:
                return key
    elif isinstance(ouelement, _OUElement):
        ouelement_class = type(ouelement)  # Get the class of the ouelement instance
        for key, value in _OU_MAP_TERM_ELEMENT.items():
            if value == ouelement_class:
                return key

    # Every OUElement is mapped to an OUTerm, hence, this exception must never happen.
    # If the target value is not found, raise an exception.
    raise OUUnmappedOUElement(ouelement)


def get_related_element(cls, ontouml_term: URIRef | str) -> _OUElement:
    """Return the corresponding OUElement object for a given OUTerm or URIRef/str object.

    If the input is a string, it's converted to a URIRef object before lookup.

    :param ontouml_term: The OUTerm object or URIRef/str representing the term.
    :type ontouml_term: Union[URIRef, str]
    :raises OUUnmappedOUTerm: If the OUTerm object is not found in the mapping.
    :return: The corresponding OUElement object.
    :rtype: _OUElement
    """
    if isinstance(ontouml_term, str):
        ontouml_term = URIRef(ontouml_term)

    try:
        return cls._OU_MAP_TERM_ELEMENT[ontouml_term]
    # Overwrites default KeyError
    except KeyError:
        raise OUUnmappedOUTerm(ontouml_term)

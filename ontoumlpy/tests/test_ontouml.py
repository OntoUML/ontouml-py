"""This module contains a series of tests to validate the mapping and type correctness of the OntoUML class
which represents OntoUML vocabulary terms as URI references.
"""
import pytest
from rdflib import URIRef

from ..classes.ontouml import OntoUML
from ..constants.const_prefix import ONTOUML_NAMESPACE


@pytest.mark.parametrize(
    "ou_term,term",
    [
        (OntoUML.literal, "literal"),
        (OntoUML.Literal, "Literal"),
        (OntoUML.name, "name"),
        (OntoUML.participational, "participational"),
        (OntoUML.role, "role"),
    ],
)
def test_valid_ontouml_uri_mapping(ou_term: URIRef, term: str) -> None:
    """Tests the correct URI mapping of the specified OntoUML instances.

    :param ou_term: The OntoUML instance to be tested.
    :type ou_term: URIRef
    :param term: The string representation of the OntoUML term.
    :type term: str
    """
    assert str(ou_term) == ONTOUML_NAMESPACE + term


@pytest.mark.parametrize(
    "ou_term,term",
    [
        (OntoUML.literal, " literal"),
        (OntoUML.Literal, "literal"),
        (OntoUML.name, "Name"),
        (OntoUML.participational, "Participational"),
        (OntoUML.role, "role "),
    ],
)
def test_invalid_ontouml_uri_mapping(ou_term: URIRef, term: str) -> None:
    """Tests for incorrect URI mappings of the specified OntoUML instances.

    :param ou_term: The OntoUML instance to be tested.
    :type ou_term: URIRef
    :param term: The string representation of the OntoUML term.
    :type term: str
    """
    assert str(ou_term) != ONTOUML_NAMESPACE + term


@pytest.mark.parametrize(
    "ou_term", [(OntoUML.type), (OntoUML.subkind), (OntoUML.situation), (OntoUML.qualityNature), (OntoUML.ModelElement)]
)
def test_valid_ontouml_type(ou_term: URIRef) -> None:
    """Verifies the type correctness of the specified OntoUML instances.

    :param ou_term: The OntoUML instance to be tested.
    :type ou_term: URIRef
    """
    assert isinstance(ou_term, str)
    assert isinstance(ou_term, URIRef)


@pytest.mark.parametrize(
    "ou_term", [(OntoUML.phase), (OntoUML.lowerBound), (OntoUML.instantiation), (OntoUML.end), (OntoUML.DecoratableElement)]
)
def test_valid_ontouml_attribute_access(ou_term: URIRef) -> None:
    """Verifies that valid attributes can be accessed without raising an AttributeError for the specified OntoUML \
    instances.

    :param ou_term: The OntoUML instance to be tested.
    :type ou_term: URIRef
    """
    try:
        ou_term
    except AttributeError:
        assert False
    assert True


@pytest.mark.parametrize(
    "ou_term",
    [(OntoUML.isAbstract), (OntoUML.cardinalityValue), (OntoUML.begin), (OntoUML.GeneralizationView), (OntoUML.isViewOf)],
)
def test_invalid_ontouml_attribute_error(ou_term: URIRef) -> None:
    """Verifies that invalid attributes raise an AttributeError when accessed for the specified OntoUML instances.

    :param ou_term: The OntoUML instance to be tested.
    :type ou_term: URIRef
    """
    try:
        ou_term
    except AttributeError:
        assert True


@pytest.mark.parametrize("term", [("width"), ("mode"), ("model"), ("stereotype"), ("Stereotype")])
def test_valid_ontouml_attribute_existence(term: str) -> None:
    """Verifies that specified attributes exist in OntoUML and that they have the expected type.

    :param term: The attribute name to be checked.
    :type term: str
    """

    assert hasattr(OntoUML, term)


@pytest.mark.parametrize("term", [("ma_terial"), (" Package"), ("owner "), ("isReDdOnly"), ("historicaldependence")])
def test_invalid_ontouml_attribute_absence(term: str) -> None:
    """Verifies that specified invalid attributes do not exist in OntoUML.

    :param term: The attribute name to be checked.
    :type term: str
    """
    assert not (hasattr(OntoUML, term))


def test_list_all_method_valid_ontouml_attribute_existence() -> None:
    """Verifies if the list_all method returns valid terms and that these terms have the expected type."""

    list_terms = OntoUML.list_all()

    for term in list_terms:
        assert hasattr(OntoUML, term)
        assert isinstance(term, URIRef)


def test_list_all_method_is_empty() -> None:
    """Verifies if the list_all method returns is not empty."""

    list_terms = OntoUML.list_all()

    assert len(list_terms) != 0

def test_list_all_number()->None:
    """Verifies if the list all method returns the same number of items as the class attribute number."""

    assert len(dir(OntoUML)) == len(OntoUML.list_all())
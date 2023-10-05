"""This module contains a series of tests to validate the mapping and type correctness of the OUTerm class
which represents OntoUML vocabulary terms as URI references.
"""
import pytest
from rdflib import URIRef

from ..classes.outerm import OUTerm
from ..constants.const_prefix import ONTOUML_NAMESPACE


@pytest.mark.parametrize(
    "ou_term,term",
    [
        (OUTerm.literal, "literal"),
        (OUTerm.Literal, "Literal"),
        (OUTerm.name, "name"),
        (OUTerm.participational, "participational"),
        (OUTerm.role, "role"),
    ],
)
def test_valid_outerm_uri_mapping(ou_term: URIRef, term: str) -> None:
    """Tests the correct URI mapping of the specified OUTerm instances.

    :param ou_term: The OUTerm instance to be tested.
    :type ou_term: URIRef
    :param term: The string representation of the OntoUML term.
    :type term: str
    """
    assert str(ou_term) == ONTOUML_NAMESPACE + term


@pytest.mark.parametrize(
    "ou_term,term",
    [
        (OUTerm.literal, " literal"),
        (OUTerm.Literal, "literal"),
        (OUTerm.name, "Name"),
        (OUTerm.participational, "Participational"),
        (OUTerm.role, "role "),
    ],
)
def test_invalid_outerm_uri_mapping(ou_term: URIRef, term: str) -> None:
    """Tests for incorrect URI mappings of the specified OUTerm instances.

    :param ou_term: The OUTerm instance to be tested.
    :type ou_term: URIRef
    :param term: The string representation of the OntoUML term.
    :type term: str
    """
    assert str(ou_term) != ONTOUML_NAMESPACE + term


@pytest.mark.parametrize(
    "ou_term", [(OUTerm.type), (OUTerm.subkind), (OUTerm.situation), (OUTerm.qualityNature), (OUTerm.ModelElement)]
)
def test_valid_outerm_type(ou_term: URIRef) -> None:
    """Verifies the type correctness of the specified OUTerm instances.

    :param ou_term: The OUTerm instance to be tested.
    :type ou_term: URIRef
    """
    assert isinstance(ou_term, str)
    assert isinstance(ou_term, URIRef)


@pytest.mark.parametrize(
    "ou_term", [(OUTerm.phase), (OUTerm.lowerBound), (OUTerm.instantiation), (OUTerm.end), (OUTerm.DecoratableElement)]
)
def test_valid_outerm_attribute_access(ou_term: URIRef) -> None:
    """Verifies that valid attributes can be accessed without raising an AttributeError for the specified OUTerm \
    instances.

    :param ou_term: The OUTerm instance to be tested.
    :type ou_term: URIRef
    """
    try:
        ou_term
    except AttributeError:
        assert False
    assert True


@pytest.mark.parametrize(
    "ou_term",
    [(OUTerm.isAbstract), (OUTerm.cardinalityValue), (OUTerm.begin), (OUTerm.GeneralizationView), (OUTerm.isViewOf)],
)
def test_invalid_outerm_attribute_error(ou_term: URIRef) -> None:
    """Verifies that invalid attributes raise an AttributeError when accessed for the specified OUTerm instances.

    :param ou_term: The OUTerm instance to be tested.
    :type ou_term: URIRef
    """
    try:
        ou_term
    except AttributeError:
        assert True


@pytest.mark.parametrize("term", [("width"), ("mode"), ("model"), ("stereotype"), ("Stereotype")])
def test_valid_outerm_attribute_existence(term: str) -> None:
    """Verifies that specified attributes exist in OUTerm and that they have the expected type.

    :param term: The attribute name to be checked.
    :type term: str
    """

    assert hasattr(OUTerm, term)


@pytest.mark.parametrize("term", [("ma_terial"), (" Package"), ("owner "), ("isReDdOnly"), ("historicaldependence")])
def test_invalid_outerm_attribute_absence(term: str) -> None:
    """Verifies that specified invalid attributes do not exist in OUTerm.

    :param term: The attribute name to be checked.
    :type term: str
    """
    assert not (hasattr(OUTerm, term))


def test_all_method_valid_outerm_attribute_existence() -> None:
    """Verifies if the all method returns valid terms and that these terms have the expected type."""

    list_terms = OUTerm.all()

    for term in list_terms:
        assert hasattr(OUTerm, term)
        assert isinstance(term, URIRef)


def test_all_method_is_empty() -> None:
    """Verifies if the all method returns is empty."""

    list_terms = OUTerm.all()

    assert len(list_terms) != 0

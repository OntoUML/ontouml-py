"""Module for testing exclusively the attributes of the OntoUML class."""
import pytest
from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.tests.test_ontouml.fixtures_test_ontouml import ALL_TERMS_STR, OK_BASE_URI, NOK_BASE_URI


def test_list_all_method_valid_ontouml_attribute_existence() -> None:
    """Verifies if the list_all method returns valid terms and that these terms have the expected type."""

    list_terms = OntoUML.list_all()

    for term in list_terms:
        assert hasattr(OntoUML, term)


@pytest.mark.parametrize("term", ALL_TERMS_STR)
def test_valid_term_in_ontouml_list(term: str) -> None:
    """Verifies if a term exists in the list returned by OntoUML.list_all().

    :param term: A term to be checked.
    :type term: str
    """
    list_terms = OntoUML.list_all()

    assert URIRef(term) in list_terms


def test_list_all_returns_correct_number_of_items() -> None:
    """Verifies if OntoUML.list_all() returns the same number of items as both the class attribute number
    and the length of ALL_TERMS_STR.
    """
    assert len(dir(OntoUML)) == len(OntoUML.list_all())
    assert len(ALL_TERMS_STR) == len(OntoUML.list_all())


def test_list_all_returns_valid_uriref_list() -> None:
    """
    Validates that OntoUML.list_all() returns a valid list of URIRef objects.

    Ensures that:
    - The return type from OntoUML.list_all() is a list.
    - The returned list is not None.
    - Every term in the list is an instance of URIRef.
    - No term in the list is None.
    """
    list_terms = OntoUML.list_all()
    assert isinstance(list_terms, list)
    assert list_terms is not None

    for term in list_terms:
        assert isinstance(term, URIRef)
        assert term is not None


def test_list_all_terms_include_correct_base_uri() -> None:
    """Ensures each term in OntoUML.list_all() contains the correct base URI and avoids incorrect ones.

    Verifies that:
    - Each term contains OK_BASE_URI.
    - NOK_BASE_URI is not contained in any term.
    """
    list_terms = OntoUML.list_all()

    for term in list_terms:
        assert OK_BASE_URI in term
        assert NOK_BASE_URI not in term


@pytest.mark.parametrize(
    "in_arg",
    [
        " ",
        "str",
        b"some_byte_string",
        10,
        10.1,
        None,
        False,
        True,
        "_",
        (10, 2),
        [1, 2],
        {},
        {"key": "value"},
        1 + 2j,
        bytearray([65, 66, 67]),
        {1, 2, 3},
        frozenset([1, 2, 3]),
    ],
)
def test_list_all_raises_typeerror_with_arguments(in_arg) -> None:
    """Verifies that OntoUML.list_all() raises a TypeError when provided with an argument.

    :param in_arg: An argument to be passed to OntoUML.list_all().
    :type in_arg: Any
    """
    with pytest.raises(TypeError):
        OntoUML.list_all(in_arg)

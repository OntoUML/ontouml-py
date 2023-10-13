"""Module for testing exclusively the method get_namespace of the OntoUML class."""
import pytest
from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouexception import OUUnavailableTerm
from ontoumlpy.tests.test_ontouml.fixtures_test_ontouml import INVALID_INPUTS, ALL_TERMS_FRAGMENT, ALL_TERMS_STR


@pytest.mark.parametrize(
    "in_arg",
    ALL_TERMS_FRAGMENT,
)
def test1(in_arg) -> None:
    assert OntoUML.get_term(in_arg) is not None
    assert str(OntoUML.get_term(in_arg)) in ALL_TERMS_STR
    assert OntoUML.get_term(in_arg) in OntoUML.get_list_all()
    assert isinstance(OntoUML.get_term(in_arg), URIRef)
    assert OntoUML.get_term(in_arg).fragment in ALL_TERMS_FRAGMENT


@pytest.mark.parametrize(
    "in_arg",
    INVALID_INPUTS,
)
def test10(in_arg) -> None:
    """Verifies that OntoUML.get_term() raises a TypeError when provided with an argument."""
    with pytest.raises(OUUnavailableTerm):
        OntoUML.get_term(in_arg)


def test11() -> None:
    """Verifies that OntoUML.get_term() raises a TypeError when provided with an argument."""
    with pytest.raises(TypeError):
        OntoUML.get_term()

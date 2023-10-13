"""Module for testing exclusively the method get_namespace of the OntoUML class."""
import pytest
from rdflib import URIRef

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouexception import OUUnavailableTerm
from ontoumlpy.tests.test_ontouml.fixtures_test_ontouml import INVALID_INPUTS


@pytest.mark.parametrize(
    "in_arg",
    INVALID_INPUTS,
)
def test1(in_arg) -> None:
    """Verifies that OntoUML.get_term() raises a TypeError when provided with an argument."""
    with pytest.raises(OUUnavailableTerm):
        OntoUML.get_term(in_arg)

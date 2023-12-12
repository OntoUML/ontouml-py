import pytest
from datetime import datetime

from ontouml_py.model.ontoumlelement import OntoumlElement


def test_ontoumlelement_creation_with_default_values():
    """Test the creation of an OntoumlElement with default values."""
    element = OntoumlElement()
    assert isinstance(element.id, str) and len(element.id) > 0, "Default 'id' should be a non-empty string"
    assert isinstance(element.created, datetime), "'created' should be a datetime instance"
    assert element.modified is None, "'modified' should be None by default"

def test_ontoumlelement_creation_with_custom_id():
    """Test the creation of an OntoumlElement with a custom 'id'."""
    custom_id = "custom_id_123"
    element = OntoumlElement(id=custom_id)
    assert element.id == custom_id, "Custom 'id' should be set correctly"

def test_ontoumlelement_equality_same_id():
    """Test the equality of two OntoumlElement instances with the same 'id'."""
    id_value = "test_id"
    element1 = OntoumlElement(id=id_value)
    element2 = OntoumlElement(id=id_value)
    assert element1 == element2, "Elements with the same 'id' should be equal"

def test_ontoumlelement_equality_different_id():
    """Test the inequality of two OntoumlElement instances with different 'id's."""
    element1 = OntoumlElement(id="id1")
    element2 = OntoumlElement(id="id2")
    assert element1 != element2, "Elements with different 'id's should not be equal"

def test_ontoumlelement_modified_date():
    """Test setting the 'modified' date of an OntoumlElement."""
    modified_date = datetime.now()
    element = OntoumlElement(modified=modified_date)
    assert element.modified == modified_date, "'modified' date should be set correctly"

@pytest.mark.parametrize("invalid_id", [None, ""])
def test_ontoumlelement_creation_with_invalid_id(invalid_id):
    """Test the creation of an OntoumlElement with an invalid 'id'.

    :param invalid_id: An invalid 'id' value to test.
    """
    with pytest.raises(ValueError, match="The 'id' field must not be empty."):
        OntoumlElement(id=invalid_id)

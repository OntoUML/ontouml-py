import pytest
from langstring import LangString

from ontouml_py.model.namedelement import NamedElement


def test_namedelement_creation_with_default_values():
    """Test the creation of a NamedElement with default values."""
    element = NamedElement()
    assert isinstance(element.names, set), "'names' should be a set"
    assert isinstance(element.alt_names, set), "'alt_names' should be a set"
    assert element.description is None, "'description' should be None by default"
    assert isinstance(element.editorial_notes, set), "'editorial_notes' should be a set"
    assert isinstance(element.creators, set), "'creators' should be a set"
    assert isinstance(element.contributors, set), "'contributors' should be a set"

def test_namedelement_field_assignments():
    """Test the assignment of various fields in NamedElement."""
    names = {LangString("Name1"), LangString("Name2")}
    alt_names = {LangString("AltName1")}
    description = LangString("Description")
    editorial_notes = {LangString("Note1")}
    creators = {"creator1", "creator2"}
    contributors = {"contributor1"}

    element = NamedElement(names=names, alt_names=alt_names, description=description,
                           editorial_notes=editorial_notes, creators=creators, contributors=contributors)

    assert element.names == names, "'names' should be assigned correctly"
    assert element.alt_names == alt_names, "'alt_names' should be assigned correctly"
    assert element.description == description, "'description' should be assigned correctly"
    assert element.editorial_notes == editorial_notes, "'editorial_notes' should be assigned correctly"
    assert element.creators == creators, "'creators' should be assigned correctly"
    assert element.contributors == contributors, "'contributors' should be assigned correctly"


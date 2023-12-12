import pytest

from ontouml_py.model.modelelement import ModelElement


def test_modelelement_creation_with_default_values():
    """Test the creation of a ModelElement with default values."""
    element = ModelElement()
    assert isinstance(element.custom_properties, set), "'custom_properties' should be a set"

def test_modelelement_custom_properties_assignment():
    """Test the assignment of custom properties in ModelElement."""
    custom_properties = {("key1", "value1"), ("key2", 2)}
    element = ModelElement(custom_properties=custom_properties)
    assert element.custom_properties == custom_properties, "'custom_properties' should be assigned correctly"

def test_modelelement_inherited_properties():
    """Test that ModelElement correctly inherits properties from ProjectElement and NamedElement."""
    element = ModelElement()
    # Testing inherited properties from NamedElement and ProjectElement
    assert hasattr(element, "id"), "ModelElement should inherit 'id' from OntoumlElement"
    assert hasattr(element, "names"), "ModelElement should inherit 'names' from NamedElement"

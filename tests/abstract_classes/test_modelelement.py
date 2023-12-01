from typing import Any

import pytest

from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Anchor(ModelElement):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


@pytest.fixture
def sample_model_element() -> Anchor:
    """Fixture to create a sample Anchor instance for testing.

    :return: An instance of Anchor for testing purposes.
    """
    return Anchor()


def test_model_element_initialization() -> None:
    """Test the initialization of a ModelElement instance."""
    element = Anchor(custom_properties={("key1", "value1"), ("key2", "value2")})
    assert element.custom_properties == {
        ("key1", "value1"),
        ("key2", "value2"),
    }, "ModelElement should initialize with the provided custom properties."


def test_model_element_custom_properties_assignment(sample_model_element: Anchor) -> None:
    """Test assigning custom properties to a ModelElement instance.

    :param sample_model_element: A sample Anchor instance.
    """
    sample_model_element.custom_properties = {("key3", "value3")}
    assert sample_model_element.custom_properties == {
        ("key3", "value3")
    }, "ModelElement should correctly assign new custom properties."


def test_model_element_custom_properties_update(sample_model_element: Anchor) -> None:
    """Test updating custom properties of a ModelElement instance.

    :param sample_model_element: A sample Anchor instance.
    """
    sample_model_element.custom_properties.add(("key4", "value4"))
    assert (
        "key4",
        "value4",
    ) in sample_model_element.custom_properties, "ModelElement should allow updating custom properties."


def test_model_element_invalid_custom_properties_type() -> None:
    """Test assigning invalid type to custom properties of a ModelElement instance."""
    with pytest.raises(ValueError):
        Anchor(custom_properties="invalid_type")
        pytest.fail("ModelElement should not accept non-set types for custom properties.")

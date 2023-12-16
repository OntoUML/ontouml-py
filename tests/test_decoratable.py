import pytest
from pytest_lazyfixture import lazy_fixture

from ontouml_py.model.decoratable import Decoratable
from ontouml_py.model.property import Property


@pytest.mark.parametrize(
    "classifier_fixture",
    [lazy_fixture("valid_class"), lazy_fixture("valid_binary_relation"), lazy_fixture("valid_nary_relation")],
)
def test_classifier_initialization_from_decoratable(classifier_fixture):
    """Test the initialization of Classifier subclasses from Decoratable.

    :param classifier_fixture: A fixture for a concrete classifier instance.
    """
    assert isinstance(classifier_fixture, Decoratable)
    assert hasattr(classifier_fixture, "is_derived")


@pytest.mark.parametrize("is_derived", [True, False])
def test_property_initialization_from_decoratable(valid_class, is_derived):
    """Test the initialization of Property from Decoratable with different is_derived values.

    :param valid_class: A fixture for a valid Class instance.
    :param is_derived: A boolean value to test the is_derived attribute.
    """
    property = Property(classifier=valid_class, is_derived=is_derived)
    assert isinstance(property, Decoratable)
    assert property.is_derived == is_derived


@pytest.mark.parametrize("is_derived", [True, False])
@pytest.mark.parametrize(
    "classifier_fixture",
    [lazy_fixture("valid_class"), lazy_fixture("valid_binary_relation"), lazy_fixture("valid_nary_relation")],
)
def test_is_derived_attribute_in_classifier(classifier_fixture, is_derived):
    """Test the is_derived attribute in Classifier subclasses.

    :param classifier_fixture: A fixture for a concrete classifier instance.
    :param is_derived: A boolean value to test the is_derived attribute.
    """
    classifier_fixture.is_derived = is_derived
    assert classifier_fixture.is_derived == is_derived


@pytest.mark.parametrize("is_derived", [True, False])
def test_is_derived_attribute_in_property(valid_class, is_derived):
    """Test the is_derived attribute in Property.

    :param valid_class: A fixture for a valid Class instance.
    :param is_derived: A boolean value to test the is_derived attribute.
    """
    property = valid_class.create_property(is_derived=is_derived)
    assert property.is_derived == is_derived

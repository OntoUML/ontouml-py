import pytest
from ontouml_py.classes.abstract_classes.decoratable import Decoratable


class Classifier(Decoratable):
    """A concrete implementation of the abstract Decoratable class for testing purposes."""

    def __init__(self, **data):
        super().__init__(**data)


class Property(Decoratable):
    """A concrete implementation of the abstract Decoratable class for testing purposes."""

    def __init__(self, **data):
        super().__init__(**data)


@pytest.fixture
def default_decoratable():
    """Fixture to create a default instance of Property."""
    return Property()


def test_decoratable_initialization(default_decoratable: Property):
    """
    Test the initialization of a Decoratable instance.

    :param default_decoratable: Fixture providing a default instance of Property.
    :return: None
    """
    assert not default_decoratable.is_derived, "Decoratable should initialize 'is_derived' as False by default."


def test_decoratable_is_derived_attribute(default_decoratable: Property):
    """
    Test setting the 'is_derived' attribute of a Decoratable instance.

    :param default_decoratable: Fixture providing a default instance of Property.
    :return: None
    """
    default_decoratable.is_derived = True
    assert (
        default_decoratable.is_derived
    ), "Setting 'is_derived' to True should be reflected in the Decoratable instance."


def test_decoratable_invalid_subclass_initialization():
    """
    Test the initialization of a Decoratable instance with an invalid subclass.

    :raises TypeError: If an invalid subclass is used to initialize a Decoratable instance.
    """
    with pytest.raises(TypeError):
        Decoratable()  # Abstract class should not be instantiated directly


def test_decoratable_valid_subclass_initialization():
    """
    Test the initialization of a Decoratable instance with valid subclasses.

    :return: None
    """
    classifier_instance = Classifier()
    property_instance = Property()
    assert isinstance(classifier_instance, Decoratable), "Classifier should be a valid subclass of Decoratable."
    assert isinstance(property_instance, Decoratable), "Property should be a valid subclass of Decoratable."

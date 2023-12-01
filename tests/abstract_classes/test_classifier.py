import pytest

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.concrete_classes.property import Property


class Class(Classifier):
    """A concrete implementation of the abstract Classifier class for testing purposes."""

    def __init__(self, **data):
        super().__init__(**data)


class Relation(Classifier):
    """A concrete implementation of the abstract Classifier class for testing purposes."""

    def __init__(self, **data):
        super().__init__(**data)


def test_classifier_initialization() -> None:
    """Test the initialization of a Classifier instance.

    Ensures that a Classifier instance can be initialized and its properties are set correctly.
    """
    classifier = Class(is_abstract=True)
    assert classifier.is_abstract, "Classifier should be initialized as abstract."


def test_add_property_valid() -> None:
    """Test adding a valid property to a Classifier.

    Ensures that a Property instance can be added to a Classifier's properties set.
    """
    classifier = Class()
    prop = Property()
    classifier.add_property(prop)
    assert prop in classifier.properties, "Property should be added to the classifier's properties."


def test_add_property_invalid_type() -> None:
    """Test adding an invalid type as a property to a Classifier.

    Ensures that a TypeError is raised when a non-Property instance is added.
    """
    classifier = Class()
    with pytest.raises(TypeError, match="Property to be added must be an instance of Property."):
        classifier.add_property("not_a_property")


def test_remove_property_valid() -> None:
    """Test removing a valid property from a Classifier.

    Ensures that a Property instance can be removed from a Classifier's properties set.
    """
    classifier = Class()
    prop = Property()
    classifier.add_property(prop)
    classifier.remove_property(prop)
    assert classifier.properties == [], "Property should be removed from the classifier's properties."


def test_remove_property_invalid_type() -> None:
    """Test removing an invalid type from a Classifier's properties.

    Ensures that a TypeError is raised when attempting to remove a non-Property instance.
    """
    classifier = Class()
    with pytest.raises(TypeError, match="Property 'not_a_property' cannot be removed as it is not a valid Property."):
        classifier.remove_property("not_a_property")


def test_remove_property_not_in_list() -> None:
    """Test removing a property that is not in the Classifier's properties list.

    Ensures that a ValueError is raised when attempting to remove a Property that is not part of the classifier.
    """
    classifier = Class()
    prop = Property()
    with pytest.raises(ValueError, match="cannot be removed because"):
        classifier.remove_property(prop)


def test_classifier_abstractness_change() -> None:
    """Test changing the abstractness of a Classifier.

    Ensures that the is_abstract attribute of a Classifier can be changed after initialization.
    """
    classifier = Class()
    classifier.is_abstract = True
    assert classifier.is_abstract, "Classifier's abstractness should be changeable."


def test_property_association_on_addition() -> None:
    """Test if a property's property_of is set correctly when added to a classifier."""
    classifier = Class()
    prop = Property()
    classifier.add_property(prop)
    assert prop.property_of == classifier, "Property's owner should be set to the classifier on addition."


def test_property_disassociation_on_removal() -> None:
    """Test if a property's property_of is set to None when removed from a classifier."""
    classifier = Class()
    prop = Property()
    classifier.add_property(prop)
    classifier.remove_property(prop)
    assert prop.property_of is None, "Property's owner should be None after removal from the classifier."


def test_classifier_with_empty_properties() -> None:
    """Test initializing a Classifier with no properties."""
    classifier = Class()
    assert classifier.properties == [], "Classifier should be initialized with an empty set of properties."

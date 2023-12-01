import pytest
from icecream import ic

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.concrete_classes.property import Property
from ontouml_py.classes.enumerations.aggregationkind import AggregationKind
from ontouml_py.classes.enumerations.propertystereotype import PropertyStereotype
from ontouml_py.classes.datatypes.cardinality import Cardinality


@pytest.fixture
def default_property() -> Property:
    """Fixture to create a default Property instance for testing."""
    init_cardinality = Cardinality(lower_bound=0, upper_bound=1)
    return Property(cardinality=init_cardinality)


@pytest.fixture
def classifier_instance() -> Classifier:
    """Fixture to create a Classifier instance for testing."""
    return Classifier()


def test_property_initialization(default_property: Property):
    """
    Test the initialization of a Property instance.

    :param default_property: A default Property instance created by the fixture.
    """
    ic()
    assert default_property.is_read_only is False, "Default is_read_only should be False"
    assert default_property.aggregation_kind == AggregationKind.NONE, "Default aggregation_kind should be NONE"
    assert default_property.stereotype is None, "Default stereotype should be None"
    assert default_property.cardinality == Cardinality(min=0, max=1), "Cardinality should match the initialized value"
    assert default_property.property_type is None, "Default property_type should be None"
    assert default_property.subsetted_by == set(), "Default subsetted_by should be an empty set"
    assert default_property.redefined_by == set(), "Default redefined_by should be an empty set"


def test_property_is_property_of_setter(default_property: Property, classifier_instance: Classifier):
    """
    Test the setter for the is_property_of attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    :param classifier_instance: A Classifier instance created by the fixture.
    """
    default_property.is_property_of = classifier_instance
    assert (
        default_property.is_property_of == classifier_instance
    ), "is_property_of should reference the Classifier instance"


def test_property_is_property_of_getter(default_property: Property, classifier_instance: Classifier):
    """
    Test the getter for the is_property_of attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    :param classifier_instance: A Classifier instance created by the fixture.
    """
    default_property.is_property_of = classifier_instance
    assert default_property.is_property_of == classifier_instance, "Getter should return the set Classifier instance"


def test_property_read_only_flag(default_property: Property):
    """
    Test the modification and retrieval of the is_read_only attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    """
    default_property.is_read_only = True
    assert default_property.is_read_only is True, "is_read_only should be set to True"


def test_property_aggregation_kind(default_property: Property):
    """
    Test the modification and retrieval of the aggregation_kind attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    """
    default_property.aggregation_kind = AggregationKind.COMPOSITE
    assert default_property.aggregation_kind == AggregationKind.COMPOSITE, "aggregation_kind should be set to COMPOSITE"


def test_property_stereotype(default_property: Property):
    """
    Test the modification and retrieval of the stereotype attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    """
    default_property.stereotype = PropertyStereotype.BEGIN
    assert default_property.stereotype == PropertyStereotype.BEGIN, "stereotype should be set to BEGIN"


def test_property_cardinality(default_property: Property):
    """
    Test the modification and retrieval of the cardinality attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    """
    new_cardinality = Cardinality(min=1, max=1)
    default_property.cardinality = new_cardinality
    assert default_property.cardinality == new_cardinality, "cardinality should be updated to the new value"


def test_property_type(default_property: Property, classifier_instance: Classifier):
    """
    Test the modification and retrieval of the property_type attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    :param classifier_instance: A Classifier instance created by the fixture.
    """
    default_property.property_type = classifier_instance
    assert (
        default_property.property_type == classifier_instance
    ), "property_type should reference the Classifier instance"


def test_property_subsetted_by(default_property: Property):
    """
    Test the modification and retrieval of the subsetted_by attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    """
    subset_property = Property(cardinality=Cardinality(min=0, max=1))
    default_property.subsetted_by.add(subset_property)
    assert subset_property in default_property.subsetted_by, "subsetted_by should include the added Property instance"


def test_property_redefined_by(default_property: Property):
    """
    Test the modification and retrieval of the redefined_by attribute of the Property class.

    :param default_property: A default Property instance created by the fixture.
    """
    redefined_property = Property(cardinality=Cardinality(min=0, max=1))
    default_property.redefined_by.add(redefined_property)
    assert (
        redefined_property in default_property.redefined_by
    ), "redefined_by should include the added Property instance"

import pytest
from pydantic import ValidationError
from pytest_lazyfixture import lazy_fixture

from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.cardinality import Cardinality
from ontouml_py.model.class_ontouml import Class
from ontouml_py.model.enumerations.aggregationkind import AggregationKind
from ontouml_py.model.enumerations.propertystereotype import PropertyStereotype
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.property import Property


@pytest.mark.parametrize(
    "classifier_fixture",
    [lazy_fixture("valid_class"), lazy_fixture("valid_binary_relation"), lazy_fixture("valid_nary_relation")],
)
def test_create_property(classifier_fixture):
    """Test the creation of a property in a classifier.

    :param classifier_fixture: A fixture for a concrete classifier instance.
    """
    new_property = classifier_fixture.create_property()
    assert new_property in classifier_fixture.properties


@pytest.mark.parametrize(
    "classifier_fixture",
    [lazy_fixture("valid_class"), lazy_fixture("valid_binary_relation"), lazy_fixture("valid_nary_relation")],
)
def test_properties_getter(classifier_fixture):
    """Test the properties getter method of the classifier.

    :param classifier_fixture: A fixture for a concrete classifier instance.
    """
    assert isinstance(classifier_fixture.properties, list)
    for prop in classifier_fixture.properties:
        assert isinstance(prop, Property)


@pytest.mark.parametrize(
    "property_data",
    [
        {"is_read_only": True, "aggregation_kind": AggregationKind.SHARED},
        {"stereotype": PropertyStereotype.BEGIN, "cardinality": Cardinality(lower_bound=0, upper_bound=1)},
        {"property_type": "some_type", "subsetted_by": set(), "redefined_by": set()},
    ],
)
@pytest.mark.parametrize(
    "classifier_fixture",
    [lazy_fixture("valid_class"), lazy_fixture("valid_binary_relation"), lazy_fixture("valid_nary_relation")],
)
def test_create_property_with_parameters(classifier_fixture, property_data):
    """Test the creation of a property with various parameters in a classifier.

    :param classifier_fixture: A fixture for a concrete classifier instance.
    :param property_data: A dictionary of property attributes to be tested.
    """
    new_property = classifier_fixture.create_property(**property_data)
    for key, value in property_data.items():
        assert getattr(new_property, key) == value
    assert new_property in classifier_fixture.properties


@pytest.mark.parametrize("invalid_cardinality", [None, 5, "invalid", []])
@pytest.mark.parametrize(
    "classifier_fixture",
    [lazy_fixture("valid_class"), lazy_fixture("valid_binary_relation"), lazy_fixture("valid_nary_relation")],
)
def test_property_invalid_cardinality_initialization(classifier_fixture, invalid_cardinality):
    """Test Property initialization with invalid cardinality types.

    :param classifier_fixture: A fixture for a concrete classifier instance.
    :param invalid_cardinality: An invalid cardinality value.
    :raises TypeError: If the cardinality is not an instance of Cardinality.
    """
    with pytest.raises(ValidationError, match="Input should be a valid"):
        classifier_fixture.create_property(cardinality=invalid_cardinality)


@pytest.mark.parametrize(
    "classifier_type, fixture_name",
    [(Class, "valid_class"), (BinaryRelation, "valid_binary_relation"), (NaryRelation, "valid_nary_relation")],
)
def test_classifier_type_property_creation(classifier_type, fixture_name, request):
    """Test that different classifier types can create properties consistently.

    :param classifier_type: The type of the classifier to test.
    :param fixture_name: The name of the fixture to use for the test.
    :param request: Pytest fixture to dynamically request a fixture.
    """
    classifier_fixture = request.getfixturevalue(fixture_name)
    assert isinstance(classifier_fixture, classifier_type)

    new_property = classifier_fixture.create_property()
    assert isinstance(new_property, Property)
    assert new_property in classifier_fixture.properties

import pytest
from pydantic import ValidationError
from pytest_lazyfixture import lazy_fixture

from ontouml_py.model.cardinality import Cardinality
from ontouml_py.model.enumerations.aggregationkind import AggregationKind
from ontouml_py.model.enumerations.propertystereotype import PropertyStereotype
from ontouml_py.model.property import Property


@pytest.mark.parametrize(
    "is_read_only, aggregation_kind, stereotype, cardinality, property_type, subsetted_by, redefined_by",
    [
        (True, AggregationKind.NONE, None, Cardinality(), None, set(), set()),
        (
            False,
            AggregationKind.SHARED,
            PropertyStereotype.BEGIN,
            Cardinality(lower_bound=0, upper_bound=1),
            lazy_fixture("valid_class"),
            set(),
            set(),
        ),
        (
            True,
            AggregationKind.COMPOSITE,
            PropertyStereotype.END,
            Cardinality(lower_bound=1, upper_bound=1),
            lazy_fixture("valid_class"),
            set(),
            set(),
        ),
    ],
)
def test_property_initialization(
    valid_class,
    is_read_only,
    aggregation_kind,
    stereotype,
    cardinality,
    property_type,
    subsetted_by,
    redefined_by,
):
    """Test the initialization of Property with various combinations of parameters.

    :param valid_class: A valid Class instance to be used as the classifier for the Property.
    :param is_read_only: A boolean indicating if the property is read-only.
    :param aggregation_kind: An AggregationKind enumeration value.
    :param stereotype: A PropertyStereotype enumeration value or None.
    :param cardinality: A Cardinality instance.
    :param property_type: A Class instance or None.
    :param subsetted_by: A set of Property instances or an empty set.
    :param redefined_by: A set of Property instances or an empty set.
    :return: None
    """
    property = Property(
        classifier=valid_class,
        is_read_only=is_read_only,
        aggregation_kind=aggregation_kind,
        stereotype=stereotype,
        cardinality=cardinality,
        property_type=property_type,
        subsetted_by=subsetted_by,
        redefined_by=redefined_by,
    )
    assert property.is_read_only == is_read_only
    assert property.aggregation_kind == aggregation_kind
    assert property.stereotype == stereotype
    assert property.cardinality == cardinality
    assert property.property_type == property_type
    assert property.subsetted_by == subsetted_by
    assert property.redefined_by == redefined_by


@pytest.mark.parametrize("invalid_cardinality", [None, 5, "invalid", []])
def test_property_invalid_cardinality_type(valid_class, invalid_cardinality):
    """Test Property initialization with invalid cardinality types.

    :param valid_class: A valid Class instance to be used as the classifier for the Property.
    :param invalid_cardinality: An invalid cardinality value.
    :raises TypeError: If the cardinality is not an instance of Cardinality.
    """
    with pytest.raises(ValidationError, match="Input should be a valid dictionary or instance of Cardinality"):
        Property(classifier=valid_class, cardinality=invalid_cardinality)


def test_property_classifier_getter(valid_property):
    """Test the classifier getter method of the Property class.

    :param valid_property: A valid Property instance.
    :return: None
    """
    assert valid_property.classifier == valid_property._classifier


@pytest.mark.parametrize(
    "attribute, value",
    [
        ("is_read_only", True),
        ("is_read_only", False),
        ("aggregation_kind", AggregationKind.SHARED),
        ("stereotype", PropertyStereotype.BEGIN),
        ("cardinality", Cardinality(lower_bound=1, upper_bound=1)),
        ("property_type", lazy_fixture("valid_class")),
    ],
)
def test_property_attribute_assignment(valid_property, attribute, value):
    """Test assignment of different attributes of the Property class.

    :param valid_property: A valid Property instance.
    :param attribute: Name of the attribute to be tested.
    :param value: The value to be assigned to the attribute.
    :return: None
    """
    setattr(valid_property, attribute, value)
    assert getattr(valid_property, attribute) == value


def test_property_invalid_aggregation_kind_assignment(valid_property):
    """Test assignment of invalid aggregation kind to a Property instance.

    :param valid_property: A valid Property instance.
    :raises ValidationError: If an invalid AggregationKind is assigned.
    """
    with pytest.raises(ValidationError, match="Input should be 'none', 'composite' or 'shared'"):
        valid_property.aggregation_kind = "invalid_kind"

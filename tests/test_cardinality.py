import pytest
from pydantic import ValidationError

from ontouml_py.model.cardinality import Cardinality


# Assuming the necessary imports are already in place


def test_cardinality_initialization():
    """Test successful initialization of a Cardinality instance."""
    cardinality = Cardinality()
    assert cardinality.lower_bound == 1, "Cardinality should initialize lower_bound as 1"
    assert cardinality.upper_bound == 1, "Cardinality should initialize upper_bound as 1"
    assert cardinality.is_ordered is False, "Cardinality should initialize is_ordered as False"
    assert cardinality.is_unique is True, "Cardinality should initialize is_unique as True"


@pytest.mark.parametrize("lower_bound, upper_bound", [(0, 1), ("0", "1"), (None, None)])
def test_cardinality_bounds_initialization(lower_bound, upper_bound):
    """Test Cardinality initialization with various bounds.

    :param lower_bound: Lower bound for the cardinality.
    :param upper_bound: Upper bound for the cardinality.
    """
    cardinality = Cardinality(lower_bound=lower_bound, upper_bound=upper_bound)
    assert cardinality.lower_bound == lower_bound, "Cardinality should be initialized with the correct lower_bound"
    assert cardinality.upper_bound == upper_bound, "Cardinality should be initialized with the correct upper_bound"


@pytest.mark.parametrize("valid_value", ["valid", -1])
def test_cardinality_unusual_bounds_types(valid_value):
    """Test Cardinality initialization with unusual types for bounds.

    :param valid_value: A unusual, but valid value for the bounds.
    :raises ValidationError: If bounds are set with invalid types.
    """
    assert Cardinality(lower_bound=valid_value)
    assert Cardinality(upper_bound=valid_value)


@pytest.mark.parametrize("invalid_value", [[1], 1.5])
def test_cardinality_invalid_bounds_types(invalid_value):
    """Test Cardinality initialization with invalid types for bounds.

    :param invalid_value: An invalid value for the bounds.
    :raises ValidationError: If bounds are set with invalid types.
    """
    with pytest.raises(ValidationError):
        Cardinality(lower_bound=invalid_value)
    with pytest.raises(ValidationError):
        Cardinality(upper_bound=invalid_value)


@pytest.mark.parametrize("invalid_value", [3, "mystring", 1.5])
def test_cardinality_invalid_attribute_init(invalid_value):
    """Test Cardinality initialization with invalid types for bounds.

    :param invalid_value: An invalid value for the bounds.
    :raises ValidationError: If bounds are set with invalid types.
    """
    with pytest.raises(ValidationError):
        Cardinality(is_ordered=invalid_value)
    with pytest.raises(ValidationError):
        Cardinality(is_unique=invalid_value)


@pytest.mark.parametrize("invalid_value", [3, "mystring", 1.5])
def test_cardinality_invalid_attribute_post_init(invalid_value):
    """Test Cardinality initialization with invalid types for bounds.

    :param invalid_value: An invalid value for the bounds.
    :raises ValidationError: If bounds are set with invalid types.
    """
    c = Cardinality()
    with pytest.raises(ValidationError):
        c.is_ordered = invalid_value
    with pytest.raises(ValidationError):
        c.is_unique = invalid_value


def test_cardinality_attribute_assignment():
    """Test attribute assignment for a Cardinality instance."""
    cardinality = Cardinality()
    cardinality.lower_bound = 1
    cardinality.upper_bound = "5"
    cardinality.is_ordered = True
    cardinality.is_unique = False
    assert cardinality.lower_bound == 1, "Cardinality attribute 'lower_bound' should be assignable"
    assert cardinality.upper_bound == "5", "Cardinality attribute 'upper_bound' should be assignable"
    assert cardinality.is_ordered, "Cardinality attribute 'is_ordered' should be assignable"
    assert not cardinality.is_unique, "Cardinality attribute 'is_unique' should be assignable"

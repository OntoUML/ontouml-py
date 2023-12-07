import pytest

from ontouml_py.classes.datatypes.cardinality import Cardinality


def test_cardinality_lower_equals_upper() -> None:
    """Test Cardinality with lower_bound equal to upper_bound."""
    cardinality = Cardinality(lower_bound="1", upper_bound="1")
    assert cardinality.lower_bound == cardinality.upper_bound


def test_cardinality_both_star() -> None:
    """Test Cardinality with both lower_bound and upper_bound set to '*'."""
    cardinality = Cardinality(lower_bound="*", upper_bound="*")
    assert cardinality.lower_bound == "*"
    assert cardinality.upper_bound == "*"


def test_cardinality_lower_star_upper_value_error() -> None:
    """Test Cardinality with lower_bound as '*' and upper_bound as a value, expecting an error.

    :raises: ValueError: If the lower_bound is '*' and upper_bound is a value.
    """
    with pytest.raises(ValueError, match="The cardinality's lower bound .* is higher than its upper bound"):
        Cardinality(lower_bound="*", upper_bound="1")


def test_cardinality_lower_value_upper_star() -> None:
    """Test Cardinality with lower_bound as a value and upper_bound as '*'."""
    cardinality = Cardinality(lower_bound="1", upper_bound="*")
    assert cardinality.lower_bound == "1"
    assert cardinality.upper_bound == "*"


def test_cardinality_lower_higher_than_upper_error() -> None:
    """Test Cardinality with lower_bound higher than upper_bound, expecting an error.

    :raises: ValueError: If the lower_bound is higher than upper_bound.
    """
    with pytest.raises(ValueError, match="The cardinality's lower bound .* is higher than its upper bound"):
        Cardinality(lower_bound="2", upper_bound="1")


def test_cardinality_lower_lower_than_upper() -> None:
    """Test Cardinality with lower_bound lower than upper_bound."""
    cardinality = Cardinality(lower_bound="1", upper_bound="2")
    assert cardinality.lower_bound == "1"
    assert cardinality.upper_bound == "2"

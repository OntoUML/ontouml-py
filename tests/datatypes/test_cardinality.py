from pydantic import ValidationError


def test_cardinality_with_valid_integer_bounds() -> None:
    """Test Cardinality with valid integer values for lower_bound and upper_bound."""
    cardinality = Cardinality(lower_bound="1", upper_bound="10")
    assert (
        cardinality.lower_bound == "1" and cardinality.upper_bound == "10"
    ), "Cardinality should accept valid integer bounds."


def test_cardinality_with_invalid_string_bounds() -> None:
    """Test Cardinality with invalid string values for lower_bound and upper_bound, expecting an error.

    :raises: ValueError: If non-integer, non-'*' string values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="a", upper_bound="b")


def test_cardinality_with_none_bounds() -> None:
    """Test Cardinality with None for both lower_bound and upper_bound."""
    cardinality = Cardinality(lower_bound=None, upper_bound=None)
    assert (
        cardinality.lower_bound is None and cardinality.upper_bound is None
    ), "Cardinality should allow None as bounds."


def test_cardinality_with_mixed_valid_invalid_bounds() -> None:
    """Test Cardinality with a mix of valid and invalid bounds, expecting an error.

    :raises: ValueError: If one bound is valid and the other is invalid.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="1", upper_bound="a")


def test_cardinality_with_star_and_integer_bounds() -> None:
    """Test Cardinality with '*' for lower_bound and an integer for upper_bound.

    :raises: ValueError: If lower bound is higher than upper bound.
    """
    with pytest.raises(ValueError):
        cardinality = Cardinality(lower_bound="*", upper_bound="10")


def test_cardinality_with_integer_and_star_bounds() -> None:
    """Test Cardinality with an integer for lower_bound and '*' for upper_bound."""
    cardinality = Cardinality(lower_bound="1", upper_bound="*")
    assert (
        cardinality.lower_bound == "1" and cardinality.upper_bound == "*"
    ), "Cardinality should allow an integer for lower_bound and '*' for upper_bound."


def test_cardinality_with_negative_integer_bounds_error() -> None:
    """Test Cardinality with negative integer values for bounds, expecting an error.

    :raises: ValueError: If negative integer values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="-1", upper_bound="-5")


def test_cardinality_with_empty_string_bounds_error() -> None:
    """Test Cardinality with empty string values for bounds, expecting an error.

    :raises: ValueError: If empty string values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="", upper_bound="")


def test_cardinality_with_whitespace_string_bounds_error() -> None:
    """Test Cardinality with whitespace string values for bounds, expecting an error.

    :raises: ValueError: If whitespace string values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound=" ", upper_bound=" ")


def test_cardinality_with_integer_bounds_converted_to_string() -> None:
    """"Test Cardinality with integer values for lower_bound and upper_bound, expecting conversion to strings.

    :raises: ValueError: If the conversion from integer to string does not occur.
    """
    cardinality = Cardinality(lower_bound=1, upper_bound=10)
    assert (
        cardinality.lower_bound == "1" and cardinality.upper_bound == "10"
    ), "Integer bounds should be converted to strings."


def test_cardinality_with_mixed_none_and_valid_bound() -> None:
    """"Test Cardinality with None for lower_bound and a valid integer for upper_bound.

    :raises: ValueError: If the class does not handle None and valid bounds correctly.
    """
    cardinality = Cardinality(lower_bound=None, upper_bound="10")
    assert (
        cardinality.lower_bound == "10" and cardinality.upper_bound == "10"
    ), "Cardinality should handle None for lower_bound and a valid integer for upper_bound."


def test_cardinality_with_mixed_none_and_invalid_bound() -> None:
    """"Test Cardinality with None for lower_bound and an invalid value for upper_bound, expecting an error.

    :raises: ValueError: If the class does not handle None and invalid bounds correctly.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound=None, upper_bound="a")


def test_cardinality_with_non_numeric_string_bounds() -> None:
    """"Test Cardinality with non-numeric, non-'*' string values for bounds, expecting an error.

    :raises: ValueError: If non-numeric, non-'*' string values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="abc", upper_bound="xyz")


import pytest
from ontouml_py.classes.datatypes.cardinality import Cardinality


def test_cardinality_with_invalid_type_for_lower_bound() -> None:
    """"Test Cardinality with an invalid type (e.g., list) for lower_bound, expecting a TypeError.

    :raises: TypeError: If an invalid type is used for lower_bound.
    """
    with pytest.raises(ValidationError):
        Cardinality(lower_bound=[1, 2, 3], upper_bound="10")


def test_cardinality_with_invalid_type_for_upper_bound() -> None:
    """"Test Cardinality with an invalid type (e.g., dict) for upper_bound, expecting a TypeError.

    :raises: TypeError: If an invalid type is used for upper_bound.
    """
    with pytest.raises(ValidationError):
        Cardinality(lower_bound="1", upper_bound={"max": 10})


def test_cardinality_with_invalid_types_for_both_bounds() -> None:
    """"Test Cardinality with invalid types (e.g., tuple and float) for both lower_bound and upper_bound, expecting a TypeError.

    :raises: TypeError: If invalid types are used for both bounds.
    """
    with pytest.raises(ValidationError):
        Cardinality(lower_bound=(1, 2), upper_bound=3.14)

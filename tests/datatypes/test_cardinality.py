import pytest

from ontouml_py.classes.datatypes.cardinality import Cardinality


def test_cardinality_with_valid_integer_bounds() -> None:
    """ "Test Cardinality with valid integer values for lower_bound and upper_bound."""
    cardinality = Cardinality(lower_bound="1", upper_bound="10")
    assert (
        cardinality.lower_bound == "1" and cardinality.upper_bound == "10"
    ), "Cardinality should accept valid integer bounds."


def test_cardinality_with_invalid_string_bounds() -> None:
    """ "Test Cardinality with invalid string values for lower_bound and upper_bound, expecting an error.

    :raises: ValueError: If non-integer, non-'*' string values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="a", upper_bound="b")


def test_cardinality_with_none_bounds() -> None:
    """ "Test Cardinality with None for both lower_bound and upper_bound."""
    cardinality = Cardinality(lower_bound=None, upper_bound=None)
    assert (
        cardinality.lower_bound is None and cardinality.upper_bound is None
    ), "Cardinality should allow None as bounds."


def test_cardinality_with_mixed_valid_invalid_bounds() -> None:
    """ "Test Cardinality with a mix of valid and invalid bounds, expecting an error.

    :raises: ValueError: If one bound is valid and the other is invalid.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="1", upper_bound="a")


def test_cardinality_with_star_and_integer_bounds() -> None:
    """ "Test Cardinality with '*' for lower_bound and an integer for upper_bound.

    :raises: ValueError: If lower bound is higher than upper bound.
    """
    with pytest.raises(ValueError):
        cardinality = Cardinality(lower_bound="*", upper_bound="10")


def test_cardinality_with_integer_and_star_bounds() -> None:
    """ "Test Cardinality with an integer for lower_bound and '*' for upper_bound."""
    cardinality = Cardinality(lower_bound="1", upper_bound="*")
    assert (
        cardinality.lower_bound == "1" and cardinality.upper_bound == "*"
    ), "Cardinality should allow an integer for lower_bound and '*' for upper_bound."


def test_cardinality_with_negative_integer_bounds_error() -> None:
    """ "Test Cardinality with negative integer values for bounds, expecting an error.

    :raises: ValueError: If negative integer values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="-1", upper_bound="-5")


def test_cardinality_with_empty_string_bounds_error() -> None:
    """ "Test Cardinality with empty string values for bounds, expecting an error.

    :raises: ValueError: If empty string values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound="", upper_bound="")


def test_cardinality_with_whitespace_string_bounds_error() -> None:
    """ "Test Cardinality with whitespace string values for bounds, expecting an error.

    :raises: ValueError: If whitespace string values are provided.
    """
    with pytest.raises(ValueError):
        Cardinality(lower_bound=" ", upper_bound=" ")

from typing import Any, List, Union, Optional

import pytest

from ontouml_py.utils.utils import validate_and_set


class TestClass:
    """Example class for testing validate_and_set function."""

    def __init__(self):
        self.name: Any = None
        self.age: Any = None


def test_validate_and_set_with_correct_type() -> None:
    """Test the validate_and_set function with the correct type to ensure it sets the value without raising an error.

    :raises AssertionError: If validate_and_set fails to set the value of the correct type.
    """
    instance = TestClass()
    validate_and_set(instance, "name", "John Doe", str)
    assert instance.name == "John Doe", "validate_and_set should successfully set the correct type."


def test_validate_and_set_with_incorrect_type() -> None:
    """Test the validate_and_set function with the incorrect type to ensure it raises a TypeError.

    :raises TypeError: If validate_and_set allows setting a value of incorrect type.
    """
    instance = TestClass()
    with pytest.raises(TypeError, match=r".* must be a str, not int."):
        validate_and_set(instance, "name", 123, str)


def test_validate_and_set_with_optional_none() -> None:
    """Test the validate_and_set function with an optional parameter set to None to ensure it allows None for optional attributes.

    :raises AssertionError: If validate_and_set fails to set an optional attribute to None.
    """
    instance = TestClass()
    validate_and_set(instance, "age", None, int, optional=True)
    assert instance.age is None, "validate_and_set should allow setting an optional attribute to None."


def test_validate_and_set_with_non_optional_none() -> None:
    """Test the validate_and_set function with a non-optional parameter set to None to ensure it raises a TypeError.

    :raises TypeError: If validate_and_set allows setting a non-optional attribute to None.
    """
    instance = TestClass()
    with pytest.raises(TypeError, match=r".* cannot be None."):
        validate_and_set(instance, "age", None, int, optional=False)


def test_validate_and_set_with_list_of_correct_types() -> None:
    """Test the validate_and_set function with a list of correct types to ensure it sets the value without raising an error.

    :raises AssertionError: If validate_and_set fails to set a list of values of the correct type.
    """
    instance = TestClass()
    validate_and_set(instance, "name", ["John Doe", "Jane Doe"], list)
    assert instance.name == [
        "John Doe",
        "Jane Doe",
    ], "validate_and_set should successfully set a list of correct types."


def test_validate_and_set_with_list_of_incorrect_types() -> None:
    """Test the validate_and_set function with a list containing incorrect types to ensure it raises a TypeError.

    :raises TypeError: If validate_and_set allows setting a list containing values of incorrect type.
    """
    instance = TestClass()
    with pytest.raises(TypeError, match=r"All elements in 'name' must be of type str."):
        validate_and_set(instance, "name", ["John Doe", 123], List[str])


def test_validate_and_set_with_empty_list() -> None:
    """Test the validate_and_set function with an empty list to ensure it does not raise an error when lists are allowed.

    :raises AssertionError: If validate_and_set fails to set an empty list when lists are allowed.
    """
    instance = TestClass()
    validate_and_set(instance, "name", [], List[str])
    assert instance.name == [], "validate_and_set should allow setting an empty list when lists are allowed."


def test_validate_and_set_with_list_of_mixed_correct_types() -> None:
    """Test the validate_and_set function with a list of mixed but correct types to ensure it sets the value without error.

    :raises AssertionError: If validate_and_set fails to set a list of mixed but correct types.
    """
    instance = TestClass()
    validate_and_set(instance, "name", ["John Doe", 42], List[Union[str, int]])
    assert instance.name == ["John Doe", 42], "validate_and_set should allow setting a list of mixed but correct types."


def test_validate_and_set_with_list_including_none() -> None:
    """Test the validate_and_set function with a list including None to ensure it sets the value without raising an error.

    :raises AssertionError: If validate_and_set fails to set a list including None when None is allowed.
    """
    instance = TestClass()
    validate_and_set(instance, "name", ["John Doe", None], List[Optional[str]])
    assert instance.name == ["John Doe", None], "validate_and_set should allow setting a list including None."


def test_validate_and_set_with_nested_list() -> None:
    """Test the validate_and_set function with nested lists to ensure it sets the value without raising an error.

    :raises AssertionError: If validate_and_set fails to set nested lists correctly.
    """
    instance = TestClass()
    validate_and_set(instance, "name", [["John Doe"], ["Jane Doe"]], List[List[str]])
    assert instance.name == [["John Doe"], ["Jane Doe"]], "validate_and_set should successfully set nested lists."


def test_validate_and_set_with_nonexistent_attribute() -> None:
    """Test the validate_and_set function to ensure it can create and set a new attribute that wasn't initially present.

    :raises AssertionError: If validate_and_set fails to create and set a new attribute.
    """
    instance = TestClass()
    validate_and_set(instance, "new_attr", "New Value", str)
    assert (
        hasattr(instance, "new_attr") and instance.new_attr == "New Value"
    ), "validate_and_set should create and set a new attribute that wasn't initially present."


def test_validate_and_set_reassign_attribute() -> None:
    """
    Test the validate_and_set function to ensure it correctly handles reassigning an existing attribute.

    :raises AssertionError: If validate_and_set fails to reassign an existing attribute with a new value of the correct type.
    """
    instance = TestClass()
    validate_and_set(instance, "name", "John Doe", str)
    validate_and_set(instance, "name", "Jane Smith", str)
    assert instance.name == "Jane Smith", "validate_and_set should correctly reassign an existing attribute."


def test_validate_and_set_with_complex_types() -> None:
    """
    Test the validate_and_set function with a complex type like a dictionary to ensure it sets the value correctly.

    :raises AssertionError: If validate_and_set fails to set a complex type like a dictionary.
    """
    instance = TestClass()
    validate_and_set(instance, "preferences", {"theme": "dark"}, dict)
    assert instance.preferences == {"theme": "dark"}, "validate_and_set should correctly set a dictionary attribute."


class CustomType:
    pass


def test_validate_and_set_with_custom_object() -> None:
    """
    Test the validate_and_set function with a custom object to ensure it sets the value correctly.

    :raises AssertionError: If validate_and_set fails to set a custom object type.
    """
    instance = TestClass()
    custom_obj = CustomType()
    validate_and_set(instance, "custom_attr", custom_obj, CustomType)
    assert isinstance(
        instance.custom_attr, CustomType
    ), "validate_and_set should correctly set a custom object attribute."

import pytest

from ontouml_py.utils import validate_subclasses


class BaseClass:
    pass


class SubClass(BaseClass):
    pass


class SubSubClass(SubClass):
    pass


class UnrelatedClass:
    pass


def test_validate_subclasses_with_valid_subclass():
    """ "Test validate_subclasses function with a valid subclass.

    :raises AssertionError: If the function does not recognize a valid subclass.
    """
    try:
        validate_subclasses(SubClass(), ["BaseClass", "SubClass"])
    except ValueError:
        pytest.fail("validate_subclasses raised ValueError unexpectedly for a valid subclass.")


def test_validate_subclasses_with_invalid_subclass():
    """ "Test validate_subclasses function with an invalid subclass.

    :raises AssertionError: If the function incorrectly accepts an invalid subclass.
    """
    with pytest.raises(ValueError) as excinfo:
        validate_subclasses(UnrelatedClass(), ["BaseClass", "SubClass"])
    assert "is not an allowed subclass" in str(
        excinfo.value
    ), "validate_subclasses did not raise ValueError for an invalid subclass."


def test_validate_subclasses_with_base_class():
    """ "Test validate_subclasses function with the base class itself.

    :raises AssertionError: If the function does not recognize the base class as a valid subclass.
    """
    try:
        validate_subclasses(BaseClass(), ["BaseClass", "SubClass"])
    except ValueError:
        pytest.fail("validate_subclasses raised ValueError unexpectedly for the base class.")


def test_validate_subclasses_with_empty_allowed_subclasses():
    """ "Test validate_subclasses function with an empty list of allowed subclasses.

    :raises AssertionError: If the function does not raise ValueError for an empty list of allowed subclasses.
    """
    with pytest.raises(ValueError) as excinfo:
        validate_subclasses(BaseClass(), [])
    assert "Only these subclasses are permitted" in str(
        excinfo.value
    ), "validate_subclasses did not raise ValueError for an empty list of allowed subclasses."


def test_validate_subclasses_with_indirect_subclass():
    """ "Test validate_subclasses function with an indirect subclass in a hierarchy A > B > C.

    :raises AssertionError: If the function does not recognize an indirect subclass.
    """
    try:
        validate_subclasses(SubSubClass(), ["BaseClass", "SubClass"])
    except ValueError:
        pytest.fail("validate_subclasses raised ValueError unexpectedly for an indirect subclass.")


def test_validate_subclasses_with_multiple_inheritance():
    """ "Test validate_subclasses function with a class inheriting from multiple parents.

    :raises AssertionError: If the function does not correctly handle multiple inheritance.
    """
    try:
        validate_subclasses(SubSubClass(), ["BaseClass"])
    except ValueError:
        pytest.fail("validate_subclasses raised ValueError unexpectedly with multiple inheritance.")

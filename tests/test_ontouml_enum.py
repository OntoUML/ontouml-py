"""
This module contains pytest tests for the OntoumlEnum class.

Tests cover the initialization of enum members and the functionality of the get_members class method.
"""

import pytest

from src.classes.enumerations.ontouml_enum import OntoumlEnum


def test_enum_member_initialization():
    """
    Test the initialization of an OntoumlEnum member.

    This test ensures that an OntoumlEnum member is correctly initialized with its name converted to CamelCase.
    """

    class TestEnum(OntoumlEnum):
        TEST_ENUM_MEMBER = ()

    member = TestEnum.TEST_ENUM_MEMBER
    assert member.value == "TestEnumMember", "Enum member's value should be 'TestEnumMember'"


def test_get_members():
    """
    Test the get_members class method of OntoumlEnum.

    This test checks if the get_members method correctly returns the keys of all enum members.
    """

    class TestEnum(OntoumlEnum):
        FIRST_MEMBER = ()
        SECOND_MEMBER = ()

    members = TestEnum.get_members()
    expected_members = {"FIRST_MEMBER", "SECOND_MEMBER"}
    assert set(members) == expected_members, f"Expected members {expected_members}, but got {members}"


def test_invalid_enum_member_name():
    """
    Test the initialization of an OntoumlEnum member with an invalid name.

    This test ensures that an OntoumlEnum member raises a ValueError if initialized with a name not in uppercase
    and underscore format.
    """
    with pytest.raises(ValueError):

        class InvalidTestEnum(OntoumlEnum):
            invalidMember = ()

        InvalidTestEnum.invalidMember


def test_enum_member_uniqueness():
    """
    Test that all enum members are unique.
    """

    class TestEnum(OntoumlEnum):
        MEMBER_ONE = ()
        MEMBER_TWO = ()

    assert len(TestEnum) == len(set(TestEnum)), "Enum members should be unique"


def test_enum_member_type():
    """
    Test that enum members are instances of the OntoumlEnum class.
    """

    class TestEnum(OntoumlEnum):
        MEMBER = ()

    assert isinstance(TestEnum.MEMBER, OntoumlEnum), "Enum members should be instances of OntoumlEnum"

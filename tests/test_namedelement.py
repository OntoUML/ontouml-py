from typing import Any

import pytest
from langstring_lib.langstring import LangString  # type: ignore
from pydantic import ValidationError

from src.classes.abstract_syntax.abstract_classes.modelelement import ModelElement
from src.classes.abstract_syntax.abstract_classes.namedelement import NamedElement


# Concrete subclass for testing
class Project(NamedElement):
    """A concrete subclass of NamedElement for testing purposes.

    Note that this is not the OntoUML Project, but just a class used for testing.

    This class inherits from NamedElement and allows the instantiation of NamedElement objects, which is normally an
    abstract class and cannot be instantiated directly.
    """

    def __init__(self, **data: dict[str, Any]):
        """Initialize a new instance of Project.

        :param data: Fields to be set on the model instance, including inherited and class-specific attributes.
        :type data: dict
        """
        super().__init__(**data)


class InvalidSubclass(NamedElement):
    def __init__(self, **data: dict[str, Any]):
        super().__init__(**data)


class Link(ModelElement):
    def __init__(self):
        pass


@pytest.fixture
def valid_langstring() -> LangString:
    """Provides a valid LangString object for testing."""
    return LangString("Test LangString")


@pytest.fixture
def valid_langstring_list() -> list[LangString]:
    """Provides a list of valid LangString objects for testing."""
    return [LangString("LangString 1"), LangString("LangString 2")]


@pytest.fixture
def invalid_langstring() -> str:
    return "Invalid LangString"


def test_namedelement_instantiation_with_arguments(
    valid_langstring: LangString, valid_langstring_list: list[LangString]
) -> None:
    """Test the instantiation of NamedElement with specific arguments.

    :param valid_langstring: A valid LangString object.
    :param valid_langstring_list: A list of valid LangString objects.
    :raises AssertionError: If attributes are not set as expected.
    """
    element = Project(
        names=[valid_langstring],
        alt_names=valid_langstring_list,
        description=valid_langstring,
        editorial_notes=valid_langstring_list,
        creators=["http://creator1.com"],
        contributors=["http://contributor1.com"],
    )
    assert element.names == [valid_langstring], "names should be initialized with the given list of LangString"
    assert (
        element.alt_names == valid_langstring_list
    ), "alt_names should be initialized with the given list of LangString"
    assert element.description == valid_langstring, "description should be initialized with the given LangString"
    assert (
        element.editorial_notes == valid_langstring_list
    ), "editorial_notes should be initialized with the given list of LangString"
    assert element.creators == ["http://creator1.com"], "creators should be initialized with the given list of URIs"
    assert element.contributors == [
        "http://contributor1.com"
    ], "contributors should be initialized with the given list of URIs"


def test_namedelement_modifying_attributes_post_instantiation(valid_langstring: LangString) -> None:
    """Test modifying NamedElement attributes after instantiation.

    :param valid_langstring: A valid LangString object.
    :raises AssertionError: If attributes are not updated as expected.
    """
    element = Project()
    element.names = [valid_langstring]
    assert element.names == [valid_langstring], "names should be updatable post-instantiation"


def test_namedelement_type_validation() -> None:
    """Test type validation for NamedElement attributes.

    :raises ValidationError: If the wrong type is assigned to an attribute.
    """
    with pytest.raises(ValidationError):
        Project(names=["Invalid Type"])  # Expect list of LangString, not list of str


def test_namedelement_abstract_class_enforcement() -> None:
    """Test that NamedElement cannot be instantiated directly due to its abstract nature.

    :raises TypeError: If NamedElement is instantiated directly.
    """
    with pytest.raises(TypeError):
        _ = NamedElement()  # Abstract class should not be instantiated


def test_namedelement_default_values() -> None:
    """Test the default values of NamedElement attributes upon instantiation.

    :raises AssertionError: If default values are not as expected.
    """
    element = Project()
    assert element.names == [], "names should default to an empty list"
    assert element.alt_names == [], "alt_names should default to an empty list"
    assert element.description is None, "description should default to None"
    assert element.editorial_notes == [], "editorial_notes should default to an empty list"
    assert element.creators == [], "creators should default to an empty list"
    assert element.contributors == [], "contributors should default to an empty list"


def test_namedelement_custom_initialization(valid_langstring: LangString) -> None:
    """Test custom initialization of NamedElement attributes.

    :param valid_langstring: A valid LangString object.
    :raises AssertionError: If custom initialization does not work as expected.
    """
    custom_names = [LangString("Custom Name")]
    element = Project(names=custom_names)
    assert element.names == custom_names, "names should be customizable during initialization"


def test_namedelement_updating_list_attributes(valid_langstring: LangString) -> None:
    """Test updating list attributes of NamedElement post-instantiation.

    :param valid_langstring: A valid LangString object.
    :raises AssertionError: If list attributes are not updatable.
    """
    element = Project()
    element.alt_names.append(valid_langstring)
    element.editorial_notes.append(valid_langstring)
    assert valid_langstring in element.alt_names, "alt_names should be updatable post-instantiation"
    assert valid_langstring in element.editorial_notes, "editorial_notes should be updatable post-instantiation"


def test_namedelement_invalid_list_type_assignment() -> None:
    """Test assignment of invalid types to list attributes of NamedElement.

    :raises ValidationError: If invalid types are assigned to list attributes.
    """
    with pytest.raises(ValidationError):
        Project(alt_names=["Invalid"])  # Expect list of LangString, not list of str


# Test initialization with invalid value and valid type
def test_initialization_with_invalid_value_and_type(invalid_langstring: str) -> None:
    """Test the instantiation of NamedElement with an invalid value but valid type for 'names'.

    :param invalid_langstring: A string that is not a valid LangString object.
    :raises ValidationError: If an invalid value is assigned to a field expecting a LangString.
    """
    with pytest.raises(ValidationError):
        Project(names=[invalid_langstring])


# Test initialization with invalid type
def test_initialization_with_invalid_type() -> None:
    """Test the instantiation of NamedElement with an invalid type for 'names'.

    :raises ValidationError: If an incorrect type is assigned to a field expecting a LangString.
    """
    with pytest.raises(ValidationError):
        Project(names=[123])


# Test initialization with empty list for 'alt_names'
def test_initialization_with_empty_list() -> None:
    """Test the instantiation of NamedElement with an empty list for 'alt_names'.

    :raises AssertionError: If 'alt_names' does not correctly handle being set to an empty list.
    """
    element = Project(alt_names=[])
    assert element.alt_names == [], "alt_names should be correctly initialized as an empty list."


# Test post-initialization assertions with invalid value and valid type
def test_post_initialization_with_invalid_value(valid_langstring_list: list[LangString]) -> None:
    """Test assigning an invalid value but valid type to 'names' after instantiation.

    :param valid_langstring_list: A list of valid LangString objects.
    :raises ValidationError: If an invalid value is assigned post-instantiation.
    """
    element = Project(names=valid_langstring_list)
    with pytest.raises(ValidationError):
        element.names = ["Invalid value"]


# Test post-initialization assertions with invalid type
def test_post_initialization_with_invalid_type() -> None:
    """Test assigning an invalid type to 'names' after instantiation.

    :raises ValidationError: If an incorrect type is assigned post-instantiation.
    """
    element = Project()
    with pytest.raises(ValidationError):
        element.names = [123]


# Test post-initialization assertions with empty list for 'alt_names'
def test_post_initialization_with_empty_list() -> None:
    """Test assigning an empty list to 'alt_names' after instantiation.

    :raises AssertionError: If 'alt_names' does not correctly handle being set to an empty list post-instantiation.
    """
    element = Project()
    element.alt_names = []
    assert element.alt_names == [], "alt_names should be correctly set to an empty list post-instantiation."


# Edge case tests for 'names'
@pytest.mark.parametrize("edge_case_value", [LangString(""), LangString(" "), LangString("\n")])
def test_names_edge_cases(edge_case_value: LangString) -> None:
    """Test initializing NamedElement with edge case LangString values for 'names'.

    :param edge_case_value: A LangString object with edge case content.
    :raises AssertionError: If 'names' does not handle edge case values correctly.
    """
    element = Project(names=[edge_case_value])
    assert element.names == [edge_case_value], "names should correctly handle edge case LangString values."


# Edge case tests for 'alt_names'
@pytest.mark.parametrize("edge_case_list", [[], [LangString("")], [LangString(" "), LangString("\n")]])
def test_alt_names_edge_cases(edge_case_list: list[LangString]) -> None:
    """Test initializing NamedElement with edge case lists for 'alt_names'.

    :param edge_case_list: A list of LangString objects with edge case content.
    :raises AssertionError: If 'alt_names' does not handle edge case lists correctly.
    """
    element = Project(alt_names=edge_case_list)
    assert element.alt_names == edge_case_list, "alt_names should correctly handle edge case lists."


# Edge case tests for 'creators' and 'contributors'
@pytest.mark.parametrize("edge_case_list", [[], [" "], ["http://example.com", ""]])
def test_uri_lists_edge_cases(edge_case_list: list[str]) -> None:
    """Test initializing NamedElement with edge case lists for 'creators' and 'contributors'.

    :param edge_case_list: A list of strings with edge case URI content.
    :raises AssertionError: If 'creators' or 'contributors' do not handle edge case lists correctly.
    """
    element = Project(creators=edge_case_list, contributors=edge_case_list)

    for item in edge_case_list:
        assert item.strip() in element.creators, "creators should correctly handle edge case lists."
        assert item.strip() in element.contributors, "contributors should correctly handle edge case lists."


# Test with null values in list attributes
def test_rejection_of_null_values_in_list_attributes() -> None:
    """Test that assigning lists with None elements to 'alt_names' and 'editorial_notes' raises a validation error.

    :raises ValidationError: If lists with None elements are assigned.
    """
    with pytest.raises(ValidationError):
        Project(alt_names=[None])
    with pytest.raises(ValidationError):
        Project(editorial_notes=[None])


# Test with extremely long strings
def test_extremely_long_strings() -> None:
    """Test assigning extremely long strings to string-based attributes.

    :raises AssertionError: If extremely long strings are not handled correctly.
    """
    long_string = "a" * 10000
    long_langstring = LangString(long_string)
    element = Project(names=[long_langstring], description=long_langstring)

    assert element.names[0].text == long_string, "names should correctly handle extremely long strings."
    assert element.description.text == long_string, "description should correctly handle extremely long strings."


# Test with special characters and Unicode
@pytest.mark.parametrize("special_string", ["特殊字符", "😊", "♠♥♦♣"])
def test_special_characters_and_unicode(special_string) -> None:
    """Test assigning strings with special characters and Unicode to string-based attributes.

    :param special_string: A string containing special characters or Unicode.
    :raises AssertionError: If special characters and Unicode are not handled correctly.
    """
    special_langstring = LangString(special_string)
    element = Project(names=[special_langstring])

    assert element.names[0].text == special_string, "names should correctly handle special characters and Unicode."


def test_alt_names_and_editorial_notes_with_valid_data() -> None:
    """Test assigning valid data to 'alt_names' and 'editorial_notes' in NamedElement.

    :raises AssertionError: If valid data is not handled correctly.
    """
    valid_langstring_list = [LangString("Test String 1"), LangString("Test String 2")]
    element = Project(alt_names=valid_langstring_list, editorial_notes=valid_langstring_list)
    assert element.alt_names == valid_langstring_list, "alt_names should accept a valid LangString list."
    assert element.editorial_notes == valid_langstring_list, "editorial_notes should accept a valid LangString list."

    empty_element = Project(alt_names=[], editorial_notes=[])
    assert empty_element.alt_names == [], "alt_names should accept an empty list."
    assert empty_element.editorial_notes == [], "editorial_notes should accept an empty list."


def test_rejection_of_invalid_data_in_list_attributes() -> None:
    """Test that assigning invalid data (lists containing None or other types) to 'alt_names' and 'editorial_notes'
    raises a validation error.

    :raises ValidationError: If invalid data is assigned.
    """
    with pytest.raises(ValidationError):
        Project(alt_names=[None])
    with pytest.raises(ValidationError):
        Project(alt_names=["Invalid Type"])
    with pytest.raises(ValidationError):
        Project(editorial_notes=[None])
    with pytest.raises(ValidationError):
        Project(editorial_notes=["Invalid Type"])


def test_valid_subclass_instantiation() -> None:
    """Test instantiation of valid subclasses defined in the allowed subclasses list.

    :raises AssertionError: If instantiation of a valid subclass raises an unexpected ValueError.
    """
    try:
        project_instance = Project()  # noqa:F841 (flake8)
        model_element_instance = Link()  # concrete subclass of ModelElement  # noqa:F841 (flake8)
    except ValueError:
        pytest.fail("Instantiation of valid subclasses should not raise ValueError.")


def test_invalid_subclass_instantiation() -> None:
    """Test that instantiating an undefined subclass raises a ValueError.

    :raises ValueError: When an undefined subclass is instantiated.
    """
    with pytest.raises(ValueError) as exc_info:
        _ = InvalidSubclass()
    assert "not an allowed subclass" in str(exc_info.value), "ValueError should mention subclass restriction."


def test_error_message_for_invalid_subclass() -> None:
    """Test the error message for instantiating an invalid subclass.

    :raises AssertionError: If the error message does not match the expected format.
    """
    with pytest.raises(ValueError) as exc_info:
        _ = InvalidSubclass()
    expected_msg_part = "not an allowed subclass"
    assert expected_msg_part in str(exc_info.value), "Error message should indicate the subclass is not allowed."

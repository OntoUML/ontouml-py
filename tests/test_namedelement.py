from typing import Any

import pytest
from langstring_lib.langstring import LangString  # type: ignore
from pydantic import ValidationError

from ontouml_py.classes.abstract_classes.modelelement import ModelElement
from ontouml_py.classes.abstract_classes.namedelement import NamedElement


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
        names={valid_langstring},
        alt_names=set(valid_langstring_list),
        description=valid_langstring,
        editorial_notes=set(valid_langstring_list),
        creators={"http://creator1.com"},
        contributors={"http://contributor1.com"},
    )
    assert element.names == set([valid_langstring]), "names should be initialized with the given list of LangString"
    assert element.alt_names == set(
        valid_langstring_list
    ), "alt_names should be initialized with the given list of LangString"
    assert element.description == valid_langstring, "description should be initialized with the given LangString"
    assert element.editorial_notes == set(
        valid_langstring_list
    ), "editorial_notes should be initialized with the given list of LangString"
    assert element.creators == set(
        ["http://creator1.com"]
    ), "creators should be initialized with the given list of URIs"
    assert element.contributors == set(
        ["http://contributor1.com"]
    ), "contributors should be initialized with the given list of URIs"


def test_namedelement_modifying_attributes_post_instantiation(valid_langstring: LangString) -> None:
    """Test modifying NamedElement attributes after instantiation.

    :param valid_langstring: A valid LangString object.
    :raises AssertionError: If attributes are not updated as expected.
    """
    element = Project()
    element.names = set([valid_langstring])
    assert element.names == set([valid_langstring]), "names should be updatable post-instantiation"


def test_namedelement_type_validation() -> None:
    """Test type validation for NamedElement attributes.

    :raises ValidationError: If the wrong type is assigned to an attribute.
    """
    with pytest.raises(ValidationError):
        Project(names="Invalid Type")  # Expect set of LangString, not str


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
    assert element.names == set(), "names should default to an empty list"
    assert element.alt_names == set(), "alt_names should default to an empty list"
    assert element.description is None, "description should default to None"
    assert element.editorial_notes == set(), "editorial_notes should default to an empty list"
    assert element.creators == set(), "creators should default to an empty list"
    assert element.contributors == set(), "contributors should default to an empty list"


def test_namedelement_custom_initialization(valid_langstring: LangString) -> None:
    """Test custom initialization of NamedElement attributes.

    :param valid_langstring: A valid LangString object.
    :raises AssertionError: If custom initialization does not work as expected.
    """
    custom_names = {LangString("Custom Name")}
    element = Project(names=custom_names)
    assert element.names == custom_names, "names should be customizable during initialization"


def test_namedelement_updating_list_attributes(valid_langstring: LangString) -> None:
    """Test updating list attributes of NamedElement post-instantiation.

    :param valid_langstring: A valid LangString object.
    :raises AssertionError: If list attributes are not updatable.
    """
    element = Project()
    element.alt_names.add(valid_langstring)
    element.editorial_notes.add(valid_langstring)
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
    element = Project()
    assert element.alt_names == set(), "alt_names should be correctly initialized as an empty list."


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
    element.alt_names = set()
    assert element.alt_names == set(), "alt_names should be correctly set to an empty list post-instantiation."


# Edge case tests for 'names'
@pytest.mark.parametrize("edge_case_value", [set([LangString("")]), set([LangString(" ")]), set([LangString("\n")])])
def test_names_edge_cases(edge_case_value: set[LangString]) -> None:
    """
    Test initializing NamedElement with edge case LangString values for 'names'.

    :param edge_case_value: A set containing a LangString object with edge case content.
    :raises AssertionError: If 'names' does not handle edge case values correctly.
    """
    element = Project(names=edge_case_value)
    assert element.names == edge_case_value, "Names should correctly handle edge case LangString values."


# Edge case tests for 'alt_names'
@pytest.mark.parametrize("edge_case_list", [[], [LangString("")], [LangString(" "), LangString("\n")]])
def test_alt_names_edge_cases(edge_case_list: list[LangString]) -> None:
    """
    Test initializing NamedElement with edge case lists for 'alt_names'.

    :param edge_case_list: A list of LangString objects with edge case content.
    :raises AssertionError: If 'alt_names' does not handle edge case lists correctly.
    """
    element = Project(alt_names=set(edge_case_list))
    expected_set = set(edge_case_list)
    assert element.alt_names == expected_set, "alt_names should correctly handle edge case lists."


# Edge case tests for 'creators' and 'contributors'
@pytest.mark.parametrize("edge_case_list", [[" "], [""], ["http://example.com", ""], ["http://example.com", " "]])
def test_uri_lists_edge_cases(edge_case_list: list[str]) -> None:
    """Test initializing NamedElement with edge case lists for 'creators' and 'contributors'.

    :param edge_case_list: A list of strings with edge case URI content.
    :raises AssertionError: If 'creators' or 'contributors' do not handle edge case lists correctly.
    """
    with pytest.raises(ValidationError):
        Project(creators=edge_case_list, contributors=edge_case_list)


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
    element = Project(names={long_langstring}, description=long_langstring)

    assert element.names == {long_langstring}, "names should correctly handle extremely long strings."
    assert element.description == long_langstring, "description should correctly handle extremely long strings."


# Test with special characters and Unicode
@pytest.mark.parametrize("special_string", ["特殊字符", "😊", "♠♥♦♣"])
def test_special_characters_and_unicode(special_string) -> None:
    """Test assigning strings with special characters and Unicode to string-based attributes.

    :param special_string: A string containing special characters or Unicode.
    :raises AssertionError: If special characters and Unicode are not handled correctly.
    """
    special_langstring = {LangString(special_string)}
    element = Project(names=special_langstring)

    assert element.names == special_langstring, "names should correctly handle special characters and Unicode."


def test_attributes_with_non_empty_valid_data() -> None:
    """
    Test assigning non-empty valid data to 'alt_names' and 'editorial_notes' in NamedElement.

    This test ensures that both 'alt_names' and 'editorial_notes' attributes correctly handle
    non-empty sets of LangString objects.

    :param None: This test function does not accept any parameters.
    :return: None
    :raises AssertionError: If non-empty valid data is not handled correctly.
    """
    valid_langstring_set = set([LangString("Test String 1"), LangString("Test String 2")])
    element = Project(alt_names=valid_langstring_set, editorial_notes=valid_langstring_set)

    assert (
        element.alt_names == valid_langstring_set
    ), "The 'alt_names' attribute should correctly store a non-empty set of valid LangString objects."
    assert (
        element.editorial_notes == valid_langstring_set
    ), "The 'editorial_notes' attribute should correctly store a non-empty set of valid LangString objects."


def test_attributes_with_empty_data() -> None:
    """
    Test assigning empty sets to 'alt_names' and 'editorial_notes' in NamedElement.

    This test verifies that both 'alt_names' and 'editorial_notes' attributes can handle
    empty sets without issues.

    :param None: This test function does not accept any parameters.
    :return: None
    :raises AssertionError: If empty sets are not handled correctly.
    """
    empty_element = Project(alt_names=set(), editorial_notes=set())

    assert empty_element.alt_names == set(), "The 'alt_names' attribute should correctly handle an empty set."
    assert (
        empty_element.editorial_notes == set()
    ), "The 'editorial_notes' attribute should correctly handle an empty set."


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
    """
    Test the instantiation of a valid subclass of NamedElement.

    :raises AssertionError: If a valid subclass cannot be instantiated.
    """
    try:
        project = Project()
        assert isinstance(project, NamedElement), "Project should be an instance of NamedElement"
    except Exception as e:
        pytest.fail(f"Instantiation of a valid subclass failed: {e}")


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


def test_direct_instantiation_of_abstract_class() -> None:
    """
    Test that direct instantiation of the abstract class NamedElement is not allowed.

    :raises TypeError: If NamedElement is instantiated directly.
    """
    with pytest.raises(TypeError, match="Can't instantiate abstract class NamedElement"):
        NamedElement()  # Attempt to instantiate an abstract class


def test_subclass_without_required_methods() -> None:
    """
    Test that a subclass missing required abstract methods cannot be instantiated.

    :raises TypeError: If a subclass without required abstract methods is instantiated.
    """

    class IncompleteSubclass(NamedElement):
        pass

    with pytest.raises(TypeError, match="Can't instantiate abstract class IncompleteSubclass"):
        IncompleteSubclass()  # Attempt to instantiate a subclass without implementing abstract methods


def test_subclass_with_all_required_methods() -> None:
    """
    Test the instantiation of a subclass that implements all required abstract methods of NamedElement.

    :raises AssertionError: If a subclass with all required methods cannot be instantiated.
    """

    try:
        complete_subclass = Project()
        assert isinstance(complete_subclass, NamedElement), "CompleteSubclass should be an instance of NamedElement"
    except Exception as e:
        pytest.fail(f"Instantiation of a complete subclass failed: {e}")


# Test with mixed valid and invalid LangString objects in lists
def test_mixed_valid_invalid_langstring_in_lists() -> None:
    """
    Test the instantiation of NamedElement with a mix of valid and invalid LangString objects in lists.

    :raises ValidationError: If lists contain invalid LangString objects.
    """
    valid_langstring = LangString("Valid LangString")
    invalid_langstring = "Invalid LangString"
    with pytest.raises(ValidationError):
        Project(names=[valid_langstring, invalid_langstring])


# Test with extremely short strings
@pytest.mark.parametrize("short_string", ["a", " ", ""])
def test_extremely_short_strings(short_string: str) -> None:
    """
    Test assigning extremely short strings to string-based attributes of NamedElement.

    :param short_string: A string containing a single character or whitespace.
    :raises AssertionError: If extremely short strings are not handled correctly.
    """
    short_langstring = LangString(short_string)
    element = Project(names={short_langstring})
    assert element.names == {short_langstring}, "names should correctly handle extremely short strings."


# Test with numeric and special characters in URIs
@pytest.mark.parametrize("uri", ["http://example1.com/123", "http://example2.com/?q=♠♥♦♣"])
def test_numeric_special_characters_in_uris(uri: str) -> None:
    """
    Test initializing NamedElement with URIs containing numeric and special characters.

    :param uri: A URI string containing numeric and/or special characters.
    :raises AssertionError: If URIs with numeric and special characters are not handled correctly.
    """
    element = Project(creators=[uri], contributors=[uri])
    assert uri in element.creators, "creators should correctly handle URIs with numeric and special characters."
    assert uri in element.contributors, "contributors should correctly handle URIs with numeric and special characters."


# Test with null values for optional attributes
def test_null_values_for_optional_attributes() -> None:
    """
    Test assigning null values to optional attributes of NamedElement.

    :raises AssertionError: If null values for optional attributes are not handled correctly.
    """
    element = Project(description=None)
    assert element.description is None, "Optional attribute 'description' should accept null values."


# Test with different types of whitespace in strings
@pytest.mark.parametrize("whitespace", ["\t", "\n", "\r", " \t\n"])
def test_whitespace_in_strings(whitespace: str) -> None:
    """
    Test assigning strings with different types of whitespace to string-based attributes of NamedElement.

    :param whitespace: A string containing various types of whitespace characters.
    :raises AssertionError: If strings with different types of whitespace are not handled correctly.
    """
    whitespace_langstring = LangString(whitespace)
    element = Project(names=set([whitespace_langstring]))
    assert whitespace_langstring in element.names, "names should correctly handle strings with various whitespace."


# Test with maximum number of elements in lists
def test_maximum_elements_in_lists() -> None:
    """
    Test assigning the maximum number of elements to list attributes of NamedElement.

    :raises AssertionError: If lists do not handle the maximum number of elements correctly.
    """
    max_elements = set([LangString(f"LangString {i}") for i in range(1000)])
    element = Project(alt_names=max_elements, editorial_notes=max_elements)
    assert element.alt_names == max_elements, "alt_names should handle maximum number of elements."
    assert element.editorial_notes == max_elements, "editorial_notes should handle maximum number of elements."


# Test with empty strings in URI lists
def test_empty_strings_in_uri_lists() -> None:
    """
    Test assigning lists containing empty strings to URI attributes of NamedElement.

    :raises ValidationError: If lists contain empty strings for URI attributes.
    """
    with pytest.raises(ValidationError):
        Project(creators=[""], contributors=[""])


# Test with mixed case strings
@pytest.mark.parametrize("mixed_case_string", ["MixedCase", "MIXED", "mixed"])
def test_mixed_case_strings(mixed_case_string: str) -> None:
    """
    Test assigning mixed case strings to string-based attributes of NamedElement.

    :param mixed_case_string: A string containing mixed case characters.
    :raises AssertionError: If mixed case strings are not handled correctly.
    """
    mixed_case_langstring = {LangString(mixed_case_string)}
    element = Project(names=mixed_case_langstring)
    assert element.names == mixed_case_langstring, "names should correctly handle mixed case strings."


# Test with duplicate elements in lists
def test_duplicate_elements_in_lists() -> None:
    """
    Test assigning lists with duplicate elements to list attributes of NamedElement.

    :raises AssertionError: If lists do not handle duplicate elements correctly.
    """
    duplicate_langstring = LangString("Duplicate")
    element = Project(alt_names=set([duplicate_langstring, duplicate_langstring]))
    assert len(element.alt_names) == 1, "alt_names should handle duplicate elements, resulting in a single inclusion."


def test_default_type_of_names() -> None:
    """
    Test the default type of the 'names' attribute in NamedElement.

    Ensures that the 'names' attribute, when not explicitly initialized, defaults to an empty list.

    :return: None
    :raises AssertionError: If the default type of 'names' is not a list.
    """
    element = Project()
    assert isinstance(element.names, set), "The default type of 'names' should be a list."


def test_default_type_of_alt_names() -> None:
    """
    Test the default type of the 'alt_names' attribute in NamedElement.

    Verifies that the 'alt_names' attribute, when not explicitly initialized, defaults to an empty list.

    :return: None
    :raises AssertionError: If the default type of 'alt_names' is not a list.
    """
    element = Project()
    assert isinstance(element.alt_names, set), "The default type of 'alt_names' should be a list."


def test_default_type_of_description() -> None:
    """
    Test the default type of the 'description' attribute in NamedElement.

    Checks that the 'description' attribute, when not explicitly initialized, defaults to None.

    :return: None
    :raises AssertionError: If the default type of 'description' is not None.
    """
    element = Project()
    assert element.description is None, "The default type of 'description' should be None."


def test_default_type_of_editorial_notes() -> None:
    """
    Test the default type of the 'editorial_notes' attribute in NamedElement.

    Confirms that the 'editorial_notes' attribute, when not explicitly initialized, defaults to an empty list.

    :return: None
    :raises AssertionError: If the default type of 'editorial_notes' is not a list.
    """
    element = Project()
    assert isinstance(element.editorial_notes, set), "The default type of 'editorial_notes' should be a list."


def test_default_type_of_creators() -> None:
    """
    Test the default type of the 'creators' attribute in NamedElement.

    Ensures that the 'creators' attribute, when not explicitly initialized, defaults to an empty list.

    :return: None
    :raises AssertionError: If the default type of 'creators' is not a list.
    """
    element = Project()
    assert isinstance(element.creators, set), "The default type of 'creators' should be a list."


def test_default_type_of_contributors() -> None:
    """
    Test the default type of the 'contributors' attribute in NamedElement.

    Verifies that the 'contributors' attribute, when not explicitly initialized, defaults to an empty list.

    :return: None
    :raises AssertionError: If the default type of 'contributors' is not a list.
    """
    element = Project()
    assert isinstance(element.contributors, set), "The default type of 'contributors' should be a list."


def test_access_non_existent_attribute() -> None:
    """
    Test accessing a non-existent attribute in NamedElement.

    This test ensures that attempting to access an attribute that does not exist in the NamedElement class raises an
    AttributeError.

    :return: None
    :raises AssertionError: If accessing a non-existent attribute does not raise an AttributeError.
    """
    element = Project()
    with pytest.raises(AttributeError) as exc_info:
        _ = element.non_existent_attribute
    assert "object has no attribute 'non_existent_attribute'" in str(
        exc_info.value
    ), "Accessing a non-existent attribute should raise an AttributeError with a specific message."


def test_assign_to_non_existent_attribute() -> None:
    """
    Test assigning a value to a non-existent attribute in NamedElement.

    Verifies that attempting to assign a value to an attribute that does not exist in the NamedElement class raises an
    AttributeError.

    :return: None
    :raises AssertionError: If assigning to a non-existent attribute does not raise an AttributeError.
    """
    element = Project()
    with pytest.raises(ValidationError):
        element.non_existent_attribute = "Test Value"


def test_method_call_on_non_existent_attribute() -> None:
    """
    Test calling a method on a non-existent attribute in NamedElement.

    Ensures that attempting to call a method on an attribute that does not exist in the NamedElement class raises an
    AttributeError.

    :return: None
    :raises AssertionError: If calling a method on a non-existent attribute does not raise an AttributeError.
    """
    element = Project()
    with pytest.raises(AttributeError) as exc_info:
        _ = element.non_existent_attribute.method_call()
    assert "object has no attribute 'non_existent_attribute'" in str(
        exc_info.value
    ), "Calling a method on a non-existent attribute should raise an AttributeError with a specific message."


def test_instantiation_with_unknown_arguments() -> None:
    """
    Test the instantiation of NamedElement with unknown arguments.

    This test verifies that attempting to instantiate a NamedElement (or its subclass) with arguments that are not
    defined in the class raises a TypeError.

    :return: None
    :raises AssertionError: If instantiation with unknown arguments does not raise a TypeError.
    """
    with pytest.raises(ValidationError):
        _ = Project(unknown_arg="Test Value")


def test_modifying_instance_with_unknown_arguments() -> None:
    """
    Test modifying an instance of NamedElement with unknown arguments.

    Ensures that attempting to modify an instance of NamedElement (or its subclass) with arguments that are not
    defined in the class raises a TypeError.

    :return: None
    :raises AssertionError: If modification with unknown arguments does not raise a TypeError.
    """
    element = Project()
    with pytest.raises(AttributeError):
        element.modify(unknown_arg="Test Value")


def test_setting_unknown_attributes_post_instantiation() -> None:
    """
    Test setting unknown attributes on an instance of NamedElement post-instantiation.

    Verifies that attempting to set an unknown attribute on an instance of NamedElement (or its subclass) post-
    instantiation raises an AttributeError.

    :return: None
    :raises AssertionError: If setting an unknown attribute post-instantiation does not raise an AttributeError.
    """
    element = Project()
    with pytest.raises(ValidationError):
        element.unknown_attribute = "Test Value"


def test_namedelement_with_single_character_names() -> None:
    """
    Test the instantiation of NamedElement with single-character names.

    This test verifies that NamedElement (or its subclass) can be instantiated with single-character strings in the
    'names' attribute, which is a valid but unusual use case.

    :return: None
    :raises AssertionError: If instantiation with single-character names fails or is handled incorrectly.
    """
    single_char_langstring = LangString("A", "en")
    element = Project(names={single_char_langstring})
    assert single_char_langstring in element.names, "NamedElement should correctly handle single-character names."


def test_namedelement_with_reversed_uri_lists() -> None:
    """
    Test the instantiation of NamedElement with reversed URI lists.

    This test checks if NamedElement (or its subclass) can handle URI lists for 'creators' and 'contributors' where
    the URIs are in a reversed order, which is a valid but unusual scenario.

    :return: None
    :raises AssertionError: If instantiation with reversed URI lists is not handled correctly.
    """
    reversed_uris = set(["http://example.com/2", "http://example.com/1"])
    element = Project(creators=reversed_uris, contributors=reversed_uris)
    assert (
        element.creators == reversed_uris and element.contributors == reversed_uris
    ), "NamedElement should correctly handle reversed URI lists."


def test_namedelement_with_alternating_case_descriptions() -> None:
    """
    Test the instantiation of NamedElement with alternating case descriptions.

    Verifies that NamedElement (or its subclass) can be instantiated with a description having alternating case,
    which is an unusual but valid string format.

    :return: None
    :raises AssertionError: If instantiation with alternating case descriptions is not handled correctly.
    """
    alt_case_description = LangString("AlTeRnAtInG CaSe")
    element = Project(description=alt_case_description)
    assert (
        element.description == alt_case_description
    ), "NamedElement should correctly handle descriptions with alternating case."

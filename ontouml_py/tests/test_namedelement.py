import datetime
from typing import Optional, List

import pytest
from langstring_lib.langstring import LangString

from ontouml_py.classes.abastract_syntax.namedelement import NamedElement


class NamedElementStub(NamedElement):
    """A stub class that extends the abstract NamedElement class for testing purposes."""

    def __init__(
        self,
        created: Optional[datetime.datetime] = None,
        modified: Optional[datetime.datetime] = None,
        prefName: Optional[LangString] = None,
        altNames: Optional[List[LangString]] = None,
        description: Optional[LangString] = None,
        editorialNotes: Optional[LangString] = None,
        creators: Optional[List[str]] = None,
        contributors: Optional[List[str]] = None,
    ):
        super().__init__(created, modified, prefName, altNames, description, editorialNotes, creators, contributors)


# Test cases
@pytest.mark.parametrize(
    "created, modified, expected_created",
    [
        (None, None, datetime.datetime.now()),
        (datetime.datetime(2021, 1, 1), None, datetime.datetime(2021, 1, 1)),
    ],
)
def test_namedelement_initialization(
    created: Optional[datetime.datetime], modified: Optional[datetime.datetime], expected_created: datetime.datetime
) -> None:
    """Test the initialization of NamedElementStub, ensuring it sets the 'created' and 'modified' dates correctly.

    :param created: The date the element is created or None to test the default behavior.
    :param modified: The date the element was last modified or None if it hasn't been modified.
    :param expected_created: The expected value of the 'created' attribute after initialization.
    """
    element = NamedElementStub(created=created, modified=modified)
    assert element.created.date() == expected_created.date(), "The 'created' date should match the expected date"
    if modified:
        assert element.modified == modified, "The 'modified' date should be set when provided"
    else:
        assert element.modified is None, "The 'modified' date should be None when not provided"


@pytest.mark.parametrize(
    "prefName",
    [
        (LangString("Test Name")),
    ],
)
def test_namedelement_prefName_initialization(prefName: LangString) -> None:
    """Test the initialization of NamedElementStub, ensuring it sets the 'prefName' attribute correctly.

    :param prefName: The preferred name of the element, as a LangString object.
    """
    element = NamedElementStub(prefName=prefName)
    assert element.prefName == prefName, "The 'prefName' should be set correctly during initialization"


# Test the validation logic for 'altNames'
@pytest.mark.parametrize(
    "altNames, is_valid",
    [
        ([LangString("Alternative Name 1"), LangString("Alternative Name 2")], True),
        ([], True),
        # Testing empty list of alternative names
        (None, True),  # Testing 'None' as a value for 'altNames'
        ([123, "Invalid LangString"], False),  # Testing invalid list contents
    ],
)
def test_namedelement_altNames_validation(altNames: Optional[List[LangString]], is_valid: bool) -> None:
    """Test the validation of 'altNames' attribute during the initialization of NamedElementStub.

    :param altNames: A list of alternative names or None.
    :param is_valid: Boolean indicating whether the 'altNames' is valid or not.
    """
    if is_valid:
        element = NamedElementStub(altNames=altNames)
        assert element.altNames == altNames, "The 'altNames' should be set correctly when valid"
    else:
        with pytest.raises(TypeError):
            NamedElementStub(altNames=altNames)


# Test the setting and validation logic for 'description' and 'editorialNotes'
@pytest.mark.parametrize(
    "description, editorialNotes",
    [
        (LangString("Description text"), LangString("Editorial notes text")),
        (None, None),
        # Testing 'None' values for both attributes
        (LangString(""), LangString("")),  # Testing empty LangString objects
    ],
)
def test_namedelement_description_editorialNotes_initialization(
    description: Optional[LangString], editorialNotes: Optional[LangString]
) -> None:
    """Test the initialization of NamedElementStub, ensuring 'description' and 'editorialNotes' are set correctly.

    :param description: A LangString object representing the description or None.
    :param editorialNotes: A LangString object representing the editorial notes or None.
    """
    element = NamedElementStub(description=description, editorialNotes=editorialNotes)
    assert element.description == description, "The 'description' should be set correctly during initialization"
    assert (
        element.editorialNotes == editorialNotes
    ), "The 'editorialNotes' should be set correctly during initialization"


# Test to ensure that the current time is used by default for 'created' attribute when it is not provided
def test_namedelement_default_created_time() -> None:
    """Test the default behavior of the 'created' attribute to ensure it is set to the current time when not \
    provided."""
    element = NamedElementStub()
    assert element.created <= datetime.datetime.now(), "The 'created' attribute should default to the current time"
    assert element.created > datetime.datetime.now() - datetime.timedelta(
        seconds=1
    ), "The 'created' attribute should be very close to the current time"


# Test invalid argument types for 'prefName', 'description', and 'editorialNotes'
@pytest.mark.parametrize(
    "attr_name, invalid_value",
    [
        ("prefName", "Invalid type"),  # Non-LangString type for 'prefName'
        ("description", 123),  # Non-LangString type for 'description'
        ("editorialNotes", [LangString("Note")]),  # Non-LangString type for 'editorialNotes'
    ],
)
def test_namedelement_invalid_argument_types(attr_name: str, invalid_value) -> None:
    """Test the initialization of NamedElementStub with invalid argument types.

    :param attr_name: Name of the attribute being tested.
    :param invalid_value: An invalid value for the attribute.
    """
    with pytest.raises(TypeError):
        NamedElementStub(**{attr_name: invalid_value})


# Test invalid argument values for 'altNames'
@pytest.mark.parametrize(
    "invalid_altNames",
    [
        ("Invalid type"),  # Single non-LangString type in list
        (["Valid", 123, "Invalid"]),  # Mixed types, with invalid entries
        (123),  # Non-list type
    ],
)
def test_namedelement_invalid_altNames_values(invalid_altNames) -> None:
    """Test the initialization of NamedElementStub with invalid values for 'altNames'.

    :param invalid_altNames: An invalid value for the 'altNames' list.
    """
    with pytest.raises((TypeError, ValueError)):
        NamedElementStub(altNames=invalid_altNames)


# Test for attributes set as None to verify that they are allowed and handled correctly
@pytest.mark.parametrize(
    "attr_name",
    [
        ("prefName"),
        ("description"),
        ("editorialNotes"),
    ],
)
def test_namedelement_attributes_set_as_none(attr_name: str) -> None:
    """Test the initialization of NamedElementStub with attributes set as None.

    :param attr_name: Name of the attribute being tested.
    """
    element = NamedElementStub(**{attr_name: None})
    assert getattr(element, attr_name) is None, f"The '{attr_name}' attribute should be allowed to be set as None"


# Test edge cases for 'prefName', 'description', and 'editorialNotes' with unusual but valid inputs
@pytest.mark.parametrize(
    "attr_name, edge_case_value",
    [
        ("prefName", LangString("")),  # Empty string in LangString for 'prefName'
        ("description", LangString(" ")),  # Whitespace string in LangString for 'description'
        ("editorialNotes", LangString("\n")),  # Newline character in LangString for 'editorialNotes'
    ],
)
def test_namedelement_edge_cases_for_langstring_attributes(attr_name: str, edge_case_value: LangString) -> None:
    """Test the initialization of NamedElementStub with edge case values for LangString attributes.

    :param attr_name: Name of the attribute being tested.
    :param edge_case_value: An edge case LangString value for the attribute.
    """
    element = NamedElementStub(**{attr_name: edge_case_value})
    assert (
        getattr(element, attr_name) == edge_case_value
    ), f"The '{attr_name}' attribute should handle edge case LangString values"


# Test edge cases for 'altNames' with unusual but valid inputs
@pytest.mark.parametrize(
    "edge_case_altNames",
    [
        ([LangString("")]),  # List with empty string LangString
        ([LangString(" "), LangString("\t")]),  # List with whitespace and tab characters in LangString
        ([LangString("Name")] * 100),  # List with a large number of the same LangString
    ],
)
def test_namedelement_edge_cases_for_altNames(edge_case_altNames: List[LangString]) -> None:
    """Test the initialization of NamedElementStub with edge case values for 'altNames' list.

    :param edge_case_altNames: An edge case list of LangString objects for 'altNames'.
    """
    element = NamedElementStub(altNames=edge_case_altNames)
    assert element.altNames == edge_case_altNames, "The 'altNames' attribute should handle edge case lists"


# Test initialization with edge case datetime values
@pytest.mark.parametrize(
    "created, modified",
    [
        (datetime.datetime.min, datetime.datetime.min),  # Testing minimum possible datetime
        (datetime.datetime.max, datetime.datetime.max),  # Testing maximum possible datetime
    ],
)
def test_namedelement_edge_cases_for_datetime_attributes(
    created: datetime.datetime, modified: datetime.datetime
) -> None:
    """Test the initialization of NamedElementStub with edge case datetime values for 'created' and 'modified'.

    :param created: An edge case datetime value for when the element was created.
    :param modified: An edge case datetime value for when the element was last modified.
    """
    element = NamedElementStub(created=created, modified=modified)
    assert element.created == created, "The 'created' attribute should handle edge case datetime values"
    assert element.modified == modified, "The 'modified' attribute should handle edge case datetime values"


# Test the initialization and validation logic for 'creators'
@pytest.mark.parametrize(
    "creators, is_valid",
    [
        (["http://creator1.com", "http://creator2.com"], True),  # Valid URIs
        ([], True),  # Testing empty list of creators
        (None, True),  # Testing 'None' as a value for 'creators'
        (["not-a-uri", 123], False),  # Testing invalid list contents: not valid URIs and wrong type
    ],
)
def test_namedelement_creators_validation(creators: Optional[List[str]], is_valid: bool) -> None:
    """Test the validation of 'creators' attribute during the initialization of NamedElementStub.

    :param creators: A list of URIs or None.
    :param is_valid: Boolean indicating whether the 'creators' is valid or not.
    """
    if is_valid:
        element = NamedElementStub(creators=creators)
        assert element.creators == creators, "The 'creators' should be set correctly when valid"
    else:
        with pytest.raises((TypeError, ValueError)):
            NamedElementStub(creators=creators)


# Test the initialization and validation logic for 'contributors'
@pytest.mark.parametrize(
    "contributors, is_valid",
    [
        (["http://contributor1.com", "http://contributor2.com"], True),  # Valid URIs
        ([], True),  # Testing empty list of contributors
        (None, True),  # Testing 'None' as a value for 'contributors'
        (["not-a-uri", 123], False),  # Testing invalid list contents: not valid URIs and wrong type
    ],
)
def test_namedelement_contributors_validation(contributors: Optional[List[str]], is_valid: bool) -> None:
    """Test the validation of 'contributors' attribute during the initialization of NamedElementStub.

    :param contributors: A list of URIs or None.
    :param is_valid: Boolean indicating whether the 'contributors' is valid or not.
    """
    if is_valid:
        element = NamedElementStub(contributors=contributors)
        assert element.contributors == contributors, "The 'contributors' should be set correctly when valid"
    else:
        with pytest.raises((TypeError, ValueError)):
            NamedElementStub(contributors=contributors)


# Test edge cases for 'creators' and 'contributors' with unusual but valid inputs
@pytest.mark.parametrize(
    "attr_name, edge_case_values",
    [
        ("creators", ["http://creator.com", ""]),  # Testing a valid URI and an empty string
        ("contributors", ["http://contributor.com", " ", "http://contributor2.com"]),  # Valid URIs and a whitespace
    ],
)
def test_namedelement_edge_cases_for_uri_attributes(attr_name: str, edge_case_values: List[str]) -> None:
    """Test the initialization of NamedElementStub with edge case values for URI attributes.

    :param attr_name: Name of the attribute being tested.
    :param edge_case_values: An edge case list of URIs for the attribute.
    """
    kwargs = {attr_name: edge_case_values}
    element = NamedElementStub(**kwargs)
    assert (
        getattr(element, attr_name) == edge_case_values
    ), f"The '{attr_name}' attribute should handle edge case URI values"

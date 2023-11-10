from datetime import datetime, timezone, timedelta

import pytest
from langstring_lib.langstring import LangString
from pydantic import ValidationError

from ontouml_py.classes.abstract_syntax.project import Project
from ontouml_py.classes.ontoumlelement import OntoumlElement


# Utility functions and fixtures
def create_langstring(text: str) -> LangString:
    """
    Create a LangString object from a given text.

    :param text: The text to be converted into a LangString.
    :type text: str
    :return: A LangString object containing the provided text.
    :rtype: LangString
    """
    return LangString(text)


class OntoumlElementStub(OntoumlElement):
    """
    A stub class for OntoumlElement.

    This class serves as a concrete subclass of OntoumlElement, primarily used for testing and demonstration purposes.
    It does not introduce additional attributes or methods beyond those inherited from OntoumlElement, and is
    typically instantiated to create simple examples of OntoumlElement objects.
    """

    def __init__(self):
        """
        Initialize a new instance of OntoumlElementStub.

        As a stub implementation, this constructor intentionally does not perform any additional initialization
        beyond that provided by the OntoumlElement class. It serves to allow the creation of OntoumlElementStub
        instances where an actual OntoumlElement object is needed, but without any specialized behavior or attributes.
        """
        # intentionally empty
        pass


def create_ontoumlelement() -> OntoumlElementStub:
    """
    Create and return an instance of OntoumlElementStub.

    :return: An instance of OntoumlElementStub.
    :rtype: OntoumlElementStub
    """
    return OntoumlElementStub()


@pytest.fixture
def valid_langstring_list() -> list[LangString]:
    """
    Provide a fixture for creating a list of valid LangString objects.

    :return: A list of LangString objects.
    :rtype: list[LangString]
    """
    return [create_langstring("Keyword1"), create_langstring("Keyword2")]


@pytest.fixture
def valid_ontoumlelement_list() -> list[OntoumlElementStub]:
    """
    Provide a fixture for creating a list of valid OntoumlElementStub objects.

    :return: A list of OntoumlElementStub objects.
    :rtype: list[OntoumlElementStub]
    """
    return [OntoumlElementStub(), OntoumlElementStub()]


# Test for successful initialization of Project
def test_project_initialization(
    valid_langstring_list: list[LangString], valid_ontoumlelement_list: list[OntoumlElementStub]
) -> None:
    """
    Test the successful initialization of a Project instance with valid parameters.

    :param valid_langstring_list: A list of LangString objects for testing.
    :type valid_langstring_list: list[LangString]
    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    """
    project = Project(
        pref_name=create_langstring("Project Name"),
        alt_names=valid_langstring_list,
        description=create_langstring("Project Description"),
        editorial_notes=valid_langstring_list,
        creators=["http://creator1.com", "http://creator2.com"],
        contributors=["http://contributor1.com", "http://contributor2.com"],
        elements=valid_ontoumlelement_list,
        acronyms=["P1", "P2"],
        bibliographic_citations=["Citation1", "Citation2"],
        keywords=valid_langstring_list,
        landing_pages=["http://landingpage1.com", "http://landingpage2.com"],
        languages=["en", "pt"],
        namespace="http://example.org/ns",
        sources=["http://source1.com", "http://source2.com"],
        access_rights=["Public", "Restricted"],
        ontology_types=["Formal", "Informal"],
        themes=["Theme1", "Theme2"],
        license="CC BY 4.0",
        contexts=["Context1", "Context2"],
        designed_for_task=["Task1", "Task2"],
        publisher="Publisher Name",
    )

    # Assertions to validate initialization
    assert project.pref_name.text == "Project Name", "Project should have the correct 'pref_name'."
    assert project.alt_names == valid_langstring_list, "Project should have the correct 'alt_names'."
    assert project.description.text == "Project Description", "Project should have the correct 'description'."
    assert project.editorial_notes == valid_langstring_list, "Project should have the correct 'editorial_notes'."
    assert project.creators == [
        "http://creator1.com",
        "http://creator2.com",
    ], "Project should have the correct 'creators'."
    assert project.contributors == [
        "http://contributor1.com",
        "http://contributor2.com",
    ], "Project should have the correct 'contributors'."
    assert project.elements == valid_ontoumlelement_list, "Project should have the correct 'elements'."
    assert project.acronyms == ["P1", "P2"], "Project should have the correct 'acronyms'."
    assert project.bibliographic_citations == [
        "Citation1",
        "Citation2",
    ], "Project should have the correct 'bibliographic_citations'."
    assert project.keywords == valid_langstring_list, "Project should have the correct 'keywords'."
    assert project.landing_pages == [
        "http://landingpage1.com",
        "http://landingpage2.com",
    ], "Project should have the correct 'landing_pages'."
    assert project.languages == ["en", "pt"], "Project should have the correct 'languages'."
    assert project.namespace == "http://example.org/ns", "Project should have the correct 'namespace'."
    assert project.sources == ["http://source1.com", "http://source2.com"], "Project should have the correct 'sources'."
    assert project.access_rights == ["Public", "Restricted"], "Project should have the correct 'access_rights'."
    assert project.ontology_types == ["Formal", "Informal"], "Project should have the correct 'ontology_types'."
    assert project.themes == ["Theme1", "Theme2"], "Project should have the correct 'themes'."
    assert project.license == "CC BY 4.0", "Project should have the correct 'license'."
    assert project.contexts == ["Context1", "Context2"], "Project should have the correct 'contexts'."
    assert project.designed_for_task == ["Task1", "Task2"], "Project should have the correct 'designed_for_task'."
    assert project.publisher == "Publisher Name", "Project should have the correct 'publisher'."


# Test assertion after non-empty creation with empty string, list, or tuple - mutability test
def test_project_mutable_update_empty_values() -> None:
    """
    Test updating project attributes to empty values after non-empty initialization.

    :raises AssertionError: If the attributes don't update to empty values correctly.
    """
    project = Project(pref_name=create_langstring("Initial"), alt_names=[create_langstring("Alt")])
    project.pref_name = create_langstring("")
    project.alt_names = []
    assert project.pref_name.text == "" and project.alt_names == [], "Should update to empty values correctly."


def test_project_invalid_value_in_list_post_init() -> None:
    """
    Test assigning an invalid value in a list attribute after non-empty initialization.

    :raises ValidationError: If the list accepts an invalid value.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    with pytest.raises(ValidationError):
        project.alt_names = [create_langstring("Another"), None]  # Reassign with a new list containing an invalid value


def test_project_invalid_type_in_list_post_init() -> None:
    """
    Test assigning an invalid type in a list attribute after non-empty initialization.

    :raises ValidationError: If the list accepts an invalid type.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    with pytest.raises(ValidationError):
        project.alt_names = [create_langstring("Another"), 123]  # Reassign with a new list containing an invalid type


# Test for None in list after non-empty initialization
def test_project_none_in_list_post_init() -> None:
    """
    Test assigning None to a list attribute after non-empty initialization.

    :raises ValueError: If None is assigned to a list attribute.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    with pytest.raises(ValueError):
        project.alt_names = None


# Test for empty string in list after non-empty initialization
def test_project_empty_string_in_list_post_init() -> None:
    """
    Test appending an empty string to a list attribute after non-empty initialization.

    :raises AssertionError: If empty string in list is not handled correctly.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    project.alt_names.append(create_langstring(""))
    assert project.alt_names[-1].text == "", "Should handle empty string in list correctly."


# Test for updating list attribute with a mix of valid and None values
def test_project_update_list_with_mixed_values() -> None:
    """
    Test updating a list attribute with a mix of valid and None values.

    :raises ValidationError: If mixed values are incorrectly accepted.
    """
    project = Project(acronyms=["AC1"])
    with pytest.raises(ValidationError):
        project.acronyms = ["AC2", None]


# Test for updating list attribute with a mix of valid and invalid types
def test_project_update_list_with_mixed_types() -> None:
    """
    Test updating a list attribute with a mix of valid and invalid types.

    :raises ValidationError: If mixed types are incorrectly accepted.
    """
    project = Project(acronyms=["AC1"])
    with pytest.raises(ValidationError):
        project.acronyms = ["AC2", 123]


def test_project_interaction_with_langstring_complex() -> None:
    """
    Test Project initialization with complex LangString objects.

    :raises AssertionError: If complex LangString objects are not handled correctly.
    """
    # Create LangString objects for each language
    langstring_en = LangString("Complex Name", "en")
    langstring_pt = LangString("Nome Complexo", "pt")

    # Use these LangString objects in a list for an attribute like keywords
    project = Project(keywords=[langstring_en, langstring_pt])

    # Check if the LangString objects are correctly assigned and stored
    assert project.keywords[0].text == "Complex Name", "English LangString should be correctly set."
    assert project.keywords[0].lang == "en", "Language for English LangString should be 'en'."
    assert project.keywords[1].text == "Nome Complexo", "Portuguese LangString should be correctly set."
    assert project.keywords[1].lang == "pt", "Language for Portuguese LangString should be 'pt'."


def test_project_datetime_with_different_timezones() -> None:
    """
    Test Project initialization with datetime objects in different time zones.

    :raises AssertionError: If datetime objects with different time zones are not handled correctly.
    """
    # Example using timezone aware datetime objects
    aware_datetime = datetime(2022, 1, 1, tzinfo=timezone.utc)
    project = Project(created=aware_datetime)
    assert project.created == aware_datetime, "Project should handle timezone aware datetime objects."


def test_project_extreme_values_handling() -> None:
    """
    Test Project handling extreme and boundary values in attributes.

    :raises AssertionError: If extreme and boundary values are not handled correctly.
    """
    very_long_string = "x" * 10000
    project = Project(namespace=very_long_string)
    assert project.namespace == very_long_string, "Project should handle very long string values."


def test_project_default_values_initialization() -> None:
    """
    Test initialization of Project with default values.

    :raises AssertionError: If default values are not set correctly.
    """
    project = Project()
    assert isinstance(project.elements, list), "Elements should default to an empty list."
    assert isinstance(project.acronyms, list), "Acronyms should default to an empty list."
    assert isinstance(project.bibliographic_citations, list), "Bibliographic citations should default to an empty list."
    assert isinstance(project.keywords, list), "Keywords should default to an empty list."
    assert isinstance(project.landing_pages, list), "Landing pages should default to an empty list."
    assert isinstance(project.languages, list), "Languages should default to an empty list."
    assert project.namespace is None, "Namespace should default to None."
    assert isinstance(project.sources, list), "Sources should default to an empty list."
    assert isinstance(project.access_rights, list), "Access rights should default to an empty list."
    assert isinstance(project.ontology_types, list), "Ontology types should default to an empty list."
    assert isinstance(project.themes, list), "Themes should default to an empty list."
    assert project.license is None, "License should default to None."
    assert isinstance(project.contexts, list), "Contexts should default to an empty list."
    assert isinstance(project.designed_for_task, list), "Designed for task should default to an empty list."
    assert project.publisher is None, "Publisher should default to None."


# Tests for edge cases


def test_project_large_list_attributes() -> None:
    """Test handling large lists for list-type attributes."""
    large_elements = [OntoumlElementStub() for _ in range(1000)]
    large_strings = ["string" * 100 for _ in range(1000)]

    project = Project(elements=large_elements, acronyms=large_strings, bibliographic_citations=large_strings)

    assert len(project.elements) == 1000, "Should handle large lists for 'elements'."
    assert len(project.acronyms) == 1000, "Should handle large lists for 'acronyms'."
    assert len(project.bibliographic_citations) == 1000, "Should handle large lists for 'bibliographic_citations'."


def test_project_extreme_string_values() -> None:
    """Test handling extreme string values for string-type attributes."""
    very_long_string = "x" * 10000
    unusual_characters = "!@#$%^&*()_+|}{\":?><,./;'[]\\=-`~"

    project = Project(namespace=very_long_string, license=unusual_characters, publisher=very_long_string)

    assert project.namespace == very_long_string, "Should handle very long strings for 'namespace'."
    assert project.license == unusual_characters, "Should handle unusual characters for 'license'."
    assert project.publisher == very_long_string, "Should handle very long strings for 'publisher'."


def test_project_mixing_types_in_lists() -> None:
    """Test assigning mixed types in list attributes."""
    with pytest.raises(ValidationError):
        Project(elements=[123, OntoumlElementStub()])  # Mixing int and OntoumlElement in 'elements'

    with pytest.raises(ValidationError):
        Project(acronyms=[True, "ACR"])  # Mixing bool and str in 'acronyms'


def test_project_empty_values_post_initialization() -> None:
    """Test assigning empty values to attributes post-initialization."""
    project = Project(pref_name=create_langstring("Test"))
    project.namespace = ""
    project.license = ""
    project.publisher = ""

    assert project.namespace == "", "Should allow setting empty string for 'namespace' post-initialization."
    assert project.license == "", "Should allow setting empty string for 'license' post-initialization."
    assert project.publisher == "", "Should allow setting empty string for 'publisher' post-initialization."


def test_project_future_past_dates() -> None:
    """Test setting future and past dates for datetime attributes."""
    future_date = datetime.now() + timedelta(days=365)
    past_date = datetime.now() - timedelta(days=365)

    project = Project(created=past_date, modified=future_date)

    assert project.created == past_date, "Should handle past dates for 'created'."
    assert project.modified == future_date, "Should handle future dates for 'modified'."


def test_project_assigning_null_to_optional_fields() -> None:
    """Test assigning None to optional fields."""
    project = Project()
    project.namespace = None
    project.license = None
    project.publisher = None

    assert project.namespace is None, "Should allow assigning None to 'namespace'."
    assert project.license is None, "Should allow assigning None to 'license'."
    assert project.publisher is None, "Should allow assigning None to 'publisher'."


def test_project_datetime_boundaries() -> None:
    """Test setting the minimum and maximum datetime values."""
    min_datetime = datetime.min
    max_datetime = datetime.max

    project = Project(created=min_datetime, modified=max_datetime)

    assert project.created == min_datetime, "Should handle minimum datetime for 'created'."
    assert project.modified == max_datetime, "Should handle maximum datetime for 'modified'."


def test_project_empty_and_null_lists() -> None:
    """Test handling empty and None lists for list attributes."""
    project = Project()
    project.elements = []

    assert project.elements == [], "Should handle empty list for 'elements'."

    with pytest.raises(ValidationError):
        project.acronyms = None


def test_project_numerical_values_for_strings() -> None:
    """Test assigning numerical values to string attributes."""
    with pytest.raises(ValidationError):
        Project(namespace=123)

    with pytest.raises(ValidationError):
        Project(license=456)

    with pytest.raises(ValidationError):
        Project(publisher=789)


def test_project_boolean_values_in_lists() -> None:
    """Test assigning boolean values in list attributes."""
    with pytest.raises(ValidationError):
        Project(acronyms=[True, False])

    with pytest.raises(ValidationError):
        Project(bibliographic_citations=[True, False])

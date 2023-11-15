import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

import pytest
from langstring_lib.langstring import LangString  # type: ignore
from pydantic import ValidationError

from ontouml_py.classes.abstract_syntax.project import Project
from ontouml_py.classes.ontoumlelement import OntoumlElement


# Utility functions and fixtures
def create_langstring(text: str) -> LangString:
    """Create a LangString object from a given text.

    :param text: The text to be converted into a LangString.
    :type text: str
    :return: A LangString object containing the provided text.
    :rtype: LangString
    """
    return LangString(text)


class OntoumlElementStub(OntoumlElement):
    """A stub class for OntoumlElement.

    This class serves as a concrete subclass of OntoumlElement, primarily used for testing and demonstration purposes.
    It does not introduce additional attributes or methods beyond those inherited from OntoumlElement, and is typically
    instantiated to create simple examples of OntoumlElement objects.
    """

    def __init__(self):
        """Initialize a new instance of OntoumlElementStub.

        As a stub implementation, this constructor initializes all attributes inherited from OntoumlElement, including
        'in_project'.
        """
        super().__init__()


class AnotherOntoumlElementStub(OntoumlElement):
    """A second stub class for OntoumlElement.

    This class serves as a concrete subclass of OntoumlElement, primarily used for testing and demonstration purposes.
    It does not introduce additional attributes or methods beyond those inherited from OntoumlElement, and is typically
    instantiated to create simple examples of OntoumlElement objects.
    """

    def __init__(self):
        """Initialize a new instance of AnotherOntoumlElementStub.

        As a stub implementation, this constructor initializes all attributes inherited from OntoumlElement, including
        'in_project'.
        """
        super().__init__()


def create_ontoumlelement() -> OntoumlElementStub:
    """Create and return an instance of OntoumlElementStub.

    :return: An instance of OntoumlElementStub.
    :rtype: OntoumlElementStub
    """
    return OntoumlElementStub()


@pytest.fixture
def valid_langstring_list() -> list[LangString]:
    """Provide a fixture for creating a list of valid LangString objects.

    :return: A list of LangString objects.
    :rtype: list[LangString]
    """
    return [create_langstring("Keyword1"), create_langstring("Keyword2")]


@pytest.fixture
def valid_ontoumlelement_list() -> list[OntoumlElementStub]:
    """Provide a fixture for creating a list of valid OntoumlElementStub objects.

    :return: A list of OntoumlElementStub objects.
    :rtype: list[OntoumlElementStub]
    """
    return [OntoumlElementStub(), OntoumlElementStub()]


# Test for successful initialization of Project
def test_project_initialization(
    valid_langstring_list: list[LangString], valid_ontoumlelement_list: list[OntoumlElementStub]
) -> None:
    """Test the successful initialization of a Project instance with valid parameters.

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

    for element in valid_ontoumlelement_list:
        project.add_element(element)

    # Assertions to validate initialization
    assert project.elements == valid_ontoumlelement_list, "Project should have the correct 'elements'."
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
    """Test updating project attributes to empty values after non-empty initialization.

    :raises AssertionError: If the attributes don't update to empty values correctly.
    """
    project = Project(pref_name=create_langstring("Initial"), alt_names=[create_langstring("Alt")])
    project.pref_name = create_langstring("")
    project.alt_names = []
    assert project.pref_name.text == "" and project.alt_names == [], "Should update to empty values correctly."


def test_project_invalid_value_in_list_post_init() -> None:
    """Test assigning an invalid value in a list attribute after non-empty initialization.

    :raises ValidationError: If the list accepts an invalid value.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    with pytest.raises(ValidationError):
        project.alt_names = [create_langstring("Another"), None]  # Reassign with a new list containing an invalid value


def test_project_invalid_type_in_list_post_init() -> None:
    """Test assigning an invalid type in a list attribute after non-empty initialization.

    :raises ValidationError: If the list accepts an invalid type.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    with pytest.raises(ValidationError):
        project.alt_names = [create_langstring("Another"), 123]  # Reassign with a new list containing an invalid type


# Test for None in list after non-empty initialization
def test_project_none_in_list_post_init() -> None:
    """Test assigning None to a list attribute after non-empty initialization.

    :raises ValueError: If None is assigned to a list attribute.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    with pytest.raises(ValueError):
        project.alt_names = None


# Test for empty string in list after non-empty initialization
def test_project_empty_string_in_list_post_init() -> None:
    """Test appending an empty string to a list attribute after non-empty initialization.

    :raises AssertionError: If empty string in list is not handled correctly.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    project.alt_names.append(create_langstring(""))
    assert project.alt_names[-1].text == "", "Should handle empty string in list correctly."


# Test for updating list attribute with a mix of valid and None values
def test_project_update_list_with_mixed_values() -> None:
    """Test updating a list attribute with a mix of valid and None values.

    :raises ValidationError: If mixed values are incorrectly accepted.
    """
    project = Project(acronyms=["AC1"])
    with pytest.raises(ValidationError):
        project.acronyms = ["AC2", None]


# Test for updating list attribute with a mix of valid and invalid types
def test_project_update_list_with_mixed_types() -> None:
    """Test updating a list attribute with a mix of valid and invalid types.

    :raises ValidationError: If mixed types are incorrectly accepted.
    """
    project = Project(acronyms=["AC1"])
    with pytest.raises(ValidationError):
        project.acronyms = ["AC2", 123]


def test_project_interaction_with_langstring_complex() -> None:
    """Test Project initialization with complex LangString objects.

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
    """Test Project initialization with datetime objects in different time zones.

    :raises AssertionError: If datetime objects with different time zones are not handled correctly.
    """
    # Example using timezone aware datetime objects
    aware_datetime = datetime(2022, 1, 1, tzinfo=timezone.utc)
    project = Project(created=aware_datetime)
    assert project.created == aware_datetime, "Project should handle timezone aware datetime objects."


def test_project_extreme_values_handling() -> None:
    """Test Project handling extreme and boundary values in attributes.

    :raises AssertionError: If extreme and boundary values are not handled correctly.
    """
    very_long_string = "x" * 10000
    project = Project(namespace=very_long_string)
    assert project.namespace == very_long_string, "Project should handle very long string values."


def test_project_default_values_initialization() -> None:
    """Test initialization of Project with default values.

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

    project = Project(acronyms=large_strings, bibliographic_citations=large_strings)

    # Manually add elements using the add_element method
    for element in large_elements:
        project.add_element(element)

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
    """Test handling empty lists for list attributes."""
    project = Project()

    # Remove elements if any (though it should be initialized empty)
    for element in project.elements:
        project.remove_element(element)

    assert project.elements == [], "Elements should be an empty list after removal."

    # Testing setting to None should raise an error
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


# Test adding valid OntoumlElement to Project
def test_project_add_valid_element() -> None:
    """Test adding a valid OntoumlElement to a Project instance.

    :raises AssertionError: If the element is not added correctly to the Project.
    """
    project = Project()
    element = create_ontoumlelement()
    project.add_element(element)
    assert element in project.elements, "Valid element should be added to the Project."


# Test for adding duplicate OntoumlElement to Project
def test_project_add_duplicate_element() -> None:
    """Test adding a duplicate OntoumlElement to a Project instance.

    :raises AssertionError: If the duplicate element is added to the Project.
    """
    project = Project()
    element = create_ontoumlelement()
    project.add_element(element)
    project.add_element(element)  # Adding the same element again
    assert project.elements.count(element) == 1, "Duplicate element should not be added to the Project."


# Test for adding incorrect type to Project
def test_project_add_incorrect_type_element() -> None:
    """Test adding an element of incorrect type to a Project instance.

    :raises ValidationError: If an element of incorrect type is added to the Project.
    """
    project = Project()
    incorrect_element = "Not an OntoumlElement"
    with pytest.raises(TypeError):
        project.add_element(incorrect_element)


# Test for maintaining inverse relationship with OntoumlElement
def test_project_maintain_inverse_relationship() -> None:
    """Test maintaining the inverse relationship when adding an OntoumlElement to a Project.

    :raises AssertionError: If the inverse relationship is not maintained correctly.
    """
    project = Project()
    element = create_ontoumlelement()
    project.add_element(element)
    assert project in element.in_project, "Project should be in the 'in_project' list of the added element."


# Test adding None as an element
def test_project_add_none_element() -> None:
    """Test adding None as an element to a Project instance.

    :raises TypeError: If None is added as an element to the Project.
    """
    project = Project()
    with pytest.raises(TypeError):
        project.add_element(None)


# Test adding multiple elements
def test_project_add_multiple_elements(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test adding multiple OntoumlElement objects to a Project instance.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If the elements are not added correctly to the Project.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
    assert project.elements == valid_ontoumlelement_list, "All elements should be added to the Project."


# Test adding an element that is already part of another project
def test_project_add_element_already_in_other_project() -> None:
    """Test adding an OntoumlElement that is already part of another Project instance.

    :raises AssertionError: If the element is not added to both projects correctly.
    """
    project1 = Project()
    project2 = Project()
    element = create_ontoumlelement()
    project1.add_element(element)
    project2.add_element(element)
    assert element in project1.elements and element in project2.elements, "Element should be part of both projects."


# Test adding an element that is the project itself (should be forbidden)
def test_project_add_self_as_element() -> None:
    """Test adding the Project instance itself as an element.

    :raises TypeError: If the Project instance is added as its own element.
    """
    project = Project()
    project.add_element(project)

    assert not project.elements


# Test adding elements of different concrete subclasses of OntoumlElement
def test_project_add_various_subclasses_of_elements() -> None:
    """Test adding various concrete subclasses of OntoumlElement to a Project instance.

    :raises AssertionError: If different subclasses of elements are not added correctly.
    """
    project = Project()
    element1 = OntoumlElementStub()
    element2 = AnotherOntoumlElementStub()
    project.add_element(element1)
    project.add_element(element2)
    assert (
        element1 in project.elements and element2 in project.elements
    ), "Different subclasses of elements should be added correctly."


# Test adding elements with a mix of valid and invalid instances
def test_project_add_mixed_valid_invalid_elements() -> None:
    """Test adding a mix of valid and invalid instances to a Project instance.

    :raises ValidationError: If invalid instances are added to the Project.
    """
    project = Project()
    valid_element = create_ontoumlelement()
    invalid_element = "Invalid Element"
    with pytest.raises(TypeError):
        project.add_element(valid_element)
        project.add_element(invalid_element)


# Test adding elements where some have already been added
def test_project_add_elements_with_duplicates(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test adding elements to a Project instance where some elements have already been added.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If duplicate handling is not correct.
    """
    project = Project()
    project.add_element(valid_ontoumlelement_list[0])
    for element in valid_ontoumlelement_list:
        project.add_element(element)

    unique_elements = []
    for element in project.elements:
        if element not in unique_elements:
            unique_elements.append(element)

    assert len(project.elements) == len(unique_elements), "Duplicates should not be added."


# Test adding an element and checking if its in_project attribute is updated
def test_project_add_element_updates_in_project() -> None:
    """Test if adding an element to a Project instance updates the element's in_project attribute.

    :raises AssertionError: If the element's in_project attribute is not updated.
    """
    project = Project()
    element = create_ontoumlelement()
    project.add_element(element)
    assert project in element.in_project, "The element's in_project attribute should include this project."


# Test adding elements with custom attributes
def test_project_add_custom_attribute_elements() -> None:
    """Test adding elements with custom attributes to a Project instance.

    :raises AssertionError: If elements with custom attributes are not handled correctly.
    """

    class CustomOntoumlElement(OntoumlElement):
        custom_attr: str = "Custom Value"

        def __init__(self, **data: dict[str, Any]):
            super().__init__(**data)

    project = Project()
    custom_element = CustomOntoumlElement()
    project.add_element(custom_element)

    assert custom_element in project.elements, "Custom element should be added to the Project."
    assert custom_element.custom_attr == "Custom Value", "Custom attribute should be set correctly."


# Test adding a large number of unique elements
def test_project_add_large_number_unique_elements() -> None:
    """Test adding a large number of unique elements to a Project instance.

    :raises AssertionError: If the large number of elements are not handled correctly.
    """
    project = Project()
    for _ in range(1000):
        unique_element = OntoumlElementStub()
        project.add_element(unique_element)
    assert len(project.elements) == 1000, "A large number of unique elements should be handled correctly."


# Test removing a specific element from Project
def test_project_remove_specific_element(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing a specific element from a Project instance.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If the specific element is not removed correctly.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
    element_to_remove = valid_ontoumlelement_list[0]
    project.remove_element(element_to_remove)
    assert element_to_remove not in project.elements, "Specific element should be removed from the Project."


# Test removing an element that is part of multiple projects
def test_project_remove_element_from_multiple_projects() -> None:
    """Test removing an OntoumlElement that is part of multiple Project instances.

    :raises AssertionError: If the element is not correctly removed from one project while remaining in others.
    """
    project1 = Project()
    project2 = Project()
    element = create_ontoumlelement()
    project1.add_element(element)
    project2.add_element(element)
    project1.remove_element(element)
    assert (
        element not in project1.elements and element in project2.elements
    ), "Element should be removed only from the specified Project."


# Test removing an element that does not exist in Project
def test_project_remove_nonexistent_element() -> None:
    """Test removing an OntoumlElement that does not exist in the Project.

    :raises AssertionError: If the removal operation affects the Project incorrectly.
    """
    project = Project()
    nonexistent_element = create_ontoumlelement()
    project.remove_element(nonexistent_element)
    assert nonexistent_element not in project.elements, "Nonexistent element should not affect the Project."


# Test removing None from Project
def test_project_remove_none_element() -> None:
    """Test removing None from a Project instance.

    :raises TypeError: If None is attempted to be removed from the Project.
    """
    project = Project()
    with pytest.raises(TypeError):
        project.remove_element(None)


# Test removing all elements of a specific type from Project
def test_project_remove_all_elements_of_type() -> None:
    """Test removing all elements of a specific type from a Project instance.

    :raises AssertionError: If not all elements of the specific type are removed.
    """
    project = Project()
    for _ in range(5):
        project.add_element(OntoumlElementStub())
        project.add_element(AnotherOntoumlElementStub())
    for element in project.elements[:]:
        if isinstance(element, OntoumlElementStub):
            project.remove_element(element)
    assert all(
        not isinstance(el, OntoumlElementStub) for el in project.elements
    ), "All elements of specific type should be removed."


# Test removing an element and checking if its in_project attribute is updated
def test_project_remove_element_updates_in_project() -> None:
    """Test if removing an element from a Project instance updates the element's in_project attribute.

    :raises AssertionError: If the element's in_project attribute is not updated.
    """
    project = Project()
    element = create_ontoumlelement()
    project.add_element(element)
    project.remove_element(element)
    assert (
        project not in element.in_project
    ), "The element's in_project attribute should not include this project after removal."


# Test removing elements added via a list
def test_project_remove_elements_added_via_list(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing elements from a Project instance that were added via a list.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If elements are not removed correctly.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
    for element in valid_ontoumlelement_list:
        project.remove_element(element)
    assert not project.elements, "All elements added via a list should be removed."


# Test removing an element and checking other elements remain
def test_project_remove_element_check_others_remain() -> None:
    """Test removing a specific element from a Project and checking that other elements remain.

    :raises AssertionError: If other elements are affected by the removal of one.
    """
    project = Project()
    element_to_remove = create_ontoumlelement()
    other_element = create_ontoumlelement()
    project.add_element(element_to_remove)
    project.add_element(other_element)
    project.remove_element(element_to_remove)
    assert other_element in project.elements, "Other elements should remain after removing a specific element."


# Test removing multiple different elements from Project
def test_project_remove_multiple_different_elements(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing multiple different elements from a Project instance.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If the elements are not removed correctly.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
    for element in valid_ontoumlelement_list[::2]:  # Remove every other element
        project.remove_element(element)
    expected_remaining = valid_ontoumlelement_list[1::2]
    assert all(
        el in project.elements for el in expected_remaining
    ), "Multiple different elements should be removed correctly."


# Test removing an element with custom attributes from Project
def test_project_remove_custom_attribute_element() -> None:
    """Test removing an element with custom attributes from a Project instance.

    :raises AssertionError: If the element with custom attributes is not removed correctly.
    """

    class CustomOntoumlElement(OntoumlElement):
        custom_attr: str = "Custom Value"

        def __init__(self, **data: dict[str, Any]):
            super().__init__(**data)

    project = Project()
    custom_element = CustomOntoumlElement()
    project.add_element(custom_element)
    project.remove_element(custom_element)
    assert custom_element not in project.elements, "Custom element should be removed from the Project."


# Test removing elements after modifying them
def test_project_remove_modified_elements(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing elements from a Project after they have been modified.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If modified elements are not removed correctly.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
        element.modified = datetime.now()  # Modify the element
    for element in valid_ontoumlelement_list:
        project.remove_element(element)
    assert not project.elements, "Modified elements should be removed correctly."


# Test removing elements in reverse order of addition
def test_project_remove_elements_in_reverse_order(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing elements from a Project in the reverse order of their addition.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If elements are not removed correctly in reverse order.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
    for element in reversed(valid_ontoumlelement_list):
        project.remove_element(element)
    assert not project.elements, "Elements should be removed correctly in reverse order."


# Test removing elements that are part of nested projects
def test_project_remove_elements_nested_projects() -> None:
    """Test removing elements from a Project where elements are part of nested projects.

    :raises AssertionError: If nested elements are not handled correctly during removal.
    """
    parent_project = Project()
    child_project = Project()
    element = create_ontoumlelement()
    parent_project.add_element(child_project)
    child_project.add_element(element)
    parent_project.remove_element(child_project)
    assert child_project not in parent_project.elements, "Nested project should be removed from the parent project."
    assert (
        element in child_project.elements
    ), "Elements in the nested project should remain after removal from the parent project."


# Test repeatedly adding and removing the same element
def test_project_repeated_add_remove_element() -> None:
    """Test repeatedly adding and removing the same OntoumlElement to/from a Project.

    :raises AssertionError: If the element is not handled correctly during repeated add/remove operations.
    """
    project = Project()
    element = create_ontoumlelement()
    for _ in range(5):
        project.add_element(element)
        project.remove_element(element)
    assert element not in project.elements, "Element should be correctly handled during repeated add/remove operations."


# Test removing elements using a conditional filter
def test_project_remove_elements_conditional_filter(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing elements from a Project using a conditional filter.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If elements are not correctly removed based on a conditional filter.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        element_id_as_int = int(uuid.UUID(element.id))
        element.modified = datetime.now() if element_id_as_int % 2 == 0 else None
        project.add_element(element)
    for element in project.elements[:]:
        if element.modified is not None:
            project.remove_element(element)
    assert all(
        element.modified is None for element in project.elements
    ), "Elements should be removed based on the conditional filter."


# Test removing elements and checking the project's elements count
def test_project_remove_elements_check_count(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing elements from a Project and checking the project's elements count.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If the project's elements count is not updated correctly.
    """
    project = Project()
    initial_count = 0
    for element in valid_ontoumlelement_list:
        project.add_element(element)
        initial_count += 1
    for element in valid_ontoumlelement_list:
        project.remove_element(element)
        initial_count -= 1
        assert (
            len(project.elements) == initial_count
        ), "Project's elements count should be updated correctly after each removal."


# Test removing a random selection of elements from Project
def test_project_remove_random_elements(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing a random selection of elements from a Project instance.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If random elements are not removed correctly.
    """
    import random

    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
    random_elements = random.sample(valid_ontoumlelement_list, len(valid_ontoumlelement_list) // 2)
    for element in random_elements:
        project.remove_element(element)
    assert all(
        element not in project.elements for element in random_elements
    ), "Randomly selected elements should be removed correctly."


# Test removing all elements and checking project's empty state
def test_project_remove_all_elements_empty_state(valid_ontoumlelement_list: list[OntoumlElementStub]) -> None:
    """Test removing all elements from a Project and checking if the project is empty.

    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects for testing.
    :type valid_ontoumlelement_list: list[OntoumlElementStub]
    :raises AssertionError: If the project is not empty after removing all elements.
    """
    project = Project()
    for element in valid_ontoumlelement_list:
        project.add_element(element)
    for element in valid_ontoumlelement_list:
        project.remove_element(element)
    assert not project.elements, "Project should be empty after removing all elements."


# Test removing an element that does not belong to the project
def test_project_remove_nonexistent_element2() -> None:
    """Test removing an element that does not belong to the Project instance.

    :raises AssertionError: If removing a nonexistent element affects the project's elements.
    """
    project = Project()
    nonexistent_element = create_ontoumlelement()
    initial_elements = project.elements.copy()
    project.remove_element(nonexistent_element)
    assert (
        project.elements == initial_elements
    ), "Removing a nonexistent element should not affect the project's elements."


# Test removing an element and ensuring other elements remain unchanged
def test_project_remove_element_others_unchanged() -> None:
    """Test removing a single element from a Project and ensuring other elements remain unchanged.

    :raises AssertionError: If other elements are affected by the removal.
    """
    project = Project()
    elements = [create_ontoumlelement() for _ in range(5)]
    for element in elements:
        project.add_element(element)
    element_to_remove = elements[2]
    project.remove_element(element_to_remove)
    assert element_to_remove not in project.elements, "Removed element should not be in the project."
    assert all(
        el in project.elements for el in elements if el != element_to_remove
    ), "Other elements should remain unchanged."


# Test removing an element by modifying its properties before removal
def test_project_remove_modified_element() -> None:
    """Test removing an element from a Project after modifying its properties.

    :raises AssertionError: If the modified element is not removed correctly.
    """
    project = Project()
    element = create_ontoumlelement()
    project.add_element(element)
    # Modify an existing attribute instead of 'custom_property'
    element.modified = datetime.now()  # Assuming 'modified' is an existing attribute
    project.remove_element(element)
    assert element not in project.elements, "Modified element should be removed from the project."


# Test removing elements from a Project using a filter function
def test_project_remove_elements_by_filter() -> None:
    """Test removing elements from a Project using a filter function.

    :raises AssertionError: If elements are not removed according to the filter function.
    """
    project = Project()
    for i in range(10):
        element = create_ontoumlelement()
        # Assuming 'modified' is an existing attribute, update it with a datetime
        element.modified = datetime(2099, 1, 1, i)  # Example modification
        project.add_element(element)

    # Use a filter function based on the 'modified' attribute
    filter_function = lambda el: el.modified.hour < 5  # noqa:E731 (flake8)
    for element in project.elements[:]:
        if filter_function(element):
            project.remove_element(element)

    assert all(
        filter_function(el) is False for el in project.elements
    ), "Elements should be removed according to the filter function."


# Test removing elements sequentially from a Project
def test_project_sequential_remove_elements() -> None:
    """Test removing elements from a Project sequentially.

    :raises AssertionError: If elements are not removed correctly when done sequentially.
    """
    project = Project()
    elements = [create_ontoumlelement() for _ in range(5)]
    for element in elements:
        project.add_element(element)
    for element in elements:
        project.remove_element(element)
        assert element not in project.elements, "Element should be removed sequentially from the project."


# Test removing an element and ensuring project properties are unaffected
def test_project_remove_element_unaffected_properties() -> None:
    """Test removing an element from a Project and ensuring project properties remain unaffected.

    :raises AssertionError: If project properties are affected by the element removal.
    """
    project = Project(pref_name=create_langstring("Test Project"))
    element = create_ontoumlelement()
    project.add_element(element)
    project.remove_element(element)
    assert (
        project.pref_name.text == "Test Project"
    ), "Project properties should remain unaffected after element removal."


# Test removing elements and checking for empty state after each removal
def test_project_remove_elements_check_empty_each_time() -> None:
    """Test removing elements from a Project and checking for an empty state after each removal.

    :raises AssertionError: If the project is not empty when expected.
    """
    project = Project()
    elements = [create_ontoumlelement() for _ in range(3)]
    for element in elements:
        project.add_element(element)
    while elements:
        element = elements.pop()
        project.remove_element(element)
        if elements:
            assert project.elements, "Project should not be empty until the last element is removed."
        else:
            assert not project.elements, "Project should be empty after the last element is removed."


# Test removing elements and checking their in_project attribute
def test_project_remove_elements_check_in_project() -> None:
    """Test removing elements from a Project and checking their in_project attribute.

    :raises AssertionError: If in_project attribute of elements is not updated correctly.
    """
    project = Project()
    elements = [create_ontoumlelement() for _ in range(3)]
    for element in elements:
        project.add_element(element)
    for element in elements:
        project.remove_element(element)
        assert (
            project not in element.in_project
        ), "Removed element's in_project attribute should not include the project."


# Test removing an element and ensuring the order of remaining elements
def test_project_remove_element_ensure_order() -> None:
    """Test removing an element from a Project and ensuring the order of remaining elements.

    :raises AssertionError: If the order of remaining elements is not as expected.
    """
    project = Project()
    elements = [create_ontoumlelement() for _ in range(5)]
    for element in elements:
        project.add_element(element)
    project.remove_element(elements[2])
    expected_order = elements[:2] + elements[3:]
    assert project.elements == expected_order, "Order of remaining elements should be maintained after removal."


# Test removing a randomly chosen element from a Project
def test_project_remove_random_element() -> None:
    """Test removing a randomly chosen element from a Project.

    :raises AssertionError: If the randomly chosen element is not removed correctly.
    """
    import random

    project = Project()
    elements = [create_ontoumlelement() for _ in range(10)]
    for element in elements:
        project.add_element(element)
    random_element = random.choice(elements)
    project.remove_element(random_element)
    assert random_element not in project.elements, "Randomly chosen element should be removed from the project."


# Test removing elements and checking impact on other project properties
def test_project_remove_elements_impact_on_properties() -> None:
    """Test removing elements from a Project and checking the impact on other project properties.

    :raises AssertionError: If other project properties are affected by element removal.
    """
    project = Project(namespace="http://example.org/ns")
    elements = [create_ontoumlelement() for _ in range(3)]
    for element in elements:
        project.add_element(element)
    for element in elements:
        project.remove_element(element)
    assert (
        project.namespace == "http://example.org/ns"
    ), "Project namespace should remain unchanged after element removal."

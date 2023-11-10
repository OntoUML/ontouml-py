from datetime import datetime

import pytest
from langstring_lib.langstring import LangString

from ontouml_py.classes.abstract_syntax.project import Project
from ontouml_py.classes.ontoumlelement import OntoumlElement


# Utility function to create a LangString object
def create_langstring(text: str) -> LangString:
    return LangString(text)


class OntoumlElementStub(OntoumlElement):
    def __init__(self):
        # Implement abstract methods or set properties required by the OntoumlElement class.
        pass


def create_ontoumlelement() -> OntoumlElementStub:
    """Create and return an instance of OntoumlElementStub."""
    return OntoumlElementStub()


@pytest.fixture
def valid_langstring_list() -> list[LangString]:
    """Provide a list of valid LangString objects for testing."""
    return [create_langstring("Keyword1"), create_langstring("Keyword2")]


@pytest.fixture
def valid_ontoumlelement_list() -> list[OntoumlElementStub]:
    """Provide a list of valid OntoumlElementStub objects for testing."""
    return [OntoumlElementStub(), OntoumlElementStub()]


def test_project_initialization(
    valid_langstring_list: list[LangString], valid_ontoumlelement_list: list[OntoumlElementStub]
) -> None:
    """Test the successful initialization of a Project instance.

    :param valid_langstring_list: A list of LangString objects to be used for 'keywords' and 'editorial_notes'.
    :param valid_ontoumlelement_list: A list of OntoumlElementStub objects to be used for 'elements'.
    """
    current_time = datetime.now()
    project = Project(
        created=current_time,
        modified=current_time,
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

    assert project.created == current_time, "Project should have the correct 'created' datetime."
    assert project.modified == current_time, "Project should have the correct 'modified' datetime."
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


def test_project_initialization_with_invalid_types() -> None:
    """Test the initialization of Project with invalid types to ensure it raises TypeErrors."""
    with pytest.raises(TypeError):
        Project(pref_name="Not a LangString")  # Invalid type for 'pref_name'

    with pytest.raises(TypeError):
        Project(alt_names=["Not a LangString"])  # Invalid type inside 'alt_names' list

    with pytest.raises(TypeError):
        Project(elements=["Not an OntoumlElement"])  # Invalid type inside 'elements' list


# Test that missing optional parameters are handled correctly
def test_project_optional_params_handling() -> None:
    """Test that optional parameters are correctly defaulted to None when not provided."""
    project = Project(pref_name=create_langstring("Optional Params Test"))

    assert project.modified is None, "Optional 'modified' attribute should default to None."
    assert project.alt_names is None, "Optional 'alt_names' attribute should default to None."
    assert project.description is None, "Optional 'description' attribute should default to None."
    assert project.editorial_notes is None, "Optional 'editorial_notes' attribute should default to None."
    assert project.creators is None, "Optional 'creators' attribute should default to None."
    assert project.contributors is None, "Optional 'contributors' attribute should default to None."
    assert project.elements is None, "Optional 'elements' attribute should default to None."
    assert project.acronyms is None, "Optional 'acronyms' attribute should default to None."
    assert (
        project.bibliographic_citations is None
    ), "Optional 'bibliographic_citations' attribute should default to None."
    assert project.keywords is None, "Optional 'keywords' attribute should default to None."
    assert project.landing_pages is None, "Optional 'landing_pages' attribute should default to None."
    assert project.languages is None, "Optional 'languages' attribute should default to None."
    assert project.namespace is None, "Optional 'namespace' attribute should default to None."
    assert project.sources is None, "Optional 'sources' attribute should default to None."
    assert project.access_rights is None, "Optional 'access_rights' attribute should default to None."
    assert project.ontology_types is None, "Optional 'ontology_types' attribute should default to None."
    assert project.themes is None, "Optional 'themes' attribute should default to None."
    assert project.license is None, "Optional 'license' attribute should default to None."
    assert project.contexts is None, "Optional 'contexts' attribute should default to None."
    assert project.designed_for_task is None, "Optional 'designed_for_task' attribute should default to None."
    assert project.publisher is None, "Optional 'publisher' attribute should default to None."


# Test that the class correctly handles empty lists for list attributes
def test_project_empty_lists_handling() -> None:
    """Test that attributes which are lists can be set to empty lists without error."""
    project = Project(
        pref_name=create_langstring("Empty Lists Test"),
        alt_names=[],
        editorial_notes=[],
        creators=[],
        contributors=[],
        elements=[],
        acronyms=[],
        bibliographic_citations=[],
        keywords=[],
        landing_pages=[],
        languages=[],
        sources=[],
        access_rights=[],
        ontology_types=[],
        themes=[],
        contexts=[],
        designed_for_task=[],
    )

    assert project.alt_names == [], "Attribute 'alt_names' should handle being set to an empty list."
    assert project.editorial_notes == [], "Attribute 'editorial_notes' should handle being set to an empty list."
    assert project.creators == [], "Attribute 'creators' should handle being set to an empty list."
    assert project.contributors == [], "Attribute 'contributors' should handle being set to an empty list."
    assert project.elements == [], "Attribute 'elements' should handle being set to an empty list."
    assert project.acronyms == [], "Attribute 'acronyms' should handle being set to an empty list."
    assert (
        project.bibliographic_citations == []
    ), "Attribute 'bibliographic_citations' should handle being set to an empty list."
    assert project.keywords == [], "Attribute 'keywords' should handle being set to an empty list."
    assert project.landing_pages == [], "Attribute 'landing_pages' should handle being set to an empty list."
    assert project.languages == [], "Attribute 'languages' should handle being set to an empty list."
    assert project.sources == [], "Attribute 'sources' should handle being set to an empty list."
    assert project.access_rights == [], "Attribute 'access_rights' should handle being set to an empty list."
    assert project.ontology_types == [], "Attribute 'ontology_types' should handle being set to an empty list."
    assert project.themes == [], "Attribute 'themes' should handle being set to an empty list."
    assert project.contexts == [], "Attribute 'contexts' should handle being set to an empty list."
    assert project.designed_for_task == [], "Attribute 'designed_for_task' should handle being set to an empty list."


# Test setting and retrieving non-list attributes
def test_project_non_list_attributes() -> None:
    """Test setting and retrieving non-list attributes such as strings and LangString objects."""
    pref_name = create_langstring("Project Name")
    description = create_langstring("A project description")
    namespace = "http://example.com/ns"
    license = "CC BY 4.0"
    publisher = "Example Publisher"

    project = Project(
        pref_name=pref_name, description=description, namespace=namespace, license=license, publisher=publisher
    )

    assert project.pref_name == pref_name, "The 'pref_name' should be set and retrieved correctly."
    assert project.description == description, "The 'description' should be set and retrieved correctly."
    assert project.namespace == namespace, "The 'namespace' should be set and retrieved correctly."
    assert project.license == license, "The 'license' should be set and retrieved correctly."
    assert project.publisher == publisher, "The 'publisher' should be set and retrieved correctly."


# Test that incorrect types for non-list attributes raise TypeErrors
def test_project_non_list_attributes_type_errors() -> None:
    """Test that providing incorrect types for non-list attributes raises TypeErrors."""
    with pytest.raises(TypeError):
        Project(namespace=123)  # namespace should be a string

    with pytest.raises(TypeError):
        Project(license=LangString("CC BY 4.0"))  # license should be a string

    with pytest.raises(TypeError):
        Project(publisher=5.5)  # publisher should be a string


# Ensure datetime attributes are handled correctly
def test_project_datetime_attributes() -> None:
    """Test that datetime attributes are set correctly and handle None as a default value."""
    created_time = datetime(2022, 1, 1, 12, 0)
    modified_time = datetime(2022, 1, 2, 12, 0)

    project = Project(created=created_time, modified=modified_time)

    assert project.created == created_time, "The 'created' datetime should be set correctly."
    assert project.modified == modified_time, "The 'modified' datetime should be set correctly."

    project = Project()
    assert isinstance(project.created, datetime), "The 'created' datetime should be automatically set if not provided."


# Test that providing None for optional list attributes does not raise errors
def test_project_none_for_optional_list_attributes() -> None:
    """Test that providing None for optional list attributes sets them to None without error."""
    project = Project(
        pref_name=create_langstring("Test None Lists"),
        alt_names=None,
        editorial_notes=None,
        creators=None,
        contributors=None,
        elements=None,
        acronyms=None,
        bibliographic_citations=None,
        keywords=None,
        landing_pages=None,
        languages=None,
        sources=None,
        access_rights=None,
        ontology_types=None,
        themes=None,
        contexts=None,
        designed_for_task=None,
    )

    assert project.alt_names is None, "Optional list attribute 'alt_names' should accept None."
    assert project.editorial_notes is None, "Optional list attribute 'editorial_notes' should accept None."
    assert project.creators is None, "Optional list attribute 'creators' should accept None."
    assert project.contributors is None, "Optional list attribute 'contributors' should accept None."
    assert project.elements is None, "Optional list attribute 'elements' should accept None."
    assert project.acronyms is None, "Optional list attribute 'acronyms' should accept None."
    assert (
        project.bibliographic_citations is None
    ), "Optional list attribute 'bibliographic_citations' should accept None."
    assert project.keywords is None, "Optional list attribute 'keywords' should accept None."
    assert project.landing_pages is None, "Optional list attribute 'landing_pages' should accept None."
    assert project.languages is None, "Optional list attribute 'languages' should accept None."
    assert project.sources is None, "Optional list attribute 'sources' should accept None."
    assert project.access_rights is None, "Optional list attribute 'access_rights' should accept None."
    assert project.ontology_types is None, "Optional list attribute 'ontology_types' should accept None."
    assert project.themes is None, "Optional list attribute 'themes' should accept None."
    assert project.contexts is None, "Optional list attribute 'contexts' should accept None."
    assert project.designed_for_task is None, "Optional list attribute 'designed_for_task' should accept None."


# Test handling of empty strings for attributes that are strings
def test_project_empty_strings_for_string_attributes() -> None:
    """Test that providing empty strings for string attributes does not raise errors."""
    project = Project(pref_name=create_langstring("Test Empty Strings"), namespace="", license="", publisher="")
    assert project.namespace == "", "String attribute 'namespace' should accept an empty string."
    assert project.license == "", "String attribute 'license' should accept an empty string."
    assert project.publisher == "", "String attribute 'publisher' should accept an empty string."


# Test that providing invalid values for string attributes raises TypeErrors
def test_project_invalid_values_for_string_attributes() -> None:
    """Test that providing invalid values for string attributes raises TypeErrors."""
    with pytest.raises(TypeError):
        Project(namespace=123)  # Invalid type, expecting a string

    with pytest.raises(TypeError):
        Project(license=LangString("Invalid"))  # Invalid type, expecting a string

    with pytest.raises(TypeError):
        Project(publisher=True)  # Invalid type, expecting a string


# Test that providing None for optional attributes does not raise errors
def test_project_none_for_optional_attributes() -> None:
    """Test that providing None for optional attributes sets them correctly without error."""
    project = Project(pref_name=None)  # Assuming pref_name is optional and can be None
    assert project.pref_name is None, "Optional attribute 'pref_name' should accept None."


# Test providing invalid non-None values for optional attributes
def test_project_invalid_non_none_values_for_optional_attributes() -> None:
    """Test that providing invalid non-None values for optional attributes raises TypeErrors."""
    with pytest.raises(TypeError):
        Project(pref_name=123)  # Invalid type, expecting LangString or None

    with pytest.raises(TypeError):
        Project(namespace=5.5)  # Invalid type, expecting a string or None

    with pytest.raises(TypeError):
        Project(license=False)  # Invalid type, expecting a string or None


# Test providing invalid values for list attributes
def test_project_invalid_values_for_list_attributes() -> None:
    """Test that providing invalid values for list attributes raises TypeErrors."""
    with pytest.raises(TypeError):
        Project(alt_names="Not a list")  # Invalid type, expecting a list of LangString or None

    with pytest.raises(TypeError):
        Project(elements="Not a list")  # Invalid type, expecting a list of OntoumlElement or None

    with pytest.raises(TypeError):
        Project(editorial_notes=[123])  # Invalid type inside list, expecting a list of LangString


# Test providing mixed valid and invalid values in list attributes
def test_project_mixed_values_in_list_attributes() -> None:
    """Test that providing mixed valid and invalid values in list attributes raises TypeErrors."""
    with pytest.raises(TypeError):
        Project(editorial_notes=[create_langstring("Valid"), 123])  # Mixed types inside 'editorial_notes' list

    with pytest.raises(TypeError):
        Project(creators=["http://validcreator.com", 456])  # Mixed types inside 'creators' list


# Test edge cases for string attributes like very long strings or unusual characters
def test_project_string_attributes_edge_cases() -> None:
    """Test edge cases for string attributes such as extremely long strings or strings with unusual characters."""
    very_long_string = "x" * 10000
    unusual_chars_string = "\t\n\r\x0b\x0c"

    project = Project(namespace=very_long_string, license=unusual_chars_string, publisher=very_long_string)

    assert project.namespace == very_long_string, "String attribute 'namespace' should handle very long strings."
    assert project.license == unusual_chars_string, "String attribute 'license' should handle unusual characters."
    assert project.publisher == very_long_string, "String attribute 'publisher' should handle very long strings."


# Test edge cases for datetime attributes like minimum and maximum possible dates
def test_project_datetime_attributes_edge_cases() -> None:
    """Test edge cases for datetime attributes such as minimum and maximum possible dates."""
    min_datetime = datetime.min
    max_datetime = datetime.max

    project = Project(created=min_datetime, modified=max_datetime)

    assert project.created == min_datetime, "Datetime attribute 'created' should handle minimum datetime."
    assert project.modified == max_datetime, "Datetime attribute 'modified' should handle maximum datetime."


# Test edge cases for list attributes like very large lists or lists with mixed types
def test_project_list_attributes_edge_cases() -> None:
    """Test edge cases for list attributes such as very large lists or lists with mixed types."""
    large_list = [create_langstring(f"Keyword{i}") for i in range(1000)]  # Large list of LangString objects
    mixed_types_list = [create_langstring("Valid"), "Invalid", 123]

    with pytest.raises(TypeError):
        Project(keywords=large_list, editorial_notes=mixed_types_list)  # Mixed types, should raise TypeError

    project = Project(keywords=large_list)
    assert project.keywords == large_list, "List attribute 'keywords' should handle very large lists."


# Test handling of None in list attributes for scenarios where None might represent a lack of value
def test_project_none_in_list_attributes_edge_cases() -> None:
    """Test handling of None in list attributes for scenarios where None might represent a lack of value."""
    list_with_none = [None, create_langstring("Valid")]

    with pytest.raises(TypeError):
        Project(keywords=list_with_none)  # List containing None, should raise TypeError


# More edge case tests can be added to cover additional scenarios specific to the Project class.


# Test edge cases for string attributes that are URIs or supposed to follow a specific format
def test_project_string_format_edge_cases() -> None:
    """Test edge cases for string attributes that should follow specific formats, like URIs."""
    # These are not valid URIs but are being used to test the system's robustness against incorrect formats
    invalid_uri = "invalid_uri"
    project = Project(
        pref_name=create_langstring("Test String Formats"),
        creators=[invalid_uri],
        contributors=[invalid_uri],
        landing_pages=[invalid_uri],
        sources=[invalid_uri],
    )
    # Assert that the class can handle incorrect formats; this may vary depending on class constraints
    assert project.creators[0] == invalid_uri, "String URI attribute 'creators' should accept any string."
    assert project.contributors[0] == invalid_uri, "String URI attribute 'contributors' should accept any string."
    assert project.landing_pages[0] == invalid_uri, "String URI attribute 'landing_pages' should accept any string."
    assert project.sources[0] == invalid_uri, "String URI attribute 'sources' should accept any string."


# Test the resilience of the class against attributes with unexpected data types
def test_project_unexpected_data_types_handling() -> None:
    """Test the resilience of the class against attributes with unexpected data types."""
    # Passing an integer where a list is expected
    with pytest.raises(TypeError):
        Project(elements=123)

    # Passing a dictionary where a string is expected
    with pytest.raises(TypeError):
        Project(namespace={"invalid": "type"})

    # Passing a list where a LangString is expected
    with pytest.raises(TypeError):
        Project(pref_name=["Not", "LangString"])


def test_project_mixed_none_and_valid_values_handling() -> None:
    """Test that providing a list with mixed None and valid string values for list attributes raises TypeError."""
    with pytest.raises(TypeError, match="All elements in 'contributors' must be of type str."):
        Project(
            pref_name=create_langstring("Test Mixed None"),
            contributors=[None, "http://validcontributor.com"],  # This should raise a TypeError
        )


# Test the class's ability to handle exceptionally large values for string-type attributes
def test_project_large_string_values_handling() -> None:
    """Test the class's ability to handle exceptionally large values for string-type attributes."""
    large_string = "a" * int(1e6)  # 1 million characters
    project = Project(
        pref_name=create_langstring("Test Large String"),
        namespace=large_string,
        license=large_string,
        publisher=large_string,
    )
    assert project.namespace == large_string, "String attribute 'namespace' should handle large string values."
    assert project.license == large_string, "String attribute 'license' should handle large string values."
    assert project.publisher == large_string, "String attribute 'publisher' should handle large string values."

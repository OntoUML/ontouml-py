from datetime import datetime, timezone, timedelta

import pytest
from langstring import LangString
from pydantic import ValidationError

from ontouml_py.classes.abstract_classes.modelelement import ModelElement
from ontouml_py.classes.concrete_classes.project import Project
from ontouml_py.classes.enumerations.ontologyrepresentationstyle import OntologyRepresentationStyle


def create_langstring(text: str) -> LangString:
    """Create a LangString object from a given text.

    :param text: The text to be converted into a LangString.
    :type text: str
    :return: A LangString object containing the provided text.
    :rtype: LangString
    """
    return LangString(text)


class Package(ModelElement):
    """A stub class for OntoumlElement.

    This class serves as a concrete subclass of OntoumlElement, primarily used for testing and demonstration purposes.
    It does not introduce additional attributes or methods beyond those inherited from OntoumlElement, and is typically
    instantiated to create simple examples of OntoumlElement objects.
    """

    def __init__(self):
        """Initialize a new instance of Package.

        As a stub implementation, this constructor initializes all attributes inherited from OntoumlElement, including
        'in_project'.
        """
        super().__init__()


@pytest.fixture
def valid_langstring_set() -> set[LangString]:
    """Provide a fixture for creating a list of valid LangString objects.

    :return: A list of LangString objects.
    :rtype: list[LangString]
    """
    return set([create_langstring("Keyword1"), create_langstring("Keyword2")])


def test_project_string_attributes(valid_langstring_set) -> None:
    """Test the initialization of Project's string type attributes.

    :param valid_langstring_list: A list of LangString objects for testing.
    :type valid_langstring_list: list[LangString]
    """
    project = Project(
        names={create_langstring("Project Name")},
        alt_names=valid_langstring_set,
        description=create_langstring("Project Description"),
        editorial_notes=valid_langstring_set,
        creators={"http://creator1.com"},
        contributors={"http://contributor1.com"},
        acronyms={"P1"},
        bibliographic_citations={"Citation1"},
        keywords={"asd"},
        landing_pages={"http://landingpage1.com"},
        languages={"en"},
        namespace="http://example.org/ns",
        sources={"http://source1.com"},
        access_rights={"Public"},
        ontology_types={"Formal"},
        themes={"Theme1"},
        license="CC BY 4.0",
        contexts={"Context1"},
        designed_for_task={"Task1"},
        publisher="Publisher Name",
        representation_style=OntologyRepresentationStyle.ONTOUML_STYLE,
    )

    assert project.namespace == "http://example.org/ns", "Project should have the correct 'namespace'."
    assert project.license == "CC BY 4.0", "Project should have the correct 'license'."
    assert project.publisher == "Publisher Name", "Project should have the correct 'publisher'."


def test_project_langstring_attributes(valid_langstring_set) -> None:
    """Test the initialization of Project's LangString type attributes.

    :param valid_langstring_list: A list of LangString objects for testing.
    :type valid_langstring_list: list[LangString]
    """
    valid_names = {create_langstring("Project Name")}
    project = Project(
        names=valid_names,
        alt_names=valid_langstring_set,
        description=create_langstring("Project Description"),
        editorial_notes=valid_langstring_set,
        creators={"http://creator1.com"},
        contributors={"http://contributor1.com"},
        acronyms={"P1"},
        bibliographic_citations={"Citation1"},
        keywords={"asd"},
        landing_pages={"http://landingpage1.com"},
        languages={"en"},
        namespace="http://example.org/ns",
        sources={"http://source1.com"},
        access_rights={"Public"},
        ontology_types={"Formal"},
        themes={"Theme1"},
        license="CC BY 4.0",
        contexts={"Context1"},
        designed_for_task={"Task1"},
        publisher="Publisher Name",
        representation_style=OntologyRepresentationStyle.ONTOUML_STYLE,
    )

    assert project.names == valid_names, "Project should have the correct 'names'."
    assert project.alt_names == valid_langstring_set, "Project should have the correct 'alt_names'."
    assert project.description.text == "Project Description", "Project should have the correct 'description'."
    assert project.editorial_notes == valid_langstring_set, "Project should have the correct 'editorial_notes'."
    assert project.keywords == {"asd"}, "Project should have the correct 'keywords'."


def test_project_list_attributes(valid_langstring_set) -> None:
    """Test the initialization of Project's list type attributes.

    :param valid_langstring_list: A list of LangString objects for testing.
    :type valid_langstring_list: list[LangString]
    """
    project = Project(
        names={create_langstring("Project Name")},
        alt_names=valid_langstring_set,
        description=create_langstring("Project Description"),
        editorial_notes=valid_langstring_set,
        creators={"http://creator1.com"},
        contributors={"http://contributor1.com"},
        acronyms={"P1"},
        bibliographic_citations={"Citation1"},
        keywords={"asd"},
        landing_pages={"http://landingpage1.com"},
        languages={"en"},
        namespace="http://example.org/ns",
        sources={"http://source1.com"},
        access_rights={"Public"},
        ontology_types={"Formal"},
        themes={"Theme1"},
        license="CC BY 4.0",
        contexts={"Context1"},
        designed_for_task={"Task1"},
        publisher="Publisher Name",
        representation_style=OntologyRepresentationStyle.ONTOUML_STYLE,
    )

    assert project


def test_project_mutable_update_empty_values() -> None:
    """Test updating project attributes to empty values after non-empty initialization.

    :raises AssertionError: If the attributes don't update to empty values correctly.
    """
    project = Project(
        names=set([create_langstring("Initial1"), create_langstring("Initial2")]),
        alt_names=set([create_langstring("Alt1"), create_langstring("Alt2")]),
    )
    ls1 = {create_langstring("a")}
    ls2 = {create_langstring("b")}
    project.names = ls1
    project.alt_names = ls2
    assert project.names == ls1 and project.alt_names == ls2, "Should update to empty values correctly."


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


def test_project_none_in_list_post_init() -> None:
    """Test assigning None to a list attribute after non-empty initialization.

    :raises ValueError: If None is assigned to a list attribute.
    """
    project = Project(alt_names=[create_langstring("Initial")])
    with pytest.raises(ValueError):
        project.alt_names = None


def test_project_add_empty_string_to_set_post_init() -> None:
    """Test adding an empty string to a set attribute after non-empty initialization.

    This test ensures that the set attribute can handle the addition of an empty string
    after being initialized with a non-empty value.

    :raises AssertionError: If the set does not correctly handle the addition of an empty string.
    """
    project = Project(alt_names={create_langstring("Initial")})
    empty = create_langstring("")
    project.alt_names.add(empty)
    assert empty in project.alt_names, "Set should correctly handle the addition of an empty string."


def test_project_update_set_with_mixed_values() -> None:
    """Test updating a set attribute with a mix of valid and None values.

    This test checks if the set attribute correctly rejects the addition of None values
    when it's updated with a mix of valid strings and None.

    :raises ValidationError: If the set incorrectly accepts None values.
    """
    project = Project(acronyms={"AC1"})
    with pytest.raises(ValidationError):
        project.acronyms = {"AC2", None}


def test_project_update_set_with_mixed_types() -> None:
    """Test updating a set attribute with a mix of valid and invalid types.

    This test verifies if the set attribute correctly rejects the addition of elements
    of incorrect types (e.g., integers) when updated with a mix of valid strings and other types.

    :raises ValidationError: If the set incorrectly accepts elements of invalid types.
    """
    project = Project(acronyms={"AC1"})
    with pytest.raises(ValidationError):
        project.acronyms = {"AC2", 123}


def test_project_interaction_with_langstring_complex() -> None:
    """Test Project initialization with complex LangString objects.

    This test ensures that the Project class can handle initialization with complex LangString objects,
    correctly storing and retrieving their properties.

    :raises AssertionError: If complex LangString objects are not handled correctly.
    """
    langstring_en = LangString("Complex Name", "en")
    langstring_pt = LangString("Nome Complexo", "pt")

    project = Project(names={langstring_en, langstring_pt})

    assert langstring_en in project.names, "English LangString should be correctly set in the set."
    assert langstring_pt in project.names, "Portuguese LangString should be correctly set in the set."


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

    This test verifies that all attributes of the Project class are correctly initialized to their default values,
    which are typically empty sets or None, as appropriate.

    :raises AssertionError: If default values are not set correctly.
    """
    project = Project()
    assert isinstance(project.elements, set), "Elements should default to an empty set."
    assert isinstance(project.acronyms, set), "Acronyms should default to an empty set."
    assert isinstance(project.bibliographic_citations, set), "Bibliographic citations should default to an empty set."
    assert isinstance(project.keywords, set), "Keywords should default to an empty set."
    assert isinstance(project.landing_pages, set), "Landing pages should default to an empty set."
    assert isinstance(project.languages, set), "Languages should default to an empty set."
    assert project.namespace is None, "Namespace should default to None."
    assert isinstance(project.sources, set), "Sources should default to an empty set."
    assert isinstance(project.access_rights, set), "Access rights should default to an empty set."
    assert isinstance(project.ontology_types, set), "Ontology types should default to an empty set."
    assert isinstance(project.themes, set), "Themes should default to an empty set."
    assert project.license is None, "License should default to None."
    assert isinstance(project.contexts, set), "Contexts should default to an empty set."
    assert isinstance(project.designed_for_task, set), "Designed for task should default to an empty set."
    assert project.publisher is None, "Publisher should default to None."


def test_project_large_set_attributes() -> None:
    """Test handling large sets for set-type attributes.

    This test verifies that the Project class can handle large sets for its set-type attributes,
    such as 'elements', 'acronyms', and 'bibliographic_citations'.

    :raises AssertionError: If large sets are not handled correctly.
    """
    large_strings = {f"string{i}" for i in range(1000)}

    project = Project(acronyms=large_strings, bibliographic_citations=large_strings)

    assert len(project.acronyms) == 1000, "Should handle large sets for 'acronyms'."


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
        Project(elements=[123, Package()])  # Mixing int and OntoumlElement in 'elements'

    with pytest.raises(ValidationError):
        Project(acronyms=[True, "ACR"])  # Mixing bool and str in 'acronyms'


def test_project_non_empty_values_post_initialization() -> None:
    """Test assigning empty values to attributes post-initialization."""
    project = Project(names=[create_langstring("Test")])
    project.namespace = "a"
    project.license = "b"
    project.publisher = "c"

    assert project.namespace == "a", "Should allow setting empty string for 'namespace' post-initialization."
    assert project.license == "b", "Should allow setting empty string for 'license' post-initialization."
    assert project.publisher == "c", "Should allow setting empty string for 'publisher' post-initialization."


def test_project_empty_values_post_initialization() -> None:
    """Test assigning empty values to attributes post-initialization."""
    project = Project(names=[create_langstring("Test")])

    with pytest.raises(ValidationError):
        project.namespace = ""
    with pytest.raises(ValidationError):
        project.license = ""
    with pytest.raises(ValidationError):
        project.publisher = ""


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


def test_project_empty_and_null_sets() -> None:
    """Test handling empty sets for set attributes.

    This test ensures that the Project class correctly handles empty sets for its set attributes,
    and raises appropriate errors when attempting to set them to None.

    :raises AssertionError: If empty sets are not handled correctly.
    :raises ValidationError: If setting an attribute to None does not raise an error.
    """
    project = Project()

    # Remove elements if any (though it should be initialized empty)
    project.elements.clear()

    assert project.elements == set(), "Elements should be an empty set after removal."

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

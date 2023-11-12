import uuid
from datetime import datetime, timedelta

import pytest
from pydantic import ValidationError

from ontouml_py.classes.abstract_syntax.project import Project
from ontouml_py.classes.ontoumlelement import OntoumlElement


class ConcreteOntoumlElement(OntoumlElement):
    """A concrete subclass of OntoumlElement for testing purposes."""

    def __init__(self, **data) -> None:
        """Initializes a new instance of ConcreteOntoumlElement.

        :param data: Fields to be set on the model instance.
        :type data: dict
        """
        super().__init__(**data)


@pytest.fixture
def concrete_ontouml_element() -> ConcreteOntoumlElement:
    """Provides a fixture for creating a concrete OntoumlElement instance for testing.

    :return: An instance of ConcreteOntoumlElement.
    :rtype: ConcreteOntoumlElement
    """
    return ConcreteOntoumlElement()


@pytest.fixture
def project() -> Project:
    """Provides a fixture for creating a Project instance for testing.

    :return: An instance of Project.
    :rtype: Project
    """
    return Project()


@pytest.fixture
def projects() -> list[Project]:
    """Provides a fixture for creating a list of Project instances for testing.

    :return: A list of Project instances.
    :rtype: list[Project]
    """
    return [Project() for _ in range(5)]


def test_ontouml_element_init(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test the initialization of a ConcreteOntoumlElement instance.

    Ensures that the 'id' attribute is initialized as a UUID.

    :param concrete_ontouml_element: A fixture instance of ConcreteOntoumlElement.
    :type concrete_ontouml_element: ConcreteOntoumlElement
    :raises AssertionError: If the 'id' attribute is not correctly initialized as a UUID.
    """
    assert isinstance(concrete_ontouml_element.id, uuid.UUID), "The 'id' attribute must be initialized as a UUID."


def test_abstract_class() -> None:
    """Test if the class OntoumlElement can be directly instantiated.

    :raises ValidationError: If the instantiation occurs.
    """
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        OntoumlElement()


def test_abstract_class_with_id() -> None:
    """Test if the class OntoumlElement can be directly instantiated.

    :raises ValidationError: If the instantiation occurs.
    """
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        OntoumlElement(id=uuid.uuid4())


def test_invalid_created_argument_type() -> None:
    """Test passing an invalid 'created' argument type during initialization of ConcreteOntoumlElement.

    :raises ValidationError: If a non-datetime value is passed for 'created'.
    """
    with pytest.raises(ValidationError, match=r"^1 validation error for ConcreteOntoumlElement\ncreated\n"):
        ConcreteOntoumlElement(created="not-a-datetime")


def test_invalid_modified_argument_type() -> None:
    """Test passing an invalid 'modified' argument type during initialization of ConcreteOntoumlElement.

    :raises ValidationError: If a non-datetime value is passed for 'modified'.
    """
    with pytest.raises(ValidationError, match=r"^1 validation error for ConcreteOntoumlElement\nmodified\n"):
        ConcreteOntoumlElement(modified="not-a-datetime")


def test_unknown_argument() -> None:
    """Test passing an unknown argument during initialization of ConcreteOntoumlElement.

    :raises TypeError: If an unexpected keyword argument is provided.
    """
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        ConcreteOntoumlElement(unknown_arg="value")


def test_none_argument_for_modified() -> None:
    """Test passing None for the 'modified' attribute in ConcreteOntoumlElement.

    Ensures None can be assigned to 'modified' without errors.

    :raises AssertionError: If 'modified' cannot be set to None.
    """
    element = ConcreteOntoumlElement(modified=None)
    assert element.modified is None, "The 'modified' attribute should accept None without errors."


def test_creation_time_in_future() -> None:
    """Test setting a future datetime for the 'created' attribute in ConcreteOntoumlElement.

    Ensures future datetime values are accepted for 'created'.

    :raises AssertionError: If future datetime values are not accepted for 'created'.
    """
    future_time = datetime.now() + timedelta(days=1)
    element = ConcreteOntoumlElement(created=future_time)
    assert element.created == future_time, "Future datetime values should be accepted for the 'created' attribute."


def test_modification_time_before_creation() -> None:
    """Test setting a modification time earlier than creation time in ConcreteOntoumlElement.

    :raises ValidationError: If 'modified' is set to a datetime earlier than 'created'.
    """
    creation_time = datetime.now()
    past_time = creation_time - timedelta(days=1)
    with pytest.raises(ValueError, match="The 'modified' datetime must be later than the 'created' datetime"):
        ConcreteOntoumlElement(created=creation_time, modified=past_time)


def test_same_creation_and_modification_time() -> None:
    """Test setting the same creation and modification time in ConcreteOntoumlElement.

    Ensures that 'modified' can be the same as 'created' without errors.

    :raises AssertionError: If 'modified' cannot be set to the same datetime as 'created'.
    """
    creation_time = datetime.now()
    element = ConcreteOntoumlElement(created=creation_time, modified=creation_time)
    assert element.modified == creation_time, "The 'modified' attribute should be allowed to be the same as 'created'."


def test_id_read_only(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test the immutability of the 'id' attribute in ConcreteOntoumlElement.

    :raises ValueError: If attempting to modify the 'id' attribute after initialization.
    """
    with pytest.raises(ValueError, match="Attribute 'id' is read-only and cannot be modified."):
        concrete_ontouml_element.id = uuid.uuid4()


def test_id_initialization_with_uuid() -> None:
    """Test initializing the 'id' attribute with a UUID."""
    custom_id = uuid.uuid4()
    element = ConcreteOntoumlElement(id=custom_id)
    assert element.id == custom_id, "The 'id' attribute should be initialized with the specified UUID."


def test_id_read_only_post_initialization(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test that the 'id' attribute is read-only after initialization."""
    with pytest.raises(ValueError, match="Attribute 'id' is read-only and cannot be modified."):
        concrete_ontouml_element.id = uuid.uuid4()


def test_created_initialization_with_datetime() -> None:
    """Test initializing the 'created' attribute with a specific datetime."""
    custom_time = datetime(2020, 1, 1)
    element = ConcreteOntoumlElement(created=custom_time)
    assert element.created == custom_time, "The 'created' attribute should be initialized with the specified datetime."


def test_created_read_only_post_initialization(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test that the 'created' attribute is read-only after initialization."""
    with pytest.raises(ValueError, match="Attribute 'created' is read-only and cannot be modified."):
        concrete_ontouml_element.created = datetime.now()


def test_modified_initialization_with_valid_datetime(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test initializing the 'modified' attribute with a valid datetime greater than 'created'."""
    modification_time = concrete_ontouml_element.created + timedelta(days=1)
    concrete_ontouml_element.modified = modification_time
    assert (
        concrete_ontouml_element.modified == modification_time
    ), "The 'modified' attribute should be set to the specified datetime."


def test_modified_initialization_with_none(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test initializing the 'modified' attribute with None."""
    concrete_ontouml_element.modified = None
    assert concrete_ontouml_element.modified is None, "The 'modified' attribute should accept None."


def test_modified_update_with_invalid_datetime(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test updating the 'modified' attribute with a datetime earlier than 'created'."""
    earlier_time = concrete_ontouml_element.created - timedelta(days=1)
    with pytest.raises(ValueError, match="The 'modified' datetime must be later than the 'created' datetime."):
        concrete_ontouml_element.modified = earlier_time


def test_modified_update_with_valid_datetime(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test updating the 'modified' attribute with a valid datetime greater than 'created'."""
    later_time = concrete_ontouml_element.created + timedelta(days=1)
    concrete_ontouml_element.modified = later_time
    assert (
        concrete_ontouml_element.modified == later_time
    ), "The 'modified' attribute should be updated to the specified datetime."


def test_id_initialization_with_non_uuid() -> None:
    """Test initializing the 'id' attribute with a non-UUID value."""
    with pytest.raises(ValidationError, match=r"Input should be a valid UUID"):
        ConcreteOntoumlElement(id="non-uuid-value")


def test_created_initialization_with_future_datetime() -> None:
    """Test initializing the 'created' attribute with a future datetime."""
    future_datetime = datetime.now() + timedelta(days=10)
    element = ConcreteOntoumlElement(created=future_datetime)
    assert element.created == future_datetime, "The 'created' attribute should accept future datetime values."


def test_created_initialization_with_past_datetime() -> None:
    """Test initializing the 'created' attribute with a past datetime."""
    past_datetime = datetime.now() - timedelta(days=10)
    element = ConcreteOntoumlElement(created=past_datetime)
    assert element.created == past_datetime, "The 'created' attribute should accept past datetime values."


def test_modified_initialization_with_same_as_created_datetime() -> None:
    """Test initializing the 'modified' attribute with a datetime equal to 'created'."""
    current_time = datetime.now()
    element = ConcreteOntoumlElement(created=current_time, modified=current_time)
    assert element.modified == current_time, "The 'modified' attribute should accept datetime equal to 'created'."


def test_modified_update_to_none_post_initialization(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test updating the 'modified' attribute to None after initialization."""
    concrete_ontouml_element.modified = None
    assert (
        concrete_ontouml_element.modified is None
    ), "The 'modified' attribute should be settable to None after initialization."


def test_modified_update_to_future_datetime(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test updating the 'modified' attribute to a future datetime."""
    future_datetime = datetime.now() + timedelta(days=5)
    concrete_ontouml_element.modified = future_datetime
    assert (
        concrete_ontouml_element.modified == future_datetime
    ), "The 'modified' attribute should accept future datetime values."


def test_modified_update_to_past_datetime(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test updating the 'modified' attribute to a past datetime earlier than 'created'."""
    past_datetime = concrete_ontouml_element.created - timedelta(days=1)
    with pytest.raises(ValueError, match="The 'modified' datetime must be later than the 'created' datetime."):
        concrete_ontouml_element.modified = past_datetime


def test_modified_initialization_with_invalid_type() -> None:
    """Test initializing the 'modified' attribute with an invalid type."""
    with pytest.raises(ValidationError):
        ConcreteOntoumlElement(modified="not-a-datetime")


def test_default_values_for_created_and_modified() -> None:
    """Test the default values for 'created' and 'modified' attributes."""
    element = ConcreteOntoumlElement()
    assert isinstance(
        element.created, datetime
    ), "The 'created' attribute should have a default value of the current datetime."
    assert element.modified is None, "The 'modified' attribute should have a default value of None."


def test_future_dates_for_created_and_modified() -> None:
    """Test setting future datetime values for 'created' and 'modified' attributes."""
    future_datetime = datetime.now() + timedelta(days=5)
    element = ConcreteOntoumlElement(created=future_datetime, modified=future_datetime)
    assert element.created == future_datetime, "Future datetime values should be valid for 'created'."
    assert element.modified == future_datetime, "Future datetime values should be valid for 'modified'."


def test_updating_modified_post_instantiation() -> None:
    """Test updating the 'modified' attribute to a valid datetime after instantiation."""
    element = ConcreteOntoumlElement()
    new_modified_time = datetime.now() + timedelta(hours=1)
    element.modified = new_modified_time
    assert (
        element.modified == new_modified_time
    ), "The 'modified' attribute should be updatable to a valid datetime after instantiation."


def test_custom_id_initialization() -> None:
    """Test initializing with a custom UUID for 'id'."""
    custom_uuid = uuid.uuid4()
    element = ConcreteOntoumlElement(id=custom_uuid)
    assert element.id == custom_uuid, "The 'id' attribute should accept a custom UUID during initialization."


def test_instantiation_with_no_arguments() -> None:
    """Test instantiation of ConcreteOntoumlElement with no arguments."""
    element = ConcreteOntoumlElement()
    assert isinstance(element.id, uuid.UUID), "The 'id' attribute should have a UUID value by default."
    assert isinstance(element.created, datetime), "The 'created' attribute should have a datetime value by default."
    assert element.modified is None, "The 'modified' attribute should be None by default."


def test_modified_same_as_created_at_initialization() -> None:
    """Test setting 'modified' the same as 'created' during initialization."""
    now = datetime.now()
    element = ConcreteOntoumlElement(created=now, modified=now)
    assert (
        element.modified == now
    ), "The 'modified' attribute should be able to be set the same as 'created' at initialization."


def test_instantiation_with_partial_arguments() -> None:
    """Test instantiation of ConcreteOntoumlElement with partial arguments."""
    custom_time = datetime.now() - timedelta(days=1)
    element = ConcreteOntoumlElement(created=custom_time)
    assert element.created == custom_time, "The 'created' attribute should be set to the provided datetime."
    assert element.modified is None, "The 'modified' attribute should be None by default when not provided."


def test_invalid_types_for_created_and_modified() -> None:
    """Test passing invalid types for 'created' and 'modified' attributes."""
    with pytest.raises(ValidationError):
        ConcreteOntoumlElement(created="invalid-type")
    with pytest.raises(ValidationError):
        ConcreteOntoumlElement(modified="invalid-type")


def test_default_id_immutable() -> None:
    """Test that the default 'id' is immutable."""
    element = ConcreteOntoumlElement()
    original_id = element.id
    with pytest.raises(ValueError, match="Attribute 'id' is read-only and cannot be modified."):
        element.id = uuid.uuid4()
    assert element.id == original_id, "The default 'id' should be immutable."


def test_modified_accept_none_post_instantiation() -> None:
    """Test that the 'modified' attribute can be set to None after instantiation."""
    element = ConcreteOntoumlElement()
    element.modified = None
    assert element.modified is None, "The 'modified' attribute should accept None post-instantiation."


def test_error_when_modified_before_created() -> None:
    """Test an error is raised if 'modified' is set to a datetime before 'created'."""
    element = ConcreteOntoumlElement()
    with pytest.raises(ValueError, match="The 'modified' datetime must be later than the 'created' datetime."):
        element.modified = element.created - timedelta(days=1)


def test_non_existent_attribute() -> None:
    """Test if attribution to a non-existent attribute will result in an error."""
    element = ConcreteOntoumlElement()
    with pytest.raises(ValidationError, match=r"Object has no attribute"):
        element.att = 1


def test_addition_updates_in_project(concrete_ontouml_element: ConcreteOntoumlElement, project: Project) -> None:
    """Test that adding an element to a project updates its `in_project` attribute."""
    project.add_element(concrete_ontouml_element)
    assert project in concrete_ontouml_element.in_project, "Project should be in element's `in_project` list."


def test_in_project_integrity_multiple_additions(
    concrete_ontouml_element: ConcreteOntoumlElement, projects: list[Project]
) -> None:
    """Test integrity of `in_project` list after adding the element to multiple projects."""
    for proj in projects:
        proj.add_element(concrete_ontouml_element)
    assert all(
        proj in concrete_ontouml_element.in_project for proj in projects
    ), "All projects should be in `in_project` list."


def test_direct_modification_of_in_project_raises_error(concrete_ontouml_element: ConcreteOntoumlElement) -> None:
    """Test that direct modification of `in_project` attribute raises an error."""
    with pytest.raises(ValueError):
        concrete_ontouml_element.in_project = []


def test_removal_from_one_project_keeps_in_others(
    concrete_ontouml_element: ConcreteOntoumlElement, projects: list[Project]
) -> None:
    """Test removing element from one project keeps it in other projects."""
    for proj in projects:
        proj.add_element(concrete_ontouml_element)
    projects[0].remove_element(concrete_ontouml_element)
    assert all(
        proj in concrete_ontouml_element.in_project for proj in projects[1:]
    ), "Element should remain in other projects."


def test_in_project_not_affected_by_external_list_changes(
    concrete_ontouml_element: ConcreteOntoumlElement, project: Project
) -> None:
    """Test that external changes to a list do not affect `in_project`."""
    temp_list = [project]
    project.add_element(concrete_ontouml_element)
    temp_list.clear()
    assert (
        project in concrete_ontouml_element.in_project
    ), "`in_project` should not be affected by external list changes."


def test_no_duplicates_in_project_after_repeated_additions(
    concrete_ontouml_element: ConcreteOntoumlElement, project: Project
) -> None:
    """Test that `in_project` contains no duplicates after repeated additions."""
    for _ in range(5):
        project.add_element(concrete_ontouml_element)
    assert concrete_ontouml_element.in_project.count(project) == 1, "No duplicates should be in `in_project`."


def test_project_not_in_in_project_after_removal_from_multiple_projects(
    concrete_ontouml_element: ConcreteOntoumlElement, projects: list[Project]
) -> None:
    """Test that a project is not in `in_project` after being removed from multiple projects."""
    for proj in projects:
        proj.add_element(concrete_ontouml_element)
    for proj in projects:
        proj.remove_element(concrete_ontouml_element)
    assert all(
        proj not in concrete_ontouml_element.in_project for proj in projects
    ), "Removed projects should not be in `in_project`."


def test_in_project_correct_after_removal_and_readdition(
    concrete_ontouml_element: ConcreteOntoumlElement, project: Project
) -> None:
    """Test `in_project` is correct after removing and re-adding an element."""
    project.add_element(concrete_ontouml_element)
    project.remove_element(concrete_ontouml_element)
    project.add_element(concrete_ontouml_element)
    assert project in concrete_ontouml_element.in_project, "`in_project` should be correct after re-adding element."

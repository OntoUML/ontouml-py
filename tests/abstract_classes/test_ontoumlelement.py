import uuid
from datetime import datetime
from datetime import timedelta

import pytest
from pydantic import ValidationError

from ontouml_py.model.ontoumlelement import OntoumlElement
from ontouml_py.model.project import Project


def test_abstract_class() -> None:
    """Test if the class OntoumlElement can be directly instantiated.

    :raises TypeError: If the instantiation of OntoumlElement occurs.
    """
    with pytest.raises(TypeError, match="Can't instantiate abstract class OntoumlElement"):
        OntoumlElement()


def test_invalid_modified_argument_type() -> None:
    """Test passing an invalid 'modified' argument type during initialization of Project.

    :raises ValidationError: If a non-datetime value is passed for 'modified'.
    """
    with pytest.raises(
        ValidationError, match="1 validation error for Project\nmodified\n  Input should be a valid datetime"
    ):
        Project(modified="not-a-datetime")


def test_unknown_argument() -> None:
    """Test passing an unknown argument during initialization of Project.

    :raises ValidationError: If an unexpected keyword argument is provided.
    """
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        Project(unknown_arg="value")


def test_same_creation_and_modification_time() -> None:
    """Test setting the same creation and modification time in Project.

    Ensures that 'modified' can be the same as 'created' without errors.

    :raises AssertionError: If 'modified' cannot be set to the same datetime as 'created'.
    """
    creation_time = datetime.now()
    element = Project(created=creation_time, modified=creation_time)
    assert element.modified == creation_time, "The 'modified' attribute should be allowed to be the same as 'created'."


def test_id_initialization_with_uuid() -> None:
    """Test initializing the 'id' attribute with a UUID in Project.

    :raises AssertionError: If 'id' is not initialized with the specified UUID.
    """
    custom_id = str(uuid.uuid4())
    element = Project(id=custom_id)
    assert element.id == custom_id, "The 'id' attribute should be initialized with the specified UUID."


def test_modified_initialization_with_valid_datetime() -> None:
    """Test initializing the 'modified' attribute with a valid datetime greater than 'created' in Project.

    :raises AssertionError: If 'modified' is not set to the specified datetime.
    """
    concrete_ontouml_element = Project()
    modification_time = concrete_ontouml_element.created + timedelta(days=1)
    concrete_ontouml_element.modified = modification_time
    assert (
        concrete_ontouml_element.modified == modification_time
    ), "The 'modified' attribute should be set to the specified datetime."


def test_modified_initialization_with_none() -> None:
    """Test initializing the 'modified' attribute with None in Project.

    :raises AssertionError: If 'modified' does not accept None.
    """
    concrete_ontouml_element = Project()
    concrete_ontouml_element.modified = None
    assert concrete_ontouml_element.modified is None, "The 'modified' attribute should accept None."


def test_modified_update_with_valid_datetime() -> None:
    """Test updating the 'modified' attribute with a valid datetime greater than 'created' in Project.

    :raises AssertionError: If 'modified' is not updated to the specified datetime.
    """
    concrete_ontouml_element = Project()
    later_time = concrete_ontouml_element.created + timedelta(days=1)
    concrete_ontouml_element.modified = later_time
    assert (
        concrete_ontouml_element.modified == later_time
    ), "The 'modified' attribute should be updated to the specified datetime."


def test_id_initialization_with_non_uuid() -> None:
    """Test initializing the 'id' attribute with a non-string value in Project.

    :raises ValidationError: If 'id' is not a valid string.
    """
    with pytest.raises(ValidationError, match="Input should be a valid string"):
        Project(id=1)


def test_created_initialization_with_future_datetime() -> None:
    """Test initializing the 'created' attribute with a future datetime in Project.

    :raises AssertionError: If 'created' does not accept future datetime values.
    """
    future_datetime = datetime.now() + timedelta(days=10)
    element = Project(created=future_datetime)
    assert element.created == future_datetime, "The 'created' attribute should accept future datetime values."


def test_created_initialization_with_past_datetime() -> None:
    """Test initializing the 'created' attribute with a past datetime in Project.

    :raises AssertionError: If 'created' does not accept past datetime values.
    """
    past_datetime = datetime.now() - timedelta(days=10)
    element = Project(created=past_datetime)
    assert element.created == past_datetime, "The 'created' attribute should accept past datetime values."


def test_modified_initialization_with_same_as_created_datetime() -> None:
    """Test initializing the 'modified' attribute with a datetime equal to 'created' in Project.

    :raises AssertionError: If 'modified' does not accept datetime equal to 'created'.
    """
    current_time = datetime.now()
    element = Project(created=current_time, modified=current_time)
    assert element.modified == current_time, "The 'modified' attribute should accept datetime equal to 'created'."


def test_modified_update_to_none_post_initialization() -> None:
    """Test updating the 'modified' attribute to None after initialization in Project.

    :raises AssertionError: If 'modified' cannot be set to None after initialization.
    """
    concrete_ontouml_element = Project()
    concrete_ontouml_element.modified = None
    assert (
        concrete_ontouml_element.modified is None
    ), "The 'modified' attribute should be settable to None after initialization."


def test_modified_initialization_with_invalid_type() -> None:
    """Test initializing the 'modified' attribute with an invalid type in Project.

    :raises ValidationError: If 'modified' is not a valid datetime.
    """
    with pytest.raises(ValidationError, match="Input should be a valid datetime"):
        Project(modified="not-a-datetime")


def test_default_values_for_created_and_modified() -> None:
    """Test the default values for 'created' and 'modified' attributes in Project.

    :raises AssertionError: If default values for 'created' and 'modified' are not as expected.
    """
    element = Project()
    assert isinstance(
        element.created, datetime
    ), "The 'created' attribute should have a default value of the current datetime."
    assert element.modified is None, "The 'modified' attribute should have a default value of None."


def test_future_dates_for_created_and_modified() -> None:
    """Test setting future datetime values for 'created' and 'modified' attributes in Project.

    :raises AssertionError: If future datetime values are not valid for 'created' and 'modified'.
    """
    future_datetime = datetime.now() + timedelta(days=5)
    element = Project(created=future_datetime, modified=future_datetime)
    assert element.created == future_datetime, "Future datetime values should be valid for 'created'."
    assert element.modified == future_datetime, "Future datetime values should be valid for 'modified'."


def test_updating_modified_post_instantiation() -> None:
    """Test updating the 'modified' attribute to a valid datetime after instantiation in Project.

    :raises AssertionError: If 'modified' cannot be updated to a valid datetime after instantiation.
    """
    element = Project()
    new_modified_time = datetime.now() + timedelta(hours=1)
    element.modified = new_modified_time
    assert (
        element.modified == new_modified_time
    ), "The 'modified' attribute should be updatable to a valid datetime after instantiation."


def test_instantiation_with_no_arguments() -> None:
    """Test instantiation of Project with no arguments.

    :raises AssertionError: If default values for 'id', 'created', and 'modified' are not as expected.
    """
    element = Project()
    assert isinstance(element.id, str), "The 'id' attribute should have a UUID string value by default."
    assert isinstance(element.created, datetime), "The 'created' attribute should have a datetime value by default."
    assert element.modified is None, "The 'modified' attribute should be None by default."


def test_modified_same_as_created_at_initialization() -> None:
    """Test setting 'modified' the same as 'created' during initialization in Project.

    :raises AssertionError: If 'modified' cannot be set the same as 'created' at initialization.
    """
    now = datetime.now()
    element = Project(created=now, modified=now)
    assert (
        element.modified == now
    ), "The 'modified' attribute should be able to be set the same as 'created' at initialization."


def test_instantiation_with_partial_arguments() -> None:
    """Test instantiation of Project with partial arguments.

    :raises AssertionError: If 'created' and 'modified' attributes are not set as expected when provided.
    """
    custom_time = datetime.now() - timedelta(days=1)
    element = Project(created=custom_time)
    assert element.created == custom_time, "The 'created' attribute should be set to the provided datetime."
    assert element.modified is None, "The 'modified' attribute should be None by default when not provided."


def test_invalid_types_for_created_and_modified() -> None:
    """Test passing invalid types for 'created' and 'modified' attributes in Project.

    :raises ValidationError: If invalid types are passed for 'created' and 'modified'.
    """
    with pytest.raises(ValidationError, match="Input should be a valid datetime"):
        Project(created="invalid-type")
    with pytest.raises(ValidationError, match="Input should be a valid datetime"):
        Project(modified="invalid-type")


# Example concrete subclass of NamedElement for testing
class Shape(OntoumlElement):
    def __init__(self, **data):
        super().__init__(**data)


# Test instantiation of allowed subclass: NamedElement
def test_instantiation_allowed_subclass_namedelement() -> None:
    """Test instantiation of a class allowed in _allowed_subclasses."""

    try:
        element = Project()  # noqa: F841 (flake8)
    except ValueError:
        pytest.fail("Instantiation of Package should not raise ValueError.")


# Test instantiation of allowed subclass: Shape
def test_instantiation_allowed_subclass_shape() -> None:
    """Test instantiation of a class allowed in _allowed_subclasses."""
    try:
        shape = Shape()
    except ValueError:
        pytest.fail("Instantiation of Shape should not raise ValueError.")


# Test instantiation of a disallowed subclass
def test_instantiation_disallowed_subclass() -> None:
    """Test instantiation of a class not allowed in _allowed_subclasses."""

    class DisallowedElement(OntoumlElement):
        def __init__(self, **data):
            super().__init__(**data)

    with pytest.raises(ValueError, match="is not an allowed subclass"):
        DisallowedElement()


# Test deep inheritance chain with allowed subclass
def test_deep_inheritance_chain_allowed_subclass() -> None:
    """Test instantiation of a class in a deep inheritance chain that is allowed."""

    class DeepShape(Shape):
        pass

    try:
        deep_shape = DeepShape()
    except ValueError:
        pytest.fail("Instantiation of DeepShape should not raise ValueError.")


# Test dynamic class creation and instantiation
def test_dynamic_class_creation_instantiation() -> None:
    """Test dynamic creation and instantiation of a subclass."""
    dynamic_element = type("dynamic_element", (Project,), {})
    try:
        dynamic_element = dynamic_element()
    except ValueError:
        pytest.fail("Instantiation of dynamic_element should not raise ValueError.")


# Test error message for disallowed subclass
def test_error_message_disallowed_subclass() -> None:
    """Test the error message for instantiating a disallowed subclass."""

    class DisallowedElement(OntoumlElement):
        """A subclass of OntoumlElement that is not allowed according to the subclass restrictions.

        This class is used for testing the behavior of OntoumlElement when an attempt is made to instantiate
        a subclass that is not permitted.

        :param data: Arbitrary keyword arguments.
        :type data: dict
        :raises ValueError: If instantiated, as it's not an allowed subclass of OntoumlElement.
        """

        def __init__(self, **data) -> None:
            super().__init__(**data)

    with pytest.raises(ValueError, match="is not an allowed subclass"):
        DisallowedElement()


def test_initialization_with_empty_string() -> None:
    """Test the behavior of initializing a Project with an empty string for string-based attributes.

    :raises ValidationError: If the object does not handle empty string initialization as expected.
    """
    with pytest.raises(ValidationError, match="validation error for Project"):
        Project(name="")


def test_initialization_with_empty_list() -> None:
    """Test the behavior of initializing a Project with an empty list for list-based attributes.

    :raises ValidationError: If the object does not handle empty list initialization as expected.
    """
    with pytest.raises(ValidationError, match="validation error for Project"):
        Project(some_list_attribute=[])


def test_initialization_with_empty_tuple() -> None:
    """Test the behavior of initializing a Project with an empty tuple for tuple-based attributes.

    :raises ValidationError: If the object does not handle empty tuple initialization as expected.
    """
    with pytest.raises(ValidationError, match="validation error for Project"):
        Project(some_tuple_attribute=())


def test_post_initialization_type_validation() -> None:
    """Test the type validation for an attribute of Project after the object has been instantiated.

    :raises ValidationError: If the object allows setting an attribute to an invalid type post-instantiation.
    """
    element = Project()
    with pytest.raises(ValidationError, match="Object has no attribute 'some_attribute'"):
        element.some_attribute = 123  # Assuming 'some_attribute' should be a string


def test_post_initialization_with_empty_string() -> None:
    """Test setting an attribute to an empty string on a Project instance after it has been instantiated.

    :raises ValidationError: If the object allows setting a string attribute to an empty string post-instantiation.
    """
    element = Project()
    with pytest.raises(ValidationError, match="Object has no attribute 'name'"):
        element.name = ""


def test_post_initialization_id_with_invalid_uuid() -> None:
    """Test setting the 'id' attribute to an invalid UUID on a Project instance after it has been instantiated.

    :raises ValidationError: If the object allows setting the 'id' attribute to an invalid UUID post-instantiation.
    """
    element = Project()
    with pytest.raises(ValidationError, match="Input should be a valid string"):
        element.id = 123  # invalid-uuid


def test_post_initialization_created_with_none() -> None:
    """Test setting the 'created' attribute to None on a Project instance after it has been instantiated.

    :raises ValidationError: If the object allows setting the 'created' attribute to None post-instantiation.
    """
    element = Project()
    with pytest.raises(ValidationError, match="Input should be a valid datetime"):
        element.created = None


def test_id_with_not_enough_chars() -> None:
    """Test setting the id attribute to strings with less than zero chars in Project.

    :raises ValueError: If the object allows setting the id with less than 3 chars.
    """
    element = Project()
    with pytest.raises(ValueError, match="1 validation error for Project"):
        element.id = ""


@pytest.mark.parametrize("new_id", ["1", "22", "a"])
def test_id_with_enough_chars(new_id: str) -> None:
    """Test setting the id attribute to strings with 1 or more chars in Project.

    :param new_id: The new id to be set.
    :type new_id: str
    :raises AssertionError: If the id is not set as expected.
    """
    element = Project()
    element.id = new_id
    assert element.id


# Test for successful initialization
def test_ontoumlelement_initialization() -> None:
    """Test the successful initialization of an OntoumlElement instance.

    :return: None
    :raises AssertionError: If the OntoumlElement instance does not initialize correctly.
    """
    concrete_ontouml_element = Project()
    element = concrete_ontouml_element
    assert isinstance(element, OntoumlElement), "OntoumlElement should initialize successfully."


def test_ontoumlelement_hashability() -> None:
    """Test that OntoumlElement instances are hashable and their hash is based on the unique identifier.
    :return: None
    :raises AssertionError: If OntoumlElement instances are not hashable or their hash is not based on the id.
    """
    element1 = Project()
    element2 = Project().__class__()  # Create a new instance with a different id

    # Ensure that the IDs are different
    assert element1.id != element2.id, "The two elements should have different ids for this test."

    element_set = {element1, element2}
    assert len(element_set) == 2, "OntoumlElement instances should be uniquely hashable based on their id."


# Test for equality based on unique identifier
def test_ontoumlelement_equality() -> None:
    """Test that OntoumlElement instances are considered equal if they have the same unique identifier.

    :return: None
    :raises AssertionError: If OntoumlElement instances with the same id are not considered equal.
    """
    element1 = Project()
    element2 = Project().__class__()
    element2.id = element1.id
    assert element1 == element2, "OntoumlElement instances with the same id should be considered equal."


# Test for subclass restriction
def test_ontoumlelement_subclass_restriction() -> None:
    """Test that OntoumlElement cannot be instantiated if it is not a subclass of allowed types.

    :return: None
    :raises AssertionError: If OntoumlElement is instantiated as an unauthorized subclass.
    """

    class UnauthorizedElement(OntoumlElement):
        def __init__(self, **data):
            super().__init__(**data)

    with pytest.raises(ValueError, match="is not an allowed subclass"):
        UnauthorizedElement()

def test_abstract_class_instantiation() -> None:
    """Test if the abstract class OntoumlElement can be instantiated directly.

    :raises TypeError: If direct instantiation of OntoumlElement is attempted.
    """
    with pytest.raises(TypeError, match="Can't instantiate abstract class OntoumlElement without an implementation"):
        OntoumlElement()


def test_ontoumlelement_equality_different_objects() -> None:
    """Test the equality of two different OntoumlElement objects.

    :raises AssertionError: If two different OntoumlElement objects are considered equal.
    """
    element1 = Project()
    element2 = Project()
    assert element1 != element2, "Different OntoumlElement instances should not be equal."


def test_ontoumlelement_hash_collision() -> None:
    """Test for hash collisions between different OntoumlElement instances.

    :raises AssertionError: If two different OntoumlElement instances have the same hash value.
    """
    element1 = Project()
    element2 = Project()
    assert hash(element1) != hash(element2), "Different OntoumlElement instances should have different hash values."


def test_ontoumlelement_validate_subclasses_invalid_subclass() -> None:
    """Test the subclass validation mechanism with an invalid subclass.

    :raises ValueError: If an invalid subclass is used.
    """
    class InvalidElement(OntoumlElement):
        pass

    with pytest.raises(TypeError, match="Can't instantiate abstract class InvalidElement without an implementation"):
        InvalidElement()


def test_ontoumlelement_validate_subclasses_valid_subclass() -> None:
    """Test the subclass validation mechanism with a valid subclass.

    :raises AssertionError: If a valid subclass raises a ValueError.
    """
    try:
        valid_element = Project()
        assert isinstance(valid_element, OntoumlElement), "Project should be a valid subclass of OntoumlElement."
    except ValueError:
        pytest.fail("Valid subclass should not raise ValueError.")
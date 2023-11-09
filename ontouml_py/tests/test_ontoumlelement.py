import uuid
from datetime import datetime, timedelta

import pytest

from ontouml_py.classes.ontoumlelement import OntoumlElement


# Create a stub subclass just for testing purposes, as the OntoumlElement class is abstract.
class StubOntoumlElement(OntoumlElement):
    def __init__(self, created: datetime = datetime.now(), modified: datetime = None):
        super().__init__(created, modified)

    @property
    def id(self):
        """The read-only unique identifier of the OntoumlElement."""
        return self._id  # Directly access the protected _id attribute.


@pytest.fixture
def stub_ontouml_element() -> StubOntoumlElement:
    """Fixture for creating a stub OntoumlElement instance."""
    return StubOntoumlElement()


def test_ontouml_element_init(stub_ontouml_element: StubOntoumlElement):
    """
    Test the initialization of a StubOntoumlElement instance to ensure that the id, created, and modified
    attributes are set appropriately.

    :param stub_ontouml_element: A fixture instance of the stub subclass of OntoumlElement.
    :type stub_ontouml_element: StubOntoumlElement
    """
    element = stub_ontouml_element
    assert isinstance(element.id, uuid.UUID), "id attribute must be a UUID"


def test_invalid_created_argument_type():
    """Test the initialization of a StubOntoumlElement with an invalid 'created' argument type to ensure it raises
    a TypeError.
    """
    with pytest.raises(TypeError, match=r"The 'created' argument must be a datetime, not str"):
        # Pass incorrect type to 'created' to simulate a TypeError
        StubOntoumlElement(created="not-a-datetime")


def test_invalid_modified_argument_type():
    """Test the initialization of a StubOntoumlElement with an invalid 'modified' argument type to ensure it raises
    a TypeError.
    """
    with pytest.raises(TypeError, match=r"The 'modified' argument must be a datetime or None, not str"):
        # Pass incorrect type to 'modified' to simulate a TypeError
        StubOntoumlElement(modified="not-a-datetime")


def test_unknown_argument(stub_ontouml_element: StubOntoumlElement):
    """Test the initialization of a StubOntoumlElement with an unknown argument to ensure it raises a TypeError.

    :param stub_ontouml_element: A fixture instance of the stub subclass of OntoumlElement.
    :type stub_ontouml_element: StubOntoumlElement
    """
    with pytest.raises(TypeError, match="got an unexpected keyword argument 'unknown_arg'"):
        # Pass an unknown keyword argument to simulate a TypeError
        StubOntoumlElement(unknown_arg="value")


def test_none_argument(stub_ontouml_element: StubOntoumlElement):
    """Test the initialization of a StubOntoumlElement with None as an argument to ensure it handles None correctly.

    :param stub_ontouml_element: A fixture instance of the stub subclass of OntoumlElement.
    :type stub_ontouml_element: StubOntoumlElement
    """
    # It's allowed to pass None for 'modified', but not for 'created' as per our class definition
    element = StubOntoumlElement(modified=None)
    assert element.modified is None, "modified attribute should accept None"

    with pytest.raises(TypeError, match="argument must be a datetime, not NoneType"):
        # Trying to pass None to 'created' should raise an error
        StubOntoumlElement(created=None)


def test_creation_time_in_future(stub_ontouml_element: StubOntoumlElement):
    """Test the initialization of a StubOntoumlElement with a creation time set in the future to ensure it handles
    future datetime correctly.

    :param stub_ontouml_element: A fixture instance of the stub subclass of OntoumlElement.
    :type stub_ontouml_element: StubOntoumlElement
    """
    future_time = datetime.now() + timedelta(days=1)
    element = StubOntoumlElement(created=future_time)
    assert element.created == future_time, "created attribute should handle future datetime values"


def test_modification_time_before_creation(stub_ontouml_element: StubOntoumlElement):
    """Test the initialization of a StubOntoumlElement with a modification time set before the creation time to
    ensure logical consistency is maintained.

    :param stub_ontouml_element: A fixture instance of the stub subclass of OntoumlElement.
    :type stub_ontouml_element: StubOntoumlElement
    """
    creation_time = datetime.now()
    past_time = creation_time - timedelta(days=1)
    with pytest.raises(ValueError, match="The 'modified' datetime must be later than the 'created' datetime"):
        StubOntoumlElement(created=creation_time, modified=past_time)


def test_same_creation_and_modification_time(stub_ontouml_element: StubOntoumlElement):
    """Test the initialization of a StubOntoumlElement with the same creation and modification time to ensure
    it is handled appropriately.

    :param stub_ontouml_element: A fixture instance of the stub subclass of OntoumlElement.
    :type stub_ontouml_element: StubOntoumlElement
    """
    creation_time = datetime.now()
    element = StubOntoumlElement(created=creation_time, modified=creation_time)
    assert element.modified == creation_time, "modified attribute should be allowed to be the same as creation time"


def test_id_read_only():
    """Test that the id attribute is read-only by attempting to assign a new value to it after instantiation."""
    element = StubOntoumlElement()
    with pytest.raises(AttributeError):
        element.id = uuid.uuid4()  # Attempting to reassign the 'id' attribute should raise an AttributeError


def test_id_read_only(stub_ontouml_element: StubOntoumlElement):
    """Test that the id attribute is read-only by attempting to assign a new value to it after instantiation."""
    element = stub_ontouml_element
    with pytest.raises(AttributeError):
        element.id = uuid.uuid4()  # Attempting to reassign the 'id' attribute should raise an AttributeError

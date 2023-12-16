import pytest
from pydantic import ValidationError

from ontouml_py.model.package import Package
from ontouml_py.model.packageable import Packageable


def test_package_initialization(valid_project):
    """
    Test the initialization of a Package instance.

    :param valid_project: A valid Project instance.
    :return: None
    """
    package = Package(valid_project)
    assert isinstance(package, Package), "Package instance should be created successfully."


@pytest.mark.parametrize(
    "content_type, content_instance",
    [
        ("Anchor", pytest.lazy_fixture("valid_anchor")),
        ("BinaryRelation", pytest.lazy_fixture("valid_binary_relation")),
        ("Class", pytest.lazy_fixture("valid_class")),
        ("Generalization", pytest.lazy_fixture("valid_generalization")),
        ("GeneralizationSet", pytest.lazy_fixture("valid_generalization_set")),
        ("NaryRelation", pytest.lazy_fixture("valid_nary_relation")),
        ("Note", pytest.lazy_fixture("valid_note")),
        ("Package", pytest.lazy_fixture("valid_package")),
    ],
)
def test_get_content_by_id_valid_content(valid_package, content_type, content_instance):
    """
    Test retrieving content by ID with valid content types.

    :param valid_package: A valid Package instance.
    :param content_type: The type of content to be tested.
    :param content_instance: An instance of the content type.
    :return: None
    """
    valid_package._contents[content_type].add(content_instance)
    retrieved_content = valid_package.get_content_by_id(content_type, content_instance.id)
    assert retrieved_content == content_instance, f"Should retrieve the correct {content_type} instance."


def test_get_content_by_id_invalid_content(valid_package):
    """
    Test retrieving content by ID with an invalid content type.

    :param valid_package: A valid Package instance.
    :return: None
    """
    with pytest.raises(KeyError, match="InvalidType"):
        _ = valid_package.get_content_by_id("InvalidType", "some_id")


def test_remove_content_valid(valid_package, valid_anchor):
    """
    Test removing valid content from a package.

    :param valid_package: A valid Package instance.
    :param valid_anchor: A valid Anchor instance.
    :return: None
    """
    valid_package.add_anchor(valid_anchor)
    valid_package.remove_content(valid_anchor)
    valid_package_contents = valid_package.get_contents()
    assert valid_anchor not in valid_package_contents["Anchor"], "Anchor should be removed from the package."


def test_remove_content_invalid(valid_package, valid_anchor):
    """
    Test removing invalid content from a package.

    :param valid_package: A valid Package instance.
    :param valid_anchor: A valid Anchor instance.
    :return: None
    """
    with pytest.raises(ValueError, match="Invalid Anchor content for removal."):
        valid_package.remove_content(valid_anchor)


def test_packageable_abstract_instantiation():
    """
    Test that instantiating the abstract class Packageable raises a TypeError.

    :return: None
    """
    with pytest.raises(TypeError, match="Packageable is an abstract class and cannot be instantiated."):
        Packageable()


def test_get_contents_empty_package(valid_package):
    """
    Test the get_contents method on an empty package.

    :param valid_package: A valid Package instance.
    :return: None
    """
    contents = valid_package.get_contents()
    assert isinstance(contents, dict), "get_contents should return a dictionary."
    assert all(isinstance(v, set) for v in contents.values()), "All values in the contents dictionary should be sets."
    assert all(len(v) == 0 for v in contents.values()), "All sets in the contents dictionary should be empty."


def test_remove_content_not_in_package(valid_package, valid_anchor):
    """
    Test removing a content item that is not in the package.

    :param valid_package: A valid Package instance.
    :param valid_anchor: A valid Anchor instance not added to the package.
    :return: None
    """
    with pytest.raises(ValueError, match="Invalid Anchor content for removal."):
        valid_package.remove_content(valid_anchor)


def test_package_initialization_with_invalid_data(valid_project):
    """
    Test the initialization of a Package instance with invalid data.

    :param valid_project: A valid Project instance.
    :return: None
    """
    with pytest.raises(ValidationError):
        Package(valid_project, invalid_field="invalid_value")

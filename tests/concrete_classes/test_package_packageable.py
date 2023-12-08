import pytest
from pydantic import ValidationError

from ontouml_py.model.package import Package
from ontouml_py.model.packageable import Packageable


# Fixtures
@pytest.fixture
def empty_package() -> Package:
    """Fixture to create an empty Package instance."""
    return Package()


@pytest.fixture
def packageable_content() -> Packageable:
    """Fixture to create a mock Packageable instance."""

    class Anchor(Packageable):
        def __init__(self):
            super().__init__()

    return Anchor()


# Tests
def test_package_initialization(empty_package: Package) -> None:
    """Test the initialization of a Package instance.

    :param empty_package: Fixture providing an empty Package instance.
    """
    assert isinstance(empty_package, Package), "Package instance should be correctly initialized."


def test_add_packageable_content_to_package(empty_package: Package, packageable_content: Packageable) -> None:
    """Test adding a Packageable content to a Package.

    :param empty_package: Fixture providing an empty Package instance.
    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    empty_package.add_content(packageable_content)
    assert packageable_content in empty_package.contents, "Packageable content should be added to the package."


def test_remove_packageable_content_from_package(empty_package: Package, packageable_content: Packageable) -> None:
    """Test removing a Packageable content from a Package.

    :param empty_package: Fixture providing an empty Package instance.
    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    empty_package.add_content(packageable_content)
    empty_package.remove_content(packageable_content)
    assert packageable_content not in empty_package.contents, "Packageable content should be removed from the package."


def test_adding_self_to_package_contents(empty_package: Package) -> None:
    """Test that a Package cannot contain itself.

    :param empty_package: Fixture providing an empty Package instance.
    """
    with pytest.raises(TypeError):
        empty_package.add_content(empty_package)


def test_adding_non_packageable_content_to_package(empty_package: Package) -> None:
    """Test adding a non-Packageable content to a Package.

    :param empty_package: Fixture providing an empty Package instance.
    """
    with pytest.raises(TypeError):
        empty_package.add_content(object())


def test_removing_nonexistent_content_from_package(empty_package: Package, packageable_content: Packageable) -> None:
    """Test removing a content that is not in the package.

    :param empty_package: Fixture providing an empty Package instance.
    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    with pytest.raises(ValueError):
        empty_package.remove_content(packageable_content)


def test_package_contents_read_only_property(empty_package: Package, packageable_content: Packageable) -> None:
    """Test the read-only property of package contents.

    :param empty_package: Fixture providing an empty Package instance.
    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    empty_package.add_content(packageable_content)
    with pytest.raises(AttributeError):
        empty_package.contents = set()


def test_packageable_in_package_property(packageable_content: Packageable, empty_package: Package) -> None:
    """Test the 'in_package' property of a Packageable content.

    :param packageable_content: Fixture providing a mock Packageable instance.
    :param empty_package: Fixture providing an empty Package instance.
    """
    empty_package.add_content(packageable_content)
    assert packageable_content.in_package == empty_package, "'in_package' should reference the containing package."


def test_packageable_in_package_setter_restriction(packageable_content: Packageable) -> None:
    """Test that the 'in_package' property of a Packageable content cannot be set directly.

    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    with pytest.raises(AttributeError):
        packageable_content.in_package = object()


def test_package_initialization_with_contents(packageable_content: Packageable) -> None:
    """Test initializing a Package with a set of Packageable contents.

    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    with pytest.raises(ValidationError):
        Package(contains={packageable_content})


def test_removing_never_added_content_from_package(empty_package: Package, packageable_content: Packageable) -> None:
    """Test removing a content that was never added to the package.

    :param empty_package: Fixture providing an empty Package instance.
    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    with pytest.raises(ValueError):
        empty_package.remove_content(packageable_content)


def test_adding_duplicate_contents_to_package(empty_package: Package, packageable_content: Packageable) -> None:
    """Test adding the same Packageable content multiple times to a Package.

    :param empty_package: Fixture providing an empty Package instance.
    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    empty_package.add_content(packageable_content)
    empty_package.add_content(packageable_content)  # Add the same content again
    assert len(empty_package.contents) == 1, "Duplicate contents should not be added to the package."


def test_packageable_content_package_after_removal(empty_package: Package, packageable_content: Packageable) -> None:
    """Test the 'in_package' property of a Packageable content after it is removed from a package.

    :param empty_package: Fixture providing an empty Package instance.
    :param packageable_content: Fixture providing a mock Packageable instance.
    """
    empty_package.add_content(packageable_content)
    empty_package.remove_content(packageable_content)
    assert empty_package.contents == set(), "'contents' should be empty after removal from the contents."

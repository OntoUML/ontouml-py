import pytest

from ontouml_py.classes.concrete_classes.package import Package
from ontouml_py.classes.concrete_classes.project import Project


# Fixture for creating a sample project
@pytest.fixture
def sample_project() -> Project:
    return Project()


# Fixture for creating a sample package
@pytest.fixture
def sample_package() -> Package:
    return Package()


def test_validate_root_package_with_valid_package(sample_project: Project, sample_package: Package) -> None:
    """Test validate_root_package method with a valid package that is part of the project.

    :param sample_project: A sample Project instance for testing.
    :param sample_package: A sample Package instance for testing.
    """
    sample_project.add_element(sample_package)
    sample_project.root_package = sample_package
    # No exception should be raised
    assert sample_project, "validate_root_package should pass with a valid package that is part of the project."


def test_validate_root_package_with_invalid_package(sample_project: Project, sample_package: Package) -> None:
    """Test validate_root_package method with a package that is not part of the project.

    :param sample_project: A sample Project instance for testing.
    :param sample_package: A sample Package instance for testing.
    """
    with pytest.raises(ValueError):
        sample_project.root_package = sample_package


def test_validate_root_package_with_none(sample_project: Project) -> None:
    """Test validate_root_package method with None as the root package.

    :param sample_project: A sample Project instance for testing.
    """
    sample_project.root_package = None
    assert sample_project, "No exception should be raised, as None is valid."


def test_validate_root_package_with_incorrect_type(sample_project: Project) -> None:
    """Test validate_root_package method with an object that is not a Package instance.

    :param sample_project: A sample Project instance for testing.
    """
    with pytest.raises(TypeError):
        sample_project.root_package = "NotAPackage"


def test_reset_root_package_to_none(sample_project: Project, sample_package: Package) -> None:
    """Test resetting the root package of a project to None after setting it to a valid package.

    This test ensures that a project's root package can be reset to None after being initially set to a valid package
    that is part of the project's elements.

    :param sample_project: A sample Project instance for testing.
    :param sample_package: A sample Package instance for testing.
    :return: None
    :raises AssertionError: If an error occurs when resetting the root package to None.
    """
    sample_project.add_element(sample_package)
    sample_project.root_package = sample_package
    sample_project.root_package = None
    assert sample_project.root_package is None, "Project's root package should be resettable to None without errors."


def test_reset_root_package_to_valid_package(sample_project: Project, sample_package: Package) -> None:
    """Test resetting the root package of a project to a valid package after setting it to None.

    This test checks if a project's root package can be reset to a valid package that is part of the project's elements
    after being initially set to None.

    :param sample_project: A sample Project instance for testing.
    :param sample_package: A sample Package instance for testing.
    :return: None
    :raises AssertionError: If an error occurs when resetting the root package to a valid package.
    """
    sample_project.add_element(sample_package)
    sample_project.root_package = sample_package
    sample_project.root_package = None
    sample_project.root_package = sample_package
    assert (
        sample_project.root_package == sample_package
    ), "Project's root package should be resettable to a valid package in the project's elements."


def test_project_initialization_with_invalid_root_package(sample_package: Package) -> None:
    """Test the initialization of a Project instance with a root package that is not part of the project.

    :param sample_package: A sample Package instance for testing.
    :return: None
    :raises ValueError: If the Project instance initializes with a root package that is not part of the project.
    """
    with pytest.raises(ValueError):
        Project(root_package=sample_package)


def test_project_initialization_with_none_root_package() -> None:
    """Test the initialization of a Project instance with None as the root package.

    :return: None
    :raises ValueError: If the Project instance does not initialize correctly when root package is None.
    """
    project = Project(root_package=None)
    assert project.root_package is None, "Project should initialize correctly with None as the root package."

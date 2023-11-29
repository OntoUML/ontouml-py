import pytest

from ontouml_py.classes.abstract_classes.projectelement import ProjectElement
from ontouml_py.classes.concrete_classes.project import Project


@pytest.fixture
def sample_project() -> Project:
    """Fixture to create a sample Project instance for testing.

    :return: An instance of Project for testing purposes.
    """
    return Project()


@pytest.fixture
def sample_element() -> ProjectElement:
    """Fixture to create a sample ProjectElement instance for testing.

    :return: An instance of ProjectElement for testing purposes.
    """

    class Diagram(ProjectElement):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    return Diagram()


def test_add_valid_element_to_project(sample_project: Project, sample_element: ProjectElement):
    """Test adding a valid ProjectElement to a Project.

    :param sample_project: A sample Project instance.
    :param sample_element: A sample ProjectElement instance.
    :raises AssertionError: If the element is not added correctly to the project.
    """
    sample_project.add_element(sample_element)
    assert sample_element in sample_project.elements, "ProjectElement should be added to Project's elements"


def test_remove_element_from_project(sample_project: Project, sample_element: ProjectElement):
    """Test removing a ProjectElement from a Project.

    :param sample_project: A sample Project instance.
    :param sample_element: A sample ProjectElement instance.
    :raises AssertionError: If the element is not removed correctly from the project.
    """
    sample_project.add_element(sample_element)
    sample_project.remove_element(sample_element)
    assert sample_project.elements == set(), "ProjectElement should be removed from Project's elements"


def test_add_invalid_element_type_to_project(sample_project: Project):
    """Test adding an invalid type (not a ProjectElement) to a Project.

    :param sample_project: A sample Project instance.
    :raises TypeError: If a non-ProjectElement type is added to the project.
    """
    with pytest.raises(TypeError, match=r".*must be an instance of ProjectElement.*"):
        sample_project.add_element("invalid_element")


def test_remove_nonexistent_element_from_project(sample_project: Project, sample_element: ProjectElement):
    """Test removing a non-existent ProjectElement from a Project.

    :param sample_project: A sample Project instance.
    :param sample_element: A sample ProjectElement instance.
    :raises AssertionError: If the test does not correctly identify the non-existence of the element.
    """
    with pytest.raises(ValueError, match=r".*cannot be removed because is not part of the project.*"):
        sample_project.remove_element(sample_element)

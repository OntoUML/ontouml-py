import pytest
from pytest_lazyfixture import lazy_fixture

from ontouml_py.model.project import Project
from ontouml_py.model.projectelement import ProjectElement


@pytest.mark.parametrize(
    "subclass_fixture",
    [
        lazy_fixture("valid_property"),
        lazy_fixture("valid_binary_relation"),
        lazy_fixture("valid_nary_relation"),
        lazy_fixture("valid_class"),
        lazy_fixture("valid_literal"),
        lazy_fixture("valid_anchor"),
        lazy_fixture("valid_generalization"),
        lazy_fixture("valid_generalization_set"),
        lazy_fixture("valid_note"),
        lazy_fixture("valid_package"),
    ],
)
def test_project_element_initialization_through_subclass(subclass_fixture):
    """Test the initialization of various ProjectElement subclasses.

    :param subclass_fixture: A fixture for a valid subclass instance of ProjectElement.
    """
    assert isinstance(subclass_fixture, ProjectElement)
    assert isinstance(subclass_fixture.project, Project)


@pytest.mark.parametrize(
    "subclass_fixture",
    [
        lazy_fixture("valid_property"),
        lazy_fixture("valid_binary_relation"),
        lazy_fixture("valid_nary_relation"),
        lazy_fixture("valid_class"),
        lazy_fixture("valid_literal"),
        lazy_fixture("valid_anchor"),
        lazy_fixture("valid_generalization"),
        lazy_fixture("valid_generalization_set"),
        lazy_fixture("valid_note"),
        lazy_fixture("valid_package"),
    ],
)
def test_project_attribute_in_project_element_subclass(subclass_fixture):
    """Test the project attribute in various ProjectElement subclasses.

    :param subclass_fixture: A fixture for a valid subclass instance of ProjectElement.
    """
    assert isinstance(subclass_fixture.project, Project)

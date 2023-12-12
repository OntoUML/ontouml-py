from ontouml_py.model.project import Project
from ontouml_py.model.projectelement import ProjectElement

def test_project_element_initialization():
    """Test the initialization of a ProjectElement instance with a Project."""
    project = Project(id="test_project")
    project_element = ProjectElement(project=project)

    assert project_element._project == project, "ProjectElement's _project should be correctly assigned during initialization"

def test_project_element_project_property():
    """Test the project property of ProjectElement."""
    project = Project(id="test_project")
    project_element = ProjectElement(project=project)

    assert project_element.project == project, "ProjectElement's project property should return the correct Project instance"

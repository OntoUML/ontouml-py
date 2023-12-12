from typing import Any

import pytest
from ontouml_py.model.project import Project
from ontouml_py.model.enumerations.ontologyrepresentationstyle import OntologyRepresentationStyle
from ontouml_py.model.package import Package
from ontouml_py.model.projectelement import ProjectElement


def test_project_initialization():
    """Test the initialization of a Project instance with default values."""
    project = Project()

    assert isinstance(project.acronyms, set), "Acronyms should be initialized as a set"
    assert isinstance(project.bibliographic_citations, set), "Bibliographic citations should be initialized as a set"
    assert isinstance(project.keywords, set), "Keywords should be initialized as a set"
    assert isinstance(project.landing_pages, set), "Landing pages should be initialized as a set"
    assert isinstance(project.languages, set), "Languages should be initialized as a set"
    assert project.namespace is None, "Namespace should be None by default"
    assert isinstance(project.sources, set), "Sources should be initialized as a set"
    assert isinstance(project.access_rights, set), "Access rights should be initialized as a set"
    assert isinstance(project.ontology_types, set), "Ontology types should be initialized as a set"
    assert isinstance(project.themes, set), "Themes should be initialized as a set"
    assert project.license is None, "License should be None by default"
    assert isinstance(project.contexts, set), "Contexts should be initialized as a set"
    assert isinstance(project.designed_for_task, set), "Designed for task should be initialized as a set"
    assert project.publisher is None, "Publisher should be None by default"
    assert project.root_package is None, "root_package should be None by default"
    assert project.representation_style == OntologyRepresentationStyle.ONTOUML_STYLE, \
        "Representation style should be ONTOUML_STYLE by default"

def test_project_elements_initialization():
    """Test the initialization of the _elements attribute in a Project instance."""
    project = Project()
    expected_elements = {
        "Anchor", "BinaryRelation", "Class", "Diagram", "Generalization", "GeneralizationSet", "Literal",
        "NaryRelation", "Note", "Package", "Property", "Shape", "View"
    }

    assert set(project._elements.keys()) == expected_elements, \
        "Project should initialize all expected element types in _elements"
    for element_set in project._elements.values():
        assert isinstance(element_set, set), "Each element type in _elements should be a set"

@pytest.mark.parametrize("attribute, value", [
    ("acronyms", {"ACM", "IEEE"}),
    ("bibliographic_citations", {"Citation1", "Citation2"}),
    ("keywords", {"ontology", "modeling"}),
    # Add more parameters as needed for other attributes
])
def test_project_attribute_assignment(attribute: str, value: set):
    """Test the assignment of various set attributes in Project.

    :param attribute: The name of the attribute to test.
    :param value: The value to assign to the attribute.
    """
    project = Project()
    setattr(project, attribute, value)
    assert getattr(project, attribute) == value, f"Project's {attribute} should be assignable and reflect the new value"

def test_project_representation_style_assignment():
    """Test the assignment of the representation_style attribute in Project."""
    project = Project()
    new_style = OntologyRepresentationStyle.UFO_STYLE
    project.representation_style = new_style
    assert project.representation_style == new_style, "Project's representation_style should be assignable"

def test_project_namespace_assignment():
    """Test the assignment of the namespace attribute in Project."""
    project = Project()
    namespace = "http://example.org/ontology"
    project.namespace = namespace
    assert project.namespace == namespace, "Project's namespace should be assignable"

@pytest.mark.parametrize("attribute, value", [
    ("namespace", "http://newexample.org/ontology"),
    ("license", "MIT License"),
    ("publisher", "Example Publisher"),
])
def test_project_optional_attribute_assignment(attribute: str, value: str):
    """Test the assignment of various optional attributes in Project.

    :param attribute: The name of the attribute to test.
    :param value: The value to assign to the attribute.
    """
    project = Project()
    setattr(project, attribute, value)
    assert getattr(project, attribute) == value, f"Project's {attribute} should be assignable and reflect the new value"

@pytest.mark.parametrize("element_type", [
    "Anchor", "BinaryRelation", "Class", "Diagram", "Generalization", "GeneralizationSet", "Literal",
    "NaryRelation", "Note", "Package", "Property", "Shape", "View"
])
def test_project_elements_type_check(element_type: str):
    """Test the type of elements stored in the _elements dictionary of Project.

    :param element_type: The type of element to test.
    """
    project = Project()
    element_set = project._elements[element_type]
    assert all(isinstance(element, ProjectElement) for element in element_set), \
        f"All elements in _elements['{element_type}'] should be instances of ProjectElement"


import pytest

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.class_ontouml import Class
from ontouml_py.model.generalization import Generalization
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.literal import Literal
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.package import Package
from ontouml_py.model.project import Project
from ontouml_py.model.property import Property
from ontouml_py.representation.diagram import Diagram


# Test for ProjectMethodsMixin's get_anchors method
def test_get_anchors(valid_project: Project, valid_anchor: Anchor):
    """
    Test the get_anchors method.

    :param valid_project: A valid Project instance.
    :param valid_anchor: A valid Anchor instance.
    :return: None
    """
    valid_project._elements["Anchor"].add(valid_anchor)
    anchors = valid_project.get_anchors()
    assert valid_anchor in anchors, "get_anchors should return the added anchor"


# Test for ProjectMethodsMixin's get_binary_relations method
def test_get_binary_relations(valid_project: Project, valid_binary_relation: BinaryRelation):
    """
    Test the get_binary_relations method.

    :param valid_project: A valid Project instance.
    :param valid_binary_relation: A valid BinaryRelation instance.
    :return: None
    """
    valid_project._elements["BinaryRelation"].add(valid_binary_relation)
    binary_relations = valid_project.get_binary_relations()
    assert valid_binary_relation in binary_relations, "get_binary_relations should return the added binary relation"


# Test for ProjectMethodsMixin's get_classes method
def test_get_classes(valid_project: Project, valid_class: Class):
    """
    Test the get_classes method.

    :param valid_project: A valid Project instance.
    :param valid_class: A valid Class instance.
    :return: None
    """
    valid_project._elements["Class"].add(valid_class)
    classes = valid_project.get_classes()
    assert valid_class in classes, "get_classes should return the added class"


# Test for ProjectMethodsMixin's get_diagrams method
def test_get_diagrams(valid_project: Project):
    """
    Test the get_diagrams method.

    :param valid_project: A valid Project instance.
    :return: None
    """
    diagram = Diagram(valid_project)
    valid_project._elements["Diagram"].add(diagram)
    diagrams = valid_project.get_diagrams()
    assert diagram in diagrams, "get_diagrams should return the added diagram"


# Test for ProjectMethodsMixin's get_generalizations method
def test_get_generalizations(valid_project: Project, valid_generalization: Generalization):
    """
    Test the get_generalizations method.

    :param valid_project: A valid Project instance.
    :param valid_generalization: A valid Generalization instance.
    :return: None
    """
    valid_project._elements["Generalization"].add(valid_generalization)
    generalizations = valid_project.get_generalizations()
    assert valid_generalization in generalizations, "get_generalizations should return the added generalization"


# Test for ProjectMethodsMixin's get_generalization_sets method
def test_get_generalization_sets(valid_project: Project, valid_generalization_set: GeneralizationSet):
    """
    Test the get_generalization_sets method.

    :param valid_project: A valid Project instance.
    :param valid_generalization_set: A valid GeneralizationSet instance.
    :return: None
    """
    valid_project._elements["GeneralizationSet"].add(valid_generalization_set)
    generalization_sets = valid_project.get_generalization_sets()
    assert (
        valid_generalization_set in generalization_sets
    ), "get_generalization_sets should return the added generalization set"


# Test for ProjectMethodsMixin's get_literals method
def test_get_literals(valid_project: Project, valid_literal: Literal):
    """
    Test the get_literals method.

    :param valid_project: A valid Project instance.
    :param valid_literal: A valid Literal instance.
    :return: None
    """
    valid_project._elements["Literal"].add(valid_literal)
    literals = valid_project.get_literals()
    assert valid_literal in literals, "get_literals should return the added literal"


# Test for ProjectMethodsMixin's get_nary_relations method
def test_get_nary_relations(valid_project: Project, valid_nary_relation: NaryRelation):
    """
    Test the get_nary_relations method.

    :param valid_project: A valid Project instance.
    :param valid_nary_relation: A valid NaryRelation instance.
    :return: None
    """
    valid_project._elements["NaryRelation"].add(valid_nary_relation)
    nary_relations = valid_project.get_nary_relations()
    assert valid_nary_relation in nary_relations, "get_nary_relations should return the added nary relation"


# Test for ProjectMethodsMixin's get_notes method
def test_get_notes(valid_project: Project, valid_note: Note):
    """
    Test the get_notes method.

    :param valid_project: A valid Project instance.
    :param valid_note: A valid Note instance.
    :return: None
    """
    valid_project._elements["Note"].add(valid_note)
    notes = valid_project.get_notes()
    assert valid_note in notes, "get_notes should return the added note"


# Test for ProjectMethodsMixin's get_packages method
def test_get_packages(valid_project: Project, valid_package: Package):
    """
    Test the get_packages method.

    :param valid_project: A valid Project instance.
    :param valid_package: A valid Package instance.
    :return: None
    """
    valid_project._elements["Package"].add(valid_package)
    packages = valid_project.get_packages()
    assert valid_package in packages, "get_packages should return the added package"


# Test for ProjectMethodsMixin's get_properties method
def test_get_properties(valid_project: Project, valid_property: Property):
    """
    Test the get_properties method.

    :param valid_project: A valid Project instance.
    :param valid_property: A valid Property instance.
    :return: None
    """
    valid_project._elements["Property"].add(valid_property)
    properties = valid_project.get_properties()
    assert valid_property in properties, "get_properties should return the added property"


# Test for ProjectMethodsMixin's get_element_by_id method
@pytest.mark.parametrize(
    "element_type,fixture_name",
    [
        ("Anchor", "valid_anchor"),
        ("BinaryRelation", "valid_binary_relation"),
        ("Class", "valid_class"),
        ("Generalization", "valid_generalization"),
        ("GeneralizationSet", "valid_generalization_set"),
        ("Literal", "valid_literal"),
        ("NaryRelation", "valid_nary_relation"),
        ("Note", "valid_note"),
        ("Package", "valid_package"),
        ("Property", "valid_property"),
    ],
)
def test_get_element_by_id(valid_project: Project, request, element_type: str, fixture_name: str):
    """
    Test the get_element_by_id method for different element types.

    :param valid_project: A valid Project instance.
    :param request: Pytest fixture request object.
    :param element_type: The type of the element.
    :param fixture_name: The name of the fixture to use.
    :return: None
    """
    element = request.getfixturevalue(fixture_name)
    valid_project._elements[element_type].add(element)
    retrieved_element = valid_project.get_element_by_id(element_type, element.id)
    assert retrieved_element == element, f"get_element_by_id should return the added {element_type}"


@pytest.mark.parametrize(
    "creation_method_name,element_class,additional_args",
    [
        ("create_anchor", Anchor, {"note": "valid_note", "target": "valid_note"}),
        ("create_binary_relation", BinaryRelation, {}),
        ("create_class", Class, {}),
        ("create_diagram", Diagram, {}),
        ("create_generalization", Generalization, {"general": "valid_class", "specific": "valid_class"}),
        ("create_generalization_set", GeneralizationSet, {}),
        ("create_nary_relation", NaryRelation, {}),
        ("create_note", Note, {}),
        ("create_package", Package, {}),
        # Add specific creation methods for different class stereotypes
        ("create_class_abstract", Class, {}),
        ("create_class_category", Class, {}),
        ("create_class_collective", Class, {}),
        ("create_class_datatype", Class, {}),
        ("create_class_enumeration", Class, {}),
        ("create_class_event", Class, {}),
        ("create_class_historical_role", Class, {}),
        ("create_class_historical_role_mixin", Class, {}),
        ("create_class_kind", Class, {}),
        ("create_class_mixin", Class, {}),
        ("create_class_mode", Class, {}),
        ("create_class_phase", Class, {}),
        ("create_class_phase_mixin", Class, {}),
        ("create_class_quality", Class, {}),
        ("create_class_quantity", Class, {}),
        ("create_class_relator", Class, {}),
        ("create_class_role", Class, {}),
        ("create_class_role_mixin", Class, {}),
        ("create_class_situation", Class, {}),
        ("create_class_subkind", Class, {}),
        ("create_class_type", Class, {}),
        # Add other specific creation methods if any
    ],
)
def test_element_creation_methods(
    valid_project: Project, request, creation_method_name: str, element_class, additional_args: dict
):
    """
    Test the element creation methods.

    :param valid_project: A valid Project instance.
    :param request: Pytest fixture request object.
    :param creation_method_name: The name of the creation method of the project.
    :param element_class: The class of the element to be created.
    :param additional_args: Additional arguments required for creating the element.
    :return: None
    """
    # Resolve additional arguments using fixtures
    resolved_args = {
        key: request.getfixturevalue(value) if isinstance(value, str) else value
        for key, value in additional_args.items()
    }

    creation_method = getattr(valid_project, creation_method_name)
    element = creation_method(**resolved_args)

    assert isinstance(
        element, element_class
    ), f"{creation_method_name} should create an instance of {element_class.__name__}"
    assert (
        element in valid_project._elements[element_class.__name__]
    ), f"{creation_method_name} should add the created element to the project"

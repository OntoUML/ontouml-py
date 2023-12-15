import pytest
from pydantic import ValidationError

from ontouml_py.model.class_ontouml import Class
from ontouml_py.model.enumerations.classstereotype import ClassStereotype
from ontouml_py.model.enumerations.ontologicalnature import OntologicalNature
from ontouml_py.model.literal import Literal
from ontouml_py.model.project import Project


def test_class_initialization(valid_project: Project):
    """
    Test the initialization of a Class instance.

    :param valid_project: A valid instance of Project.
    """
    test_class = Class(
        project=valid_project,
        is_powertype=True,
        order=2,
        restricted_to={OntologicalNature.FUNCTIONAL_COMPLEX_NATURE},
        stereotype=ClassStereotype.KIND,
    )
    assert test_class.is_powertype, "is_powertype should be initialized correctly."
    assert test_class.order == 2, "order should be initialized correctly."
    assert test_class.restricted_to == {
        OntologicalNature.FUNCTIONAL_COMPLEX_NATURE
    }, "restricted_to should be initialized correctly."
    assert test_class.stereotype == ClassStereotype.KIND, "stereotype should be initialized correctly."


def test_class_default_values(valid_project: Project):
    """
    Test the default values of a Class instance.

    :param valid_project: A valid instance of Project.
    """
    test_class = Class(project=valid_project)
    assert test_class.is_powertype is False, "Default value of is_powertype should be False."
    assert test_class.order == 1, "Default value of order should be '1'."
    assert test_class.restricted_to == set(), "Default value of restricted_to should be an empty set."
    assert test_class.stereotype is None, "Default value of stereotype should be None."


@pytest.mark.parametrize(
    "invalid_value, attribute",
    [
        (123, "is_powertype"),
        (1.5, "order"),
        ({123}, "restricted_to"),
        (1.5, "stereotype"),
    ],
)
def test_class_invalid_attribute_types(valid_project: Project, invalid_value, attribute):
    """
    Test invalid types for Class attributes.

    :param valid_project: A valid instance of Project.
    :param invalid_value: An invalid value for the attribute.
    :param attribute: The name of the attribute to test.
    """
    with pytest.raises(ValidationError, match="Input should be"):
        Class(project=valid_project, **{attribute: invalid_value})


@pytest.mark.parametrize(
    "invalid_value, attribute",
    [
        (1.5, "order"),
        (False, "restricted_to"),
        (True, "stereotype"),
    ],
)
def test_class_invalid_attribute_values(valid_project: Project, invalid_value, attribute):
    """
    Test invalid values for Class attributes.

    :param valid_project: A valid instance of Project.
    :param invalid_value: An invalid value for the attribute.
    :param attribute: The name of the attribute to test.
    """
    with pytest.raises(ValidationError, match="Input should be a valid"):
        Class(project=valid_project, **{attribute: invalid_value})


def test_add_literal_valid(valid_class: Class):
    """
    Test adding a valid literal to a class.

    :param valid_class: A valid instance of Class.
    :param valid_literal: A valid instance of Literal.
    """
    test_class = valid_class

    new_literal = test_class.create_literal()

    assert new_literal in test_class._literals, "The literal should be added to the class."


def test_delete_literal(valid_class: Class):
    assert valid_class.literals == set()
    new_literal = valid_class.create_literal()
    assert valid_class.literals == {new_literal}
    valid_class.delete_literal(new_literal)
    assert valid_class.literals == set()


def test_class_attribute_modification(valid_class: Class):
    """
    Test modifying attributes of a Class instance.

    :param valid_class: A valid instance of Class.
    """
    valid_class.is_powertype = True
    valid_class.order = "2"
    valid_class.restricted_to = {OntologicalNature.TYPE_NATURE}
    valid_class.stereotype = ClassStereotype.TYPE

    assert valid_class.is_powertype is True, "is_powertype should be modifiable."
    assert valid_class.order == "2", "order should be modifiable."
    assert valid_class.restricted_to == {OntologicalNature.TYPE_NATURE}, "restricted_to should be modifiable."
    assert valid_class.stereotype == ClassStereotype.TYPE, "stereotype should be modifiable."


def test_class_empty_and_null_values(valid_project: Project):
    """
    Test the behavior of Class with empty and null values for optional fields.

    :param valid_project: A valid instance of Project.
    """
    test_class = Class(project=valid_project, stereotype=None)
    assert test_class.stereotype is None, "stereotype should accept None as a valid value."

    test_class.stereotype = ClassStereotype.KIND
    test_class.stereotype = None
    assert test_class.stereotype is None, "stereotype should be settable to None after initialization."

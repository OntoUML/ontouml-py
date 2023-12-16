import pytest
from pydantic import ValidationError

from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.project import Project

import sys

# Assuming the necessary imports are already in place


def test_binary_relation_initialization(valid_project):
    """Test successful initialization of a BinaryRelation instance.

    :param valid_project: A fixture that provides a valid Project instance.
    """
    binary_relation = BinaryRelation(valid_project)
    assert binary_relation.project == valid_project, "BinaryRelation should be initialized with the correct project"


def test_binary_relation_initialization_with_invalid_project():
    """Test BinaryRelation initialization with an invalid project.

    :raises TypeError: If the project is not a valid Project instance.
    """
    with pytest.raises(AttributeError, match="'str' object has no attribute '_elements'"):
        BinaryRelation(project="not_a_project")


def test_binary_relation_initialization_with_extra_fields(valid_project):
    """Test BinaryRelation initialization fails with extra fields.

    :param valid_project: A fixture that provides a valid Project instance.
    :raises ValidationError: If extra fields are provided.
    """
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        BinaryRelation(valid_project, extra_field="extra_value")


def test_binary_relation_post_initialization_with_extra_fields(valid_project):
    """Test BinaryRelation post_initialization fails with extra fields.

    :param valid_project: A fixture that provides a valid Project instance.
    :raises ValidationError: If extra fields are provided.
    """
    bn = BinaryRelation(valid_project)

    with pytest.raises(ValidationError, match="Object has no attribute 'extra'"):
        bn.extra = "extra_value"


def test_binary_relation_attribute_assignment_post_initialization(valid_binary_relation, valid_project):
    """Test forbidden attribute assignment for a BinaryRelation instance after its initialization.

    :param valid_binary_relation: A fixture that provides a valid BinaryRelation instance.
    :param valid_project: A fixture that provides a valid Project instance.
    """
    new_project = Project()
    python_minor_version = sys.version_info.minor
    if python_minor_version > 10:
        match_string = "property 'project' of 'BinaryRelation' object has no setter"
    else:
        match_string = "can't set attribute"
    with pytest.raises(AttributeError, match=match_string):
        valid_binary_relation.project = new_project


def test_binary_relation_retrieval_by_id(valid_project, valid_binary_relation):
    """Test retrieval of a BinaryRelation instance from a Project by its ID.

    :param valid_project: A fixture that provides a valid Project instance.
    :param valid_binary_relation: A fixture that provides a valid BinaryRelation instance.
    """
    retrieved_binary_relation = valid_project.get_element_by_id("BinaryRelation", valid_binary_relation.id)
    assert (
        retrieved_binary_relation == valid_binary_relation
    ), "Should retrieve the same BinaryRelation instance from the project"


def test_binary_relation_type_validation_for_attributes(valid_project):
    """Test type validation for BinaryRelation attributes.

    :param valid_project: A fixture that provides a valid Project instance.
    :raises TypeError: If an attribute is assigned an incorrect type.
    """
    binary_relation = BinaryRelation(valid_project)
    with pytest.raises(ValidationError, match="Object has no attribute 'some_attribute'"):
        binary_relation.some_attribute = "incorrect_type"

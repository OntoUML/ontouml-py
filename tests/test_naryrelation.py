import sys

import pytest
from pydantic import ValidationError

from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.project import Project


# Assuming the necessary imports are already in place


def test_nary_relation_initialization(valid_project):
    """Test successful initialization of a NaryRelation instance.

    :param valid_project: A fixture that provides a valid Project instance.
    """
    nary_relation = NaryRelation(valid_project)
    assert nary_relation.project == valid_project, "NaryRelation should be initialized with the correct project"


def test_nary_relation_initialization_with_invalid_project():
    """Test NaryRelation initialization with an invalid project.

    :raises TypeError: If the project is not a valid Project instance.
    """
    with pytest.raises(AttributeError, match="'str' object has no attribute '_elements'"):
        NaryRelation(project="not_a_project")


def test_nary_relation_initialization_with_extra_fields(valid_project):
    """Test NaryRelation initialization fails with extra fields.

    :param valid_project: A fixture that provides a valid Project instance.
    :raises ValidationError: If extra fields are provided.
    """
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        NaryRelation(valid_project, extra_field="extra_value")


def test_nary_relation_post_initialization_with_extra_fields(valid_project):
    """Test NaryRelation post_initialization fails with extra fields.

    :param valid_project: A fixture that provides a valid Project instance.
    :raises ValidationError: If extra fields are provided.
    """
    bn = NaryRelation(valid_project)

    with pytest.raises(ValidationError, match="Object has no attribute 'extra'"):
        bn.extra = "extra_value"


def test_nary_relation_attribute_assignment_post_initialization(valid_nary_relation, valid_project):
    """Test forbidden attribute assignment for a NaryRelation instance after its initialization.

    :param valid_nary_relation: A fixture that provides a valid NaryRelation instance.
    :param valid_project: A fixture that provides a valid Project instance.
    """
    new_project = Project()
    python_minor_version = sys.version_info.minor
    if python_minor_version > 10:
        match_string = "property 'project' of 'NaryRelation' object has no setter"
    else:
        match_string = "can't set attribute 'project'"
    with pytest.raises(AttributeError, match=match_string):
        valid_nary_relation.project = new_project


def test_nary_relation_retrieval_by_id(valid_project, valid_nary_relation):
    """Test retrieval of a NaryRelation instance from a Project by its ID.

    :param valid_project: A fixture that provides a valid Project instance.
    :param valid_nary_relation: A fixture that provides a valid NaryRelation instance.
    """
    retrieved_nary_relation = valid_project.get_element_by_id("NaryRelation", valid_nary_relation.id)
    assert (
        retrieved_nary_relation == valid_nary_relation
    ), "Should retrieve the same NaryRelation instance from the project"


def test_nary_relation_type_validation_for_attributes(valid_project):
    """Test type validation for NaryRelation attributes.

    :param valid_project: A fixture that provides a valid Project instance.
    :raises TypeError: If an attribute is assigned an incorrect type.
    """
    nary_relation = NaryRelation(valid_project)
    with pytest.raises(ValidationError, match="Object has no attribute 'some_attribute'"):
        nary_relation.some_attribute = "incorrect_type"

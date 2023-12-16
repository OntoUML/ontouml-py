import pytest
from pytest_lazyfixture import lazy_fixture

from ontouml_py.model.enumerations.relationstereotype import RelationStereotype
from ontouml_py.model.relation import Relation


@pytest.mark.parametrize(
    "relation_fixture, expected_stereotype",
    [(lazy_fixture("valid_binary_relation"), None), (lazy_fixture("valid_nary_relation"), None)],
)
def test_relation_initialization_through_subclass(relation_fixture, expected_stereotype):
    """Test the initialization of Relation subclasses.

    :param relation_fixture: A fixture for a subclass instance of Relation.
    :param expected_stereotype: The expected default value of the stereotype attribute.
    """
    assert isinstance(relation_fixture, Relation)
    assert relation_fixture.stereotype == expected_stereotype


@pytest.mark.parametrize(
    "relation_fixture, stereotype_value",
    [
        (lazy_fixture("valid_binary_relation"), RelationStereotype.CREATION),
        (lazy_fixture("valid_nary_relation"), RelationStereotype.COMPARATIVE),
    ],
)
def test_stereotype_attribute_in_relation_subclass(relation_fixture, stereotype_value):
    """Test the stereotype attribute in Relation subclasses.

    :param relation_fixture: A fixture for a subclass instance of Relation.
    :param stereotype_value: A value to assign to the stereotype attribute.
    """
    relation_fixture.stereotype = stereotype_value
    assert relation_fixture.stereotype == stereotype_value

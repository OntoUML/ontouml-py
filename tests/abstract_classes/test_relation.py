import pytest

from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.enumerations.relationstereotype import RelationStereotype
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.relation import Relation


def test_relation_initialization_with_valid_stereotype() -> None:
    """Test the initialization of a Relation subclass with a valid stereotype."""

    class BinaryRelation(Relation):
        def __init__(self, **data):
            super().__init__(**data)

    relation = BinaryRelation(stereotype=RelationStereotype.MATERIAL)
    assert (
        relation.stereotype == RelationStereotype.MATERIAL
    ), "Relation should be initialized with the specified stereotype"


def test_relation_initialization_with_invalid_stereotype() -> None:
    """Test the initialization of a Relation subclass with an invalid stereotype."""

    class BinaryRelation(Relation):
        def __init__(self, **data):
            super().__init__(**data)

    with pytest.raises(ValueError):
        BinaryRelation(stereotype="invalid_stereotype")


def test_relation_subclass_validation() -> None:
    """Test the validation of allowed subclasses for Relation."""

    class InvalidRelation(Relation):
        def __init__(self, **data):
            super().__init__(**data)

    with pytest.raises(ValueError):
        InvalidRelation()


def test_binary_relation_as_valid_subclass() -> None:
    """Test that BinaryRelation is a valid subclass of Relation."""
    binary_relation = BinaryRelation()
    assert isinstance(binary_relation, Relation), "BinaryRelation should be a valid subclass of Relation"


def test_nary_relation_as_valid_subclass() -> None:
    """Test that NaryRelation is a valid subclass of Relation."""
    nary_relation = NaryRelation()
    assert isinstance(nary_relation, Relation), "NaryRelation should be a valid subclass of Relation"


def test_relation_default_values() -> None:
    """Test the default values of attributes in the Relation class."""

    class BinaryRelation(Relation):
        def __init__(self, **data):
            super().__init__(**data)

    relation = BinaryRelation()
    assert relation.stereotype is None, "Default value of stereotype should be None"


def test_relation_attribute_assignment() -> None:
    """Test attribute assignment in the Relation class."""

    class BinaryRelation(Relation):
        def __init__(self, **data):
            super().__init__(**data)

    relation = BinaryRelation()
    relation.stereotype = RelationStereotype.MATERIAL
    assert relation.stereotype == RelationStereotype.MATERIAL, "Stereotype should be assignable in Relation class"


def test_relation_initialization_with_each_stereotype() -> None:
    """Test the initialization of a Relation subclass with each stereotype in RelationStereotype."""

    class BinaryRelation(Relation):
        def __init__(self, **data):
            super().__init__(**data)

    for stereotype in RelationStereotype:
        relation = BinaryRelation(stereotype=stereotype)
        assert relation.stereotype == stereotype, f"Relation should be initialized with the stereotype {stereotype}"


def test_relation_initialization_with_incorrect_type_for_stereotype() -> None:
    """Test the initialization of a Relation subclass with incorrect type for stereotype."""

    class BinaryRelation(Relation):
        def __init__(self, **data):
            super().__init__(**data)

    with pytest.raises(ValueError):
        BinaryRelation(stereotype=123)  # Using an integer instead of a RelationStereotype member

    with pytest.raises(ValueError):
        BinaryRelation(stereotype="non_existent_stereotype")  # Using a non-existent stereotype string

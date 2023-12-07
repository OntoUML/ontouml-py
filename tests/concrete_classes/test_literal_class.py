import pytest
from pydantic import ValidationError

from ontouml_py.classes.concrete_classes.class_py import Class
from ontouml_py.classes.concrete_classes.literal import Literal
from ontouml_py.classes.enumerations.classstereotype import ClassStereotype


@pytest.fixture
def enumeration_class() -> Class:
    """Fixture to create an enumeration class instance."""
    return Class(stereotype=ClassStereotype.ENUMERATION, literals={Literal(), Literal()})


@pytest.fixture
def non_enumeration_class() -> Class:
    """Fixture to create a non-enumeration class instance."""
    return Class(stereotype=ClassStereotype.KIND)


def test_enumeration_class_with_literals(enumeration_class: Class) -> None:
    """Test that an enumeration class can have literals.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    assert len(enumeration_class.literals) > 0, "Enumeration class should be able to have literals."


def test_non_enumeration_class_without_literals(non_enumeration_class: Class) -> None:
    """Test that a non-enumeration class cannot have literals.

    :param non_enumeration_class: A fixture providing a non-enumeration class instance.
    """
    assert not non_enumeration_class.literals, "Non-enumeration class should not have literals."


def test_enumeration_class_requires_at_least_one_literal() -> None:
    """Test that an enumeration class requires at least one literal."""
    with pytest.raises(ValueError):
        Class(stereotype=ClassStereotype.ENUMERATION, literals=set())


def test_non_enumeration_class_cannot_have_literals() -> None:
    """Test that a non-enumeration class cannot have literals."""
    with pytest.raises(ValueError):
        Class(stereotype=ClassStereotype.KIND, literals={Literal()})


def test_add_literal_to_enumeration_class(enumeration_class: Class) -> None:
    """Test adding a literal to an enumeration class.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    new_literal = Literal()
    enumeration_class.literals.add(new_literal)
    assert new_literal in enumeration_class.literals, "New literal should be added to the enumeration class."


def test_remove_literal_from_enumeration_class(enumeration_class: Class) -> None:
    """Test removing a literal from an enumeration class.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    literal_to_remove = next(iter(enumeration_class.literals))
    enumeration_class.literals.remove(literal_to_remove)
    assert literal_to_remove not in enumeration_class.literals, "Literal should be removed from the enumeration class."


def test_enumeration_class_initialization_with_literals() -> None:
    """Test the initialization of an enumeration class with literals."""
    literals = {Literal(), Literal()}
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION, literals=literals)
    assert set(enumeration_class.literals) == literals, "Enumeration class should initialize with provided literals."


def test_enumeration_class_initialization_without_literals_fails() -> None:
    """Test that initializing an enumeration class without literals raises an error."""
    with pytest.raises(ValueError):
        Class(stereotype=ClassStereotype.ENUMERATION)


# Ideally, this test should work. However I could not implement it yet.
# def test_adding_literal_to_non_enumeration_class_fails(non_enumeration_class: Class) -> None:
#     """Test that adding a literal to a non-enumeration class raises an error.
#
#     :param non_enumeration_class: A fixture providing a non-enumeration class instance.
#     """
#     new_literal = Literal()
#     with pytest.raises(ValueError):
#         non_enumeration_class.add_literal(new_literal)


def test_removing_all_literals_from_enumeration_class_fails(enumeration_class: Class) -> None:
    """Test that removing all literals from an enumeration class raises an error.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    with pytest.raises(ValueError):
        enumeration_class.literals.clear()


def test_updating_literals_in_enumeration_class(enumeration_class: Class) -> None:
    """Test updating literals in an enumeration class.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    new_literals = {Literal(), Literal()}
    enumeration_class.literals = new_literals
    assert set(enumeration_class.literals) == new_literals, "Enumeration class literals should be updatable."


def test_add_literal_method_with_valid_literal(enumeration_class: Class) -> None:
    """Test adding a literal to an enumeration class using the add_literal method.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    new_literal = Literal()
    enumeration_class.add_literal(new_literal)
    assert new_literal in enumeration_class.literals, "add_literal should successfully add a new literal."


def test_add_literal_method_with_invalid_type(enumeration_class: Class) -> None:
    """Test adding a non-literal object using the add_literal method raises an error.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    with pytest.raises(ValueError):
        enumeration_class.add_literal("not_a_literal")


def test_remove_literal_method_with_valid_literal(enumeration_class: Class) -> None:
    """Test removing a literal from an enumeration class using the remove_literal method.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    literal_to_remove = next(iter(enumeration_class.literals))
    enumeration_class.remove_literal(literal_to_remove)
    assert literal_to_remove not in enumeration_class.literals, "remove_literal should successfully remove a literal."


def test_remove_literal_method_with_invalid_literal(enumeration_class: Class) -> None:
    """Test removing a non-existent literal using the remove_literal method should raise an error.

    :param enumeration_class: A fixture providing an enumeration class instance.
    """
    non_existent_literal = Literal()
    with pytest.raises(ValueError):
        enumeration_class.remove_literal(non_existent_literal)


def test_initialization_with_invalid_literal_type_raises_error() -> None:
    """Test that initializing a class with a non-literal in the literals set raises an error."""
    with pytest.raises(ValidationError):
        Class(stereotype=ClassStereotype.ENUMERATION, literals={"not_a_literal"})


def test_enumeration_class_with_duplicate_literals() -> None:
    """Test that initializing an enumeration class with duplicate literals does not raise an error."""
    literal = Literal()
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION, literals={literal, literal})
    assert len(enumeration_class.literals) == 1, "Enumeration class should handle duplicate literals gracefully."

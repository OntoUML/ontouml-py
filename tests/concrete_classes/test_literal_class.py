import pytest
from icecream import ic

from ontouml_py.classes.concrete_classes.literal import Literal
from ontouml_py.classes.concrete_classes.class_py import Class
from ontouml_py.classes.enumerations.classstereotype import ClassStereotype


def test_add_literal_to_enumeration_class() -> None:
    """Test adding a literal to a class with Enumeration stereotype."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()

    enumeration_class.add_literal(literal)

    assert literal in enumeration_class.literals, "Literal should be added to the class's literals set."


def test_add_literal_to_non_enumeration_class_raises_error() -> None:
    """Test adding a literal to a class without Enumeration stereotype raises TypeError."""
    non_enumeration_class = Class(stereotype=ClassStereotype.KIND)
    literal = Literal()

    with pytest.raises(TypeError) as excinfo:
        non_enumeration_class.add_literal(literal)

    assert "Literals can only be added to classes stereotyped with ClassStereotype.ENUMERATION" in str(excinfo.value)


def test_remove_literal_from_enumeration_class() -> None:
    """Test removing a literal from a class with Enumeration stereotype."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()
    ic(enumeration_class.literals)
    enumeration_class.add_literal(literal)
    ic(enumeration_class.literals)
    enumeration_class.remove_literal(literal)
    ic(enumeration_class.literals)

    assert literal not in enumeration_class.literals, "Literal should be removed from the class's literals set."


def test_remove_literal_not_in_class_raises_error() -> None:
    """Test removing a literal not in the class raises ValueError."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()

    with pytest.raises(ValueError) as excinfo:
        enumeration_class.remove_literal(literal)

    assert "cannot be removed because is not part of the class" in str(excinfo.value)


def test_remove_literal_from_non_enumeration_class_raises_error() -> None:
    """Test removing a literal from a class without Enumeration stereotype raises TypeError."""
    non_enumeration_class = Class(stereotype=ClassStereotype.KIND)
    literal = Literal()

    with pytest.raises(TypeError) as excinfo:
        non_enumeration_class.remove_literal(literal)

    assert "Literals can only be removed from classes stereotyped with ClassStereotype.ENUMERATION" in str(
        excinfo.value
    )


def test_literal_in_class_property() -> None:
    """Test the in_class property of Literal reflects the correct Class instance."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()
    enumeration_class.add_literal(literal)

    assert literal.in_class == enumeration_class, "Literal's in_class property should reference the containing class."


def test_literal_set_in_class_internal_method() -> None:
    """Test the internal method __set_in_class correctly sets the class of a Literal."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()
    literal._Literal__set_in_class(enumeration_class)

    assert literal.in_class == enumeration_class, "Literal's in_class should be set to the given class."


def test_adding_literal_sets_in_class_correctly() -> None:
    """Test adding a literal to a class sets the literal's in_class property correctly."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()
    enumeration_class.add_literal(literal)

    assert (
        literal.in_class == enumeration_class
    ), "Literal's in_class property should be set to the class it was added to."


def test_removing_literal_unsets_in_class_correctly() -> None:
    """Test removing a literal from a class unsets the literal's in_class property correctly."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()
    enumeration_class.add_literal(literal)
    enumeration_class.remove_literal(literal)

    assert literal.in_class is None, "Literal's in_class property should be None after being removed from the class."


def test_adding_same_literal_multiple_times() -> None:
    """Test adding the same literal multiple times to a class only adds it once."""
    enumeration_class = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()
    enumeration_class.add_literal(literal)
    enumeration_class.add_literal(literal)

    assert len(enumeration_class.literals) == 1, "Class should only contain one instance of the literal."


def test_adding_literal_to_multiple_classes() -> None:
    """Test adding a literal to multiple classes and verify its in_class property."""
    class1 = Class(stereotype=ClassStereotype.ENUMERATION)
    class2 = Class(stereotype=ClassStereotype.ENUMERATION)
    literal = Literal()
    class1.add_literal(literal)
    class2.add_literal(literal)

    assert literal.in_class == class2, "Literal's in_class property should be set to the last class it was added to."

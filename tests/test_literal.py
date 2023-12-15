import pytest
from icecream import ic
from pydantic import ValidationError

from ontouml_py.model.literal import Literal


def test_literal_initialization_with_valid_class(valid_class):
    """
    Test the initialization of a Literal with a valid Class instance.

    :param valid_class: A fixture providing a valid Class instance.
    """
    literal = Literal(enumeration=valid_class)
    assert literal.enumeration == valid_class, "Literal should be initialized with the provided Class instance."


def test_literal_initialization_with_invalid_class(valid_project):
    """
    Test the initialization of a Literal with an invalid type for 'enumeration'.

    :param valid_project: A fixture providing a valid Project instance.
    """
    with pytest.raises(AttributeError, match="object has no attribute"):
        Literal(enumeration=valid_project)


def test_literal_enumeration_property(valid_class, valid_literal):
    """
    Test the 'enumeration' property of the Literal class.

    :param valid_class: A fixture providing a valid Class instance.
    :param valid_literal: A fixture providing a valid Literal instance.
    """
    assert valid_literal.enumeration == valid_class, "The 'enumeration' property should return the associated Class."


import pytest

from src.classes.enumerations.utils_enumerations import enum_literal_to_camel_case


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("THIS_IS_A_TEST", "ThisIsATest"),
        ("SINGLE", "Single"),
        ("MULTIPLE_UNDERSCORES____HERE", "MultipleUnderscoresHere"),
        ("ALREADYCAMCASE", "Alreadycamcase"),
        ("123_NUMBERS", "123Numbers"),
        ("SPECIAL$_CHARS", "Special$Chars"),
    ],
)
def test_enum_literal_to_camel_case(input_str: str, expected: str):
    """
    Test the enum_literal_to_camel_case function with various inputs.

    :param input_str: The input string in uppercase with underscores.
    :param expected: The expected CamelCase output.
    :return: None. Asserts if the output matches the expected result.
    """
    assert (
        enum_literal_to_camel_case(input_str) == expected
    ), f"Expected {expected} from {input_str}, but got {enum_literal_to_camel_case(input_str)}"


@pytest.mark.parametrize(
    "input_str",
    [
        "",
        "Alreadycamcase",
        "AlreadyCamCase",
        "MIXED_case_INPUT",
    ],
)
def test_enum_literal_to_camel_case_negative(input_str: str):
    """
    Test the enum_literal_to_camel_case function with various inputs.

    :param input_str: The input string in uppercase with underscores.
    :return: None. Asserts if the output matches the expected result.
    """
    with pytest.raises(ValueError) as e:
        enum_literal_to_camel_case(input_str)
    print(f"Error: {e}")


def test_enum_literal_to_camel_case_with_non_string_input():
    """
    Test the enum_literal_to_camel_case function with a non-string input.

    :raises TypeError: If the input is not a string.
    """
    with pytest.raises(AttributeError):
        enum_literal_to_camel_case(123)


def test_enum_literal_to_camel_case_with_none_input():
    """
    Test the enum_literal_to_camel_case function with None as input.

    :raises TypeError: If the input is None.
    """
    with pytest.raises(ValueError):
        enum_literal_to_camel_case(None)

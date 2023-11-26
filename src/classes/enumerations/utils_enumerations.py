def enum_literal_to_camel_case(text: str) -> str:
    """
    Convert a string with words in uppercase and separated by underscores to CamelCase format.

    This function assumes that the input string is in uppercase and words are separated by underscores.
    It converts the string to CamelCase format, where each word starts with a capital letter and is
    concatenated without spaces or underscores.

    :param text: The input string with words in uppercase and separated by underscores.
    :type text: str
    :return: A string converted to CamelCase format.
    :rtype: str
    :raises ValueError: If the input string is not in the expected format.

    :Example:

    >>> enum_literal_to_camel_case("HELLO_WORLD")
    'HelloWorld'
    """

    if not text:
        raise ValueError("Input string must not be empty.")
    elif not text.isupper():
        raise ValueError("Input string must be in uppercase.")

    # Split the text by underscores and capitalize the first letter of each word
    words = text.split("_")
    camel_case_words = [word.capitalize() for word in words]

    # Join the words without any separator
    camel_case_text = "".join(camel_case_words)
    return camel_case_text

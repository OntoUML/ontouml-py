import random
import string


def generate_random_string(
    min_length: int = 1,
    max_length: int = 100,
    use_letters: bool = True,
    use_digits: bool = True,
    use_punctuation: bool = True,
):
    """
    Generate a random string.

    :param min_length: Minimum length of the string. Default is 1.
    :param max_length: Maximum length of the string. Default is 27.
    :param use_letters: Whether to include ASCII letters. Default is True.
    :param use_digits: Whether to include digits. Default is True.
    :param use_punctuation: Whether to include punctuation. Default is True.
    :return: Randomly generated string.
    """
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if characters:
        return "".join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))
    else:
        raise ValueError("At least one character set must be selected")

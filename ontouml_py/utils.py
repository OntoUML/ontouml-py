"""This utility module contains a collection of helper functions that provide general-purpose functionalities \
for the project. These utilities are designed to be reusable and can be employed across various modules and components \
 of the project."""


def validate_subclasses(analyzed_class: object, allowed_subclasses: list[str]) -> None:
    """Ensures that the given class is a subclass of one of the allowed subclasses.

    :param analyzed_class: The class to be analyzed for subclass validation.
    :type analyzed_class: object
    :param allowed_subclasses: A list of allowed subclass names.
    :type allowed_subclasses: list[str]
    :raises ValueError: If the analyzed class is not a subclass of any allowed subclasses.
    """
    current_class = analyzed_class.__class__
    while current_class != object:
        if current_class.__name__ in allowed_subclasses:
            return
        current_class = current_class.__bases__[0]
    else:
        allowed = ", ".join(allowed_subclasses)

        raise ValueError(
            f"'{analyzed_class.__class__.__name__}' is not an allowed subclass. "
            f"Only these subclasses are permitted: {allowed}."
        )

"""This utility module contains a collection of helper functions that provide common functionality used throughout the \
application. These functions are designed to be generic and reusable across various parts of the codebase.
"""
from typing import Any, Type, List, get_origin, get_args, Union


from typing import Any, Type, List, Union, get_origin, get_args


def is_valid_list(item, inner_type) -> bool:
    """
    Recursively checks if all elements in a list are of the specified inner_type.

    :param item: The item to be checked, can be a list or a single element.
    :param inner_type: The type that items in the list are expected to be.
    :return: True if all elements are of the inner_type, False otherwise.
    """
    # Check if the item is a list, if so, recursively check each element
    if isinstance(item, list):
        return all(is_valid_list(sub_item, inner_type) for sub_item in item)
    else:
        # If inner_type is a subscripted generic, like List[str], we get the actual class (str in this case)
        actual_type = get_args(inner_type)[0] if get_origin(inner_type) is list else inner_type
        return isinstance(item, actual_type)


def validate_and_set(
    instance: Any, attr_name: str, att_value: Any, attr_type: Union[Type[Any], List[Type[Any]]], optional: bool = True
) -> None:
    """
    Securely sets the attribute value of an instance after type checking.

    :param instance: The instance of the object on which the attribute will be set.
    :param attr_name: The name of the attribute to set.
    :param att_value: The value to be assigned to the attribute.
    :param attr_type: The type the attribute should be. Can be a type or a list of types.
    :param optional: Specifies if the attribute is optional (can be None).
    :raises TypeError: If the value is not of the expected type.
    """

    # If the value is None and the attribute is optional, skip the type check and set the attribute
    if att_value is None and optional:
        setattr(instance, attr_name, att_value)
    # If the expected type is a list with a specified element type and the value is not None
    elif get_origin(attr_type) is list and att_value is not None:
        # Extract the inner type using get_args
        inner_type = get_args(attr_type)[0]
        if not is_valid_list(att_value, inner_type):
            raise TypeError(f"All elements in '{attr_name}' must be of type {inner_type.__name__}.")
        setattr(instance, attr_name, att_value)
    # If the value is not None, proceed with the type check for non-list types
    elif att_value is not None and not isinstance(att_value, attr_type):
        # This block handles single value assignment
        raise TypeError(f"The '{attr_name}' argument must be a {attr_type.__name__}, not {type(att_value).__name__}.")
    # If the value is None and the attribute is not optional, raise a TypeError
    elif att_value is None and not optional:
        raise TypeError(f"The '{attr_name}' argument cannot be None.")
    # If all checks pass, set the attribute
    else:
        setattr(instance, attr_name, att_value)

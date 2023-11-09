"""This utility module contains a collection of helper functions that provide common functionality used throughout the \
application. These functions are designed to be generic and reusable across various parts of the codebase.
"""
from typing import Any, Type, List


def secure_set(instance: Any, attr_name: str, att_value: Any, attr_type: Type[Any], optional: bool = True) -> None:
    """Securely sets the attribute value of an instance after type checking.

    :param instance: The instance of the object on which the attribute will be set.
    :type instance: Any
    :param attr_name: The name of the attribute to set.
    :type attr_name: str
    :param att_value: The value to be assigned to the attribute.
    :type att_value: Any
    :param attr_type: The type the attribute should be. Can be a type or a list of types.
    :type attr_type: Type[Any] | List[Type[Any]]
    :param optional: Specifies if the attribute is optional (can be None).
    :type optional: bool
    :raises TypeError: If the value is not of the expected type.
    """

    # If the value is None and the attribute is optional, skip the type check and set the attribute
    if att_value is None and optional:
        setattr(instance, attr_name, att_value)
    # If the value is not None, proceed with the type check
    elif att_value is not None and not isinstance(att_value, attr_type):
        # This block handles single value assignment
        raise TypeError(f"The '{attr_name}' argument must be a {attr_type.__name__}, not {type(att_value).__name__}.")
    # If the value is None and the attribute is not optional, raise a TypeError
    elif att_value is None and not optional:
        raise TypeError(f"The '{attr_name}' argument cannot be None.")
    # If all checks pass, set the attribute
    else:
        setattr(instance, attr_name, att_value)

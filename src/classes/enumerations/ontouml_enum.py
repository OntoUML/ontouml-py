"""
This module defines a base class for creating enumerations in OntoUML, where enum members are automatically converted
to CamelCase format and a utility method is provided to retrieve all enum members.

Classes:
    OntoumlEnum (Enum, metaclass=EnumABCMeta): An abstract base class for OntoUML enumerations.
"""

from abc import ABCMeta, abstractmethod
from enum import Enum, EnumMeta
from typing import KeysView

from src.classes.enumerations.utils_enumerations import enum_literal_to_camel_case


class EnumABCMeta(EnumMeta, ABCMeta):
    """
    A metaclass that combines the functionalities of EnumMeta and ABCMeta.

    This metaclass is used to create abstract base classes that are also enums, allowing for the creation of enums
    with abstract methods.
    """


class OntoumlEnum(Enum, metaclass=EnumABCMeta):
    """
    An abstract base class for OntoUML enumerations.

    This class converts enum member names to CamelCase format and provides a method to retrieve all enum members.
    Subclasses should define their enum members as usual, and they will automatically be converted to CamelCase.

    Attributes:
        _value_ (str): The CamelCase formatted string value of the enum member.

    Methods:
        __init__(): Initializes a new enum member, converting its name to CamelCase.
        get_members(): Returns the keys of all members of the enum class.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Initializes a new enum member, converting its name to CamelCase.

        This method is called automatically for each enum member when the enum class is created. It converts the
        member's name from uppercase with underscores to CamelCase format.

        :raises ValueError: If the name is not in the expected uppercase and underscore format.
        """
        self._value_ = enum_literal_to_camel_case(self.name)

    @classmethod
    def get_members(cls) -> KeysView[str]:
        """
        Returns the keys of the enum members.

        This method retrieves the keys (names) of all members of the enum class.

        :return: The keys of the enum members.
        :rtype: KeysView[str]
        """
        return cls.__members__.keys()

"""
This module defines a base class for creating enumerations in OntoUML.
"""

from abc import ABCMeta
from enum import Enum, EnumMeta
from typing import KeysView


class EnumABCMeta(EnumMeta, ABCMeta):
    """A metaclass that combines the functionalities of EnumMeta and ABCMeta.

    This metaclass is used to create abstract base classes that are also enums, allowing for the creation of enums
    with abstract methods.
    """


class OntoumlEnum(Enum, metaclass=EnumABCMeta):
    """An abstract base class for OntoUML enumerations.

    This class provides a framework for creating enumerations in OntoUML. It allows for the definition of enum members
    in subclasses, which can be used to represent various categorizations and types within the OntoUML model.
    """

    @classmethod
    def get_members(cls) -> KeysView[str]:
        """Returns the keys of the enum members.

        This method retrieves the keys (names) of all members of the enum class.

        :return: The keys of the enum members.
        :rtype: KeysView[str]
        """
        return cls.__members__.keys()

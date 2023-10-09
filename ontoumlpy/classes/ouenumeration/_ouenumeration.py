"""
This module provides the `_OUEnumeration` class, an enumeration base class which provides a method to retrieve all
members of an enumeration. Enumerations inheriting from `_OUEnumeration` can leverage this method to fetch all of
their members, simplifying tasks like iteration over all values.
"""

from enum import Enum

from rdflib import URIRef


class _OUEnumeration(Enum):
    """Base enumeration class providing a method to retrieve all members of the enumeration.

    Designed to be subclassed by other enumerations, this class introduces utility method, ensuring an enhanced
    reusability and adherence to DRY (Don't Repeat Yourself) principles in the codebase.
    """

    @classmethod
    def get_all(cls) -> list[URIRef]:
        """Method to retrieve all members of the enumeration.

        Iterates over all the enumeration members and returns their value in a list, simplifying tasks such as member
        iteration or display.

        :return: A list of all enumeration members' values.
        :rtype: list
        """
        return_list = []
        for member in cls:
            return_list.append(member.value)
        return return_list

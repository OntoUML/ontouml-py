"""This module provides the NonEmptySet class, a specialized set implementation that ensures the set is never empty.

The NonEmptySet class is a generic collection that extends the functionality of the standard Python set. It is designed
to maintain at least one element at all times, enforcing this constraint through its methods. This class is particularly
useful in scenarios where an empty set is not a valid state and can prevent errors related to handling empty sets.

Classes:
    NonEmptySet(Generic[T]): A generic class representing a set that cannot be empty.

Exceptions:
    ValueError: Raised when an operation that would result in an empty set is attempted.

Usage:
    The NonEmptySet class can be used similarly to Python's built-in set, with the added assurance that it will always
    contain at least one element. It supports standard set operations like add, remove, and iterate over elements.
"""
from typing import Generic
from typing import Iterator
from typing import Set
from typing import TypeVar

T = TypeVar("T")


class NonEmptySet(Generic[T]):
    """A class representing a set that cannot be empty.

    This class encapsulates the behavior of a standard set with the additional constraint that it cannot be empty
    after initialization. It provides methods to add, remove, and manipulate elements while maintaining this constraint.

    :ivar set: The internal set that stores the elements.
    :vartype set: Set[T]
    :raises ValueError: If an attempt is made to initialize with an empty set or perform an operation that would result
                        in an empty set.
    """

    def __init__(self, initial_elements: Set[T]):
        """Initialize the NonEmptySet with the given initial elements.

        :param initial_elements: A set of initial elements to populate the NonEmptySet.
        :type initial_elements: Set[T]
        :raises ValueError: If `initial_elements` is empty.
        """
        if not initial_elements:
            raise ValueError("Initial set cannot be empty.")
        self.set: Set[T] = set(initial_elements)

    def add(self, element: T) -> None:
        """Add an element to the set.

        :param element: The element to be added.
        :type element: T
        """
        self.set.add(element)

    def remove(self, element: T) -> None:
        """Remove an element from the set.

        :param element: The element to be removed.
        :type element: T
        :raises ValueError: If attempting to remove the last element from the set.
        """
        if len(self.set) == 1:
            raise ValueError("Cannot remove the last element from the set.")
        self.set.remove(element)

    def update(self, *others: Set[T]) -> None:
        """Update the set, adding elements from all other provided sets.

        :param others: Other sets whose elements should be added.
        :type others: Set[T]
        """
        for other in others:
            self.set.update(other)

    def discard(self, element: T) -> None:
        """Remove an element from the set if it is a member.

        If the element is not a member, do nothing.

        :param element: The element to be discarded.
        :type element: T
        :raises ValueError: If attempting to discard the last element from the set.
        """
        if len(self.set) == 1 and element in self.set:
            raise ValueError("Cannot discard the last element from the set.")
        self.set.discard(element)

    def pop(self) -> T:
        """Remove and return an arbitrary element from the set.

        :return: The element removed from the set.
        :rtype: T
        :raises ValueError: If attempting to pop the last element from the set.
        """
        if len(self.set) == 1:
            raise ValueError("Cannot pop the last element from the set.")
        return self.set.pop()

    def clear(self) -> None:
        """Remove all elements from the set.

        :raises ValueError: Always, as a NonEmptySet cannot be cleared.
        """
        raise ValueError("Cannot clear a NonEmptySet.")

    def __contains__(self, element: T) -> bool:
        """Check if the set contains the specified element.

        :param element: The element to check for.
        :type element: T
        :return: True if the element is in the set, False otherwise.
        :rtype: bool
        """
        return element in self.set

    def __iter__(self) -> Iterator[T]:
        """Return an iterator over the elements of the set.

        :return: An iterator over the set.
        :rtype: Iterator[T]
        """
        return iter(self.set)

    def __len__(self) -> int:
        """Return the number of elements in the set.

        :return: The number of elements in the set.
        :rtype: int
        """
        return len(self.set)

    def __str__(self) -> str:
        """Return the string representation of the set.

        :return: The string representation of the set.
        :rtype: str
        """
        return str(self.set)

    def __repr__(self) -> str:
        """Return the official string representation of the NonEmptySet.

        :return: The official string representation of the NonEmptySet.
        :rtype: str
        """
        return f"{self.__class__.__name__}({self.set})"

    @classmethod
    def convert_set(cls, my_set: Set[T]) -> "NonEmptySet[T]":
        """Convert a regular set to a NonEmptySet.

        :param my_set: The set to be converted.
        :type my_set: Set[T]
        :return: A NonEmptySet containing the elements of `my_set`.
        :rtype: NonEmptySet[T]
        :raises ValueError: If `my_set` is empty.
        """
        if not my_set:
            raise ValueError("Cannot create a NonEmptySet from an empty set")
        return cls(my_set)

    def __eq__(self, other: object) -> bool:
        """Check if two NonEmptySet instances are equal.

        Two NonEmptySet instances are considered equal if they contain the same elements, regardless of their order.

        :param other: The other object to compare with.
        :type other: object
        :return: True if the sets contain the same elements, False otherwise.
        :rtype: bool
        """
        if not isinstance(other, NonEmptySet):
            return NotImplemented
        return self.set == other.set

    def __hash__(self) -> int:
        """Return the hash value of the NonEmptySet.

        The hash value is based on the elements of the set. This allows NonEmptySet instances to be used in hash-based
        collections like sets and dictionaries.

        :return: The hash value of the set.
        :rtype: int
        """
        return hash(tuple(sorted(self.set)))

from typing import Generic, TypeVar, Set, Iterator

from icecream import ic

T = TypeVar('T')

class NonEmptySet(Generic[T]):
    def __init__(self, initial_elements: Set[T]):
        if not initial_elements:
            raise ValueError("Initial set cannot be empty.")
        self.set: Set[T] = set(initial_elements)

    def add(self, element: T) -> None:
        self.set.add(element)

    def remove(self, element: T) -> None:
        if len(self.set) == 1:
            raise ValueError("Cannot remove the last element from the set.")
        self.set.remove(element)

    def update(self, *others: Set[T]) -> None:
        for other in others:
            self.set.update(other)

    def discard(self, element: T) -> None:
        if len(self.set) == 1 and element in self.set:
            raise ValueError("Cannot discard the last element from the set.")
        self.set.discard(element)

    def pop(self) -> T:
        if len(self.set) == 1:
            raise ValueError("Cannot pop the last element from the set.")
        return self.set.pop()

    def clear(self) -> None:
        raise ValueError("Cannot clear a NonEmptySet.")

    def __contains__(self, element: T) -> bool:
        return element in self.set

    def __iter__(self) -> Iterator[T]:
        return iter(self.set)

    def __len__(self) -> int:
        return len(self.set)

    def __str__(self) -> str:
        return str(self.set)

    @classmethod
    def convert_set(cls, my_set: Set[T]) -> 'NonEmptySet[T]':
        if not my_set:
            raise ValueError("Cannot create a NonEmptySet from an empty set")
        return cls(my_set)

x = NonEmptySet({1,2})
ic(x)
print(x)
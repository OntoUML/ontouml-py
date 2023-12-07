from ontouml_py.classes.utils.nonemptyset import NonEmptySet

import pytest


def test_nonemptyset_initialization() -> None:
    """Test initialization of NonEmptySet with non-empty set."""
    non_empty_set = NonEmptySet({1, 2, 3})
    assert len(non_empty_set) == 3, "NonEmptySet should initialize with the correct number of elements"


def test_nonemptyset_initialization_empty_set() -> None:
    """Test initialization of NonEmptySet with an empty set raises ValueError."""
    with pytest.raises(ValueError, match="Initial set cannot be empty."):
        NonEmptySet(set())


def test_nonemptyset_add_element() -> None:
    """Test adding an element to the NonEmptySet."""
    non_empty_set = NonEmptySet({1})
    non_empty_set.add(2)
    assert 2 in non_empty_set, "Element should be added to NonEmptySet"


def test_nonemptyset_remove_element() -> None:
    """Test removing an element from the NonEmptySet."""
    non_empty_set = NonEmptySet({1, 2})
    non_empty_set.remove(1)
    assert 1 not in non_empty_set, "Element should be removed from NonEmptySet"


def test_nonemptyset_remove_last_element() -> None:
    """Test removing the last element from the NonEmptySet raises ValueError."""
    non_empty_set = NonEmptySet({1})
    with pytest.raises(ValueError, match="Cannot remove the last element from the set."):
        non_empty_set.remove(1)


def test_nonemptyset_update() -> None:
    """Test updating NonEmptySet with another set."""
    non_empty_set = NonEmptySet({1})
    non_empty_set.update({2, 3})
    assert non_empty_set == NonEmptySet({1, 2, 3}), "NonEmptySet should be updated correctly"


def test_nonemptyset_discard_existing_element() -> None:
    """Test discarding an existing element from NonEmptySet."""
    non_empty_set = NonEmptySet({1, 2})
    non_empty_set.discard(1)
    assert 1 not in non_empty_set, "Existing element should be discarded from NonEmptySet"


def test_nonemptyset_discard_last_element() -> None:
    """Test discarding the last element from NonEmptySet raises ValueError."""
    non_empty_set = NonEmptySet({1})
    with pytest.raises(ValueError, match="Cannot discard the last element from the set."):
        non_empty_set.discard(1)


def test_nonemptyset_pop_element() -> None:
    """Test popping an element from NonEmptySet."""
    non_empty_set = NonEmptySet({1, 2})
    popped = non_empty_set.pop()
    assert popped in {1, 2}, "Popped element should be from NonEmptySet"
    assert len(non_empty_set) == 1, "NonEmptySet should have one less element after pop"


def test_nonemptyset_pop_last_element() -> None:
    """Test popping the last element from NonEmptySet raises ValueError."""
    non_empty_set = NonEmptySet({1})
    with pytest.raises(ValueError, match="Cannot pop the last element from the set."):
        non_empty_set.pop()


def test_nonemptyset_clear() -> None:
    """Test clearing NonEmptySet raises ValueError."""
    non_empty_set = NonEmptySet({1, 2, 3})
    with pytest.raises(ValueError, match="Cannot clear a NonEmptySet."):
        non_empty_set.clear()


def test_nonemptyset_convert_set() -> None:
    """Test converting a regular set to NonEmptySet."""
    regular_set = {1, 2, 3}
    non_empty_set = NonEmptySet.convert_set(regular_set)
    assert non_empty_set == NonEmptySet({1, 2, 3}), "NonEmptySet should be correctly created from a regular set"


def test_nonemptyset_convert_empty_set() -> None:
    """Test converting an empty set to NonEmptySet raises ValueError."""
    with pytest.raises(ValueError, match="Cannot create a NonEmptySet from an empty set"):
        NonEmptySet.convert_set(set())


def test_nonemptyset_str_representation() -> None:
    """Test the string representation of NonEmptySet."""
    non_empty_set = NonEmptySet({1, 2, 3})
    assert str(non_empty_set) == "{1, 2, 3}", "String representation of NonEmptySet should be correct"


def test_nonemptyset_repr_representation() -> None:
    """Test the official string representation of NonEmptySet."""
    non_empty_set = NonEmptySet({1, 2})
    assert (
        repr(non_empty_set) == "NonEmptySet({1, 2})"
    ), "Official string representation of NonEmptySet should be correct"

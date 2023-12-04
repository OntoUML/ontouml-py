from typing import Any

import pytest

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.abstract_classes.modelelement import ModelElement
from ontouml_py.classes.concrete_classes.class_py import Class
from ontouml_py.classes.concrete_classes.generalization import Generalization
from ontouml_py.classes.concrete_classes.generalizationset import GeneralizationSet
from ontouml_py.classes.enumerations.classstereotype import ClassStereotype


class Relation(Classifier):
    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)


def test_generalization_set_initialization() -> None:
    """Test the initialization of a GeneralizationSet instance."""
    generalization = Generalization(general=Relation(), specific=Relation())
    generalization_set = GeneralizationSet(is_disjoint=True, is_complete=False, generalizations={generalization})
    assert generalization_set.is_disjoint, "GeneralizationSet should be initialized as disjoint"
    assert not generalization_set.is_complete, "GeneralizationSet should be initialized as not complete"
    assert generalization in generalization_set.generalizations, "Generalization should be in the generalizations set"


def test_generalization_set_empty_generalizations() -> None:
    """Test the initialization of a GeneralizationSet with no generalizations.
    :raises: ValueError: If generalizations set is empty.
    """
    with pytest.raises(ValueError):
        GeneralizationSet(is_disjoint=True, is_complete=True, generalizations=set())


def test_generalization_set_with_invalid_generalization_type() -> None:
    """Test the initialization of a GeneralizationSet with an invalid type in generalizations.
    :raises: TypeError: If an element in generalizations is not a Generalization instance.
    """
    with pytest.raises(TypeError):
        GeneralizationSet(is_disjoint=True, is_complete=True, generalizations={ModelElement()})


def test_generalization_set_add_generalization() -> None:
    """Test adding a generalization to a GeneralizationSet."""
    generalization0 = Generalization(general=Relation(), specific=Relation())
    generalization_set = GeneralizationSet(generalizations={generalization0})
    generalization = Generalization(general=Relation(), specific=Relation())
    generalization_set.generalizations.add(generalization)
    assert (
        generalization in generalization_set.generalizations
    ), "Generalization should be added to the generalizations set"


def test_generalization_set_remove_to_empty() -> None:
    """Test removing a generalization from a GeneralizationSet."""
    generalization = Generalization(general=Relation(), specific=Relation())
    generalization_set = GeneralizationSet(generalizations={generalization})
    with pytest.raises(ValueError):
        generalization_set.generalizations.remove(generalization)


def test_generalization_set_remove_generalization() -> None:
    """Test removing a generalization from a GeneralizationSet."""
    generalization0 = Generalization(general=Relation(), specific=Relation())
    generalization1 = Generalization(general=Relation(), specific=Relation())
    generalization_set = GeneralizationSet(generalizations={generalization0, generalization1})
    generalization_set.generalizations.remove(generalization0)
    assert (
        generalization0 not in generalization_set.generalizations
    ), "Generalization should be removed from the generalizations set"


def test_generalization_set_with_categorizer() -> None:
    """Test the initialization of a GeneralizationSet with a categorizer."""
    generalization = Generalization(general=Relation(), specific=Relation())
    categorizer = Class(stereotype=ClassStereotype.KIND)
    generalization_set = GeneralizationSet(categorizer=categorizer, generalizations={generalization})
    assert generalization_set.categorizer == categorizer, "Categorizer should be set correctly in GeneralizationSet"


def test_generalization_set_without_categorizer() -> None:
    """Test the initialization of a GeneralizationSet without a categorizer."""
    generalization = Generalization(general=Relation(), specific=Relation())
    generalization_set = GeneralizationSet(generalizations={generalization})
    assert generalization_set.categorizer is None, "Categorizer should be None when not set in GeneralizationSet"

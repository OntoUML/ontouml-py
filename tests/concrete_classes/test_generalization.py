from typing import Any

import pytest
from pydantic import ValidationError

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.concrete_classes.generalization import Generalization


class Relation(Classifier):
    def __init__(self, **data: dict[str, Any]) -> None:
        super().__init__(**data)


def test_generalization_with_different_classifiers() -> None:
    """Test creating a Generalization with different general and specific classifiers."""
    general = Relation()
    specific = Relation()

    generalization = Generalization(general=general, specific=specific)

    assert generalization.general == general, "General classifier should be correctly set in Generalization."
    assert generalization.specific == specific, "Specific classifier should be correctly set in Generalization."


def test_generalization_with_same_classifier_raises_error() -> None:
    """Test that creating a Generalization with the same classifier for general and specific raises ValueError."""
    classifier = Relation()

    with pytest.raises(ValueError):
        Generalization(general=classifier, specific=classifier)


def test_generalization_with_invalid_general_type_raises_error() -> None:
    """Test that creating a Generalization with an invalid type for general raises TypeError."""
    specific = Relation()

    with pytest.raises(ValidationError):
        Generalization(general="invalid_type", specific=specific)


def test_generalization_with_invalid_specific_type_raises_error() -> None:
    """Test that creating a Generalization with an invalid type for specific raises TypeError."""
    general = Relation()

    with pytest.raises(ValidationError):
        Generalization(general=general, specific="invalid_type")


def test_generalization_without_general_raises_error() -> None:
    """Test that creating a Generalization without a general classifier raises a validation error."""
    specific = Relation()

    with pytest.raises(ValidationError):
        Generalization(specific=specific)


def test_generalization_without_specific_raises_error() -> None:
    """Test that creating a Generalization without a specific classifier raises a validation error."""
    general = Relation()

    with pytest.raises(ValidationError):
        Generalization(general=general)


def test_modifying_generalization_classifiers() -> None:
    """Test modifying the general and specific classifiers of an existing Generalization."""
    general1 = Relation()
    specific1 = Relation()
    generalization = Generalization(general=general1, specific=specific1)

    general2 = Relation()
    specific2 = Relation()
    generalization.general = general2
    generalization.specific = specific2

    assert generalization.general == general2, "General classifier should be updated correctly."
    assert generalization.specific == specific2, "Specific classifier should be updated correctly."

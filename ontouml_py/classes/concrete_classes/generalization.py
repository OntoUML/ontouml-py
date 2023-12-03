"""This module defines the `Generalization` class, a component of the ontouml_py library. The `Generalization` class
represents a generalization relationship in an ontological model, linking two classifiers in a hierarchy where one
(classifier) is a generalization of the other. This module includes the necessary validations to ensure the integrity
of the generalization relationship, such as preventing a classifier from being a generalization of itself.
"""
from typing import Any

from pydantic import Field, model_validator

from ontouml_py.classes.abstract_classes.classifier import Classifier
from ontouml_py.classes.abstract_classes.modelelement import ModelElement


class Generalization(ModelElement):
    """Represent a generalization relationship between two classifiers in an ontological model.

    This class extends `ModelElement` and is used to define a generalization, where one classifier (the general) is
    a generalization of another classifier (the specific).

    :ivar general: The general classifier in the generalization relationship.
    :vartype general: Classifier
    :ivar specific: The specific classifier in the generalization relationship.
    :vartype specific: Classifier
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    general: Classifier = Field()
    specific: Classifier = Field()

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @model_validator(mode="after")
    def ensure_irreflexive(self):
        """Validate that the generalization relationship is irreflexive.

        Ensures that the 'general' and 'specific' classifiers are not the same, as a classifier cannot generalize itself.

        :raises ValueError: If 'general' and 'specific' classifiers are the same.
        """
        if self.general == self.specific:
            raise ValueError("A generalization must relate different 'general' and 'specific' Classifiers.")

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new instance of the Generalization class.

        This constructor initializes a Generalization instance with specified attributes. It ensures that the
        generalization relationship is correctly established between the 'general' and 'specific' classifiers.

        :param data: A dictionary containing the data to initialize the Generalization instance. Expected keys are
                     'general' and 'specific', corresponding to the classifiers involved in the generalization.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

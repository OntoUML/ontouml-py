"""This module defines the `Generalization` class, a component of the ontouml_py library.

The `Generalization` class represents a generalization relationship in an ontological model, linking two classifiers in
a hierarchy where one (classifier) is a generalization of the other. This module includes the necessary validations to
ensure the integrity of the generalization relationship, such as preventing a classifier from being a generalization
of itself.
"""
from typing import Any

from pydantic import Field
from pydantic import model_validator

from ontouml_py.model.classifier import Classifier
from ontouml_py.model.packageable import Packageable
from ontouml_py.utils.error_message import format_error_message


class Generalization(Packageable):
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

    model_config = {
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "validate_default": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
    }

    @model_validator(mode="after")
    def __ensure_irreflexive(self) -> None:
        """Validate that the generalization relationship is irreflexive.

        Ensures that the 'general' and 'specific' classifiers are different, as a classifier cannot generalize itself.

        :raises ValueError: If 'general' and 'specific' classifiers are the same.
        """
        if self.general == self.specific:
            error_message = format_error_message(
                description=f"Invalid relationship for generalization with ID {self.id}.",
                cause=f"The 'general' and 'specific' classifiers are the same (same ID {self.general.id}).",
                solution="Ensure 'general' and 'specific' refer to different Classifiers.",
            )
            raise ValueError(error_message)

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new instance of the Generalization class.

        This constructor initializes a Generalization instance with specified attributes. It ensures that the
        generalization relationship is correctly established between the 'general' and 'specific' classifiers.

        :param data: A dictionary containing the data to initialize the Generalization instance. Expected keys are
                     'general' and 'specific', corresponding to the classifiers involved in the generalization.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

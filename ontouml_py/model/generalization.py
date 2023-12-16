"""This module defines the `Generalization` class, a component of the ontouml_py library.

The `Generalization` class represents a generalization relationship in an ontological model, linking two classifiers in
a hierarchy where one (classifier) is a generalization of the other. This module includes the necessary validations to
ensure the integrity of the generalization relationship, such as preventing a classifier from being a generalization
of itself.
"""
from typing import Any

from pydantic import Field

from ontouml_py.model.classifier import Classifier
from ontouml_py.model.modelelement import ModelElement
from ontouml_py.model.packageable import Packageable


class Generalization(ModelElement, Packageable):
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
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: "Project", **data: dict[str, Any]) -> None:
        ModelElement.__init__(self, project=project, pe_type=self.__class__.__name__, **data)

"""This module defines the GeneralizationSet class, a key construct in ontological modeling within the ontouml_py library.

The GeneralizationSet class is used to represent a collection of generalizations, encapsulating the notions of
disjointness and completeness in a model. It extends the ModelElement class, inheriting its core properties and
behaviors, and adds specific attributes and methods relevant to the management of generalizations.

A GeneralizationSet is typically used in ontological models to express constraints and relationships between different
classes. It can specify whether the subclasses in the generalization are disjoint (no instances can be shared
among subclasses) and whether they are complete (the superclass is fully covered by the subclasses).

Key Features:
- Represents a set of generalizations in an ontological model.
- Supports disjointness and completeness constraints.
- Allows association with a categorizing class.

The module provides the necessary functionality to create, manipulate, and query GeneralizationSet instances, making
it a vital part of the ontouml_py library's support for advanced ontological modeling.

Classes:
- GeneralizationSet: Represents a set of generalizations with optional disjointness and completeness constraints.

Dependencies:
- ModelElement from ontouml_py.classes.abstract_classes.modelelement
- Class from ontouml_py.classes.concrete_classes.class_py
- Generalization from ontouml_py.classes.concrete_classes.generalization
"""
from typing import Optional, Any

from pydantic import Field, model_validator, field_validator

from ontouml_py.classes.abstract_classes.modelelement import ModelElement
from ontouml_py.classes.concrete_classes.class_py import Class
from ontouml_py.classes.concrete_classes.generalization import Generalization
from ontouml_py.classes.utils.nonemptyset import NonEmptySet


class GeneralizationSet(ModelElement):
    """Represent a set of generalizations in an ontological model, extending the ModelElement class.

    A GeneralizationSet is a collection of Generalization instances, typically used to represent
    disjointness and completeness constraints in a model.

    :ivar is_disjoint: Indicates if the generalizations in the set are disjoint.
    :vartype is_disjoint: bool
    :ivar is_complete: Indicates if the generalizations in the set are complete.
    :vartype is_complete: bool
    :ivar generalizations: A set of Generalization instances included in this generalization set.
    :vartype generalizations: Set[Generalization]
    :ivar categorizer: An optional Class instance that categorizes the generalization set.
    :vartype categorizer: Optional[Class]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    is_disjoint: bool = Field(default=False)
    is_complete: bool = Field(default=False)
    generalizations: set[object] = Field(min_length=1, default_factory=set)
    categorizer: Optional[object] = Field(default=None)

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @field_validator("generalizations", mode="after")
    @classmethod
    def __ensure_generalizations_type(cls, checked_set: set[object]) -> set[Generalization]:
        for elem in checked_set:
            if not isinstance(elem, Generalization):
                raise ValueError(
                    "All elements in a GeneralizationSet's generalization set must be of type " "Generalization."
                )
        return checked_set

    @field_validator("categorizer", mode="after")
    @classmethod
    def __ensure_categorizer_type(cls, checked_value: Optional[object]) -> Optional[Class]:
        if checked_value and not isinstance(checked_value, Class):
            raise ValueError("A GeneralizationSet's categorizer must be of type Class.")
        else:
            return checked_value

    @model_validator(mode="after")
    def __validate_generalization_set(self) -> None:
        if not isinstance(self.generalizations, NonEmptySet):
            converted_generalizations = NonEmptySet.convert_set(self.generalizations)
            # Workaround necessary to avoid recursively invoking the validation
            self.__dict__["generalizations"] = converted_generalizations

    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new instance of GeneralizationSet.

        :param data: A dictionary of data to initialize the GeneralizationSet attributes.
        :type data: dict[str, Any]
        """
        super().__init__(**data)

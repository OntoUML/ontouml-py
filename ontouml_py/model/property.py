from typing import Any
from typing import Optional

from pydantic import Field
from pydantic import PrivateAttr
from pydantic import field_validator

from ontouml_py.model.cardinality import Cardinality
from ontouml_py.model.decoratable import Decoratable
from ontouml_py.model.enumerations.aggregationkind import AggregationKind
from ontouml_py.model.enumerations.propertystereotype import PropertyStereotype
from ontouml_py.utils.error_message import format_error_message


class Property(Decoratable):
    # Private attributes
    _classifier: "Classifier" = PrivateAttr(default=None)
    # Public attributes
    is_read_only: bool = Field(default=False)
    aggregation_kind: AggregationKind = Field(default=AggregationKind.NONE)
    stereotype: Optional[PropertyStereotype] = Field(default=None)
    cardinality: Cardinality = Field(default=Cardinality())
    property_type: Optional[object] = Field(default=None)
    subsetted_by: set["Property"] = Field(default_factory=set)
    redefined_by: set["Property"] = Field(default_factory=set)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, classifier: "Classifier", project: object, **data: dict[str, Any]) -> None:
        self._classifier = classifier
        super().__init__(project=project, pe_type=self.__class__.__name__, **data)

    @field_validator("cardinality", mode="after")
    @classmethod
    def __validate_cardinality_type(cls, checked_value: object) -> Cardinality:
        if not isinstance(checked_value, Cardinality):
            error_message = format_error_message(
                description="Invalid cardinality type.",
                cause=f"Expected Cardinality instance, got {type(checked_value).__name__} instance.",
                solution="Ensure the cardinality is set with an instance of the Cardinality class.",
            )
            raise TypeError(error_message)
        return checked_value

    @property
    def classifier(self) -> "Classifier":
        """Get the owning classifier of this property.

        :return: The Classifier instance that owns this property, if any.
        :rtype: Optional[Classifier]
        """
        return self._classifier

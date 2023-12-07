"""This module provides the Cardinality class, which is used to represent and validate cardinality constraints in \
data models.

The Cardinality class allows for the specification of lower and upper bounds for cardinality, along with flags for \
ordering and uniqueness of elements. It uses Pydantic's BaseModel for data validation and ensures that the \
cardinality constraints provided are logically consistent and valid.

Classes:
    Cardinality: A class for defining and validating cardinality constraints in data models.

Example:
    To define a cardinality constraint with a minimum of 1 and no maximum limit, while ensuring elements are unique \
    and not ordered:

        cardinality = Cardinality(lower_bound="1", upper_bound="*", is_ordered=False, is_unique=True)

Dependencies:
    This module requires the 'pydantic' package for data validation.
"""
from typing import Optional, Union

from pydantic import Field, BaseModel, model_validator

from ontouml_py.classes.utils.error_message import format_error_message


class Cardinality(BaseModel):
    """A class representing the cardinality constraints in a data model.

    This class allows for the specification and validation of lower and upper bounds of cardinality,
    along with properties indicating whether the elements are ordered and unique.

    :ivar lower_bound: The lower bound of the cardinality, either an integer as a string or '*'. Defaults to None.
    :vartype lower_bound: Optional[str]
    :ivar upper_bound: The upper bound of the cardinality, either an integer as a string or '*'. Defaults to None.
    :vartype upper_bound: Optional[str]
    :ivar is_ordered: Flag indicating if the elements are ordered. Defaults to False.
    :vartype is_ordered: bool
    :ivar is_unique: Flag indicating if the elements are unique. Defaults to True.
    :vartype is_unique: bool
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    lower_bound: Optional[Union[str, int]] = Field(default=None)
    upper_bound: Optional[Union[str, int]] = Field(default=None)
    is_ordered: bool = Field(default=False)
    is_unique: bool = Field(default=True)

    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @model_validator(mode="after")
    def __ensure_valid_multiplicity(self):
        """Validate the cardinality ensuring the lower and upper bounds are synchronized and valid.

        This method checks for the logical consistency of the lower and upper bounds of the cardinality.
        It ensures that the values are either integers or '*', and that the lower bound is not greater than the upper
        bound. It raises a ValueError if the bounds are not valid, logically inconsistent, or if empty strings are
        provided.

        :raises ValueError: If the cardinality values do not follow the defined rules or if empty strings are used.
        """
        # Ensuring cardinality value will be stored as a string even though received as an integer:
        if isinstance(self.lower_bound, int):
            self.lower_bound = str(self.lower_bound)
        if isinstance(self.upper_bound, int):
            self.upper_bound = str(self.upper_bound)

        # Ensuring synchronicity between lower and upper bounds
        if self.lower_bound and not self.upper_bound:
            self.upper_bound = self.lower_bound
        elif self.upper_bound and not self.lower_bound:
            self.lower_bound = self.upper_bound

        # Ensure minimum string size > 0 (i.e., empty strings are not allowed)
        if (self.lower_bound == "") or (self.upper_bound == ""):
            error_message = format_error_message(
                error_type="ValueError.",
                description="Invalid cardinality bounds.",
                cause="Empty string provided for lower or upper bound.",
                solution="Ensure both bounds are integers or '*'.",
            )
            raise ValueError(error_message)

        # Verifying invalid digit
        rule1_lb = self.lower_bound and (self.lower_bound != "*" and not self.lower_bound.isdigit())
        rule1_ub = self.upper_bound and (self.upper_bound != "*" and not self.upper_bound.isdigit())

        if rule1_lb or rule1_ub:
            error_message = format_error_message(
                error_type="ValueError.",
                description="Invalid cardinality bounds.",
                cause="Non-integer and non-'*' value provided for lower or upper bound.",
                solution="Ensure both bounds are integers or '*'.",
            )
            raise ValueError(error_message)

        # Verifying if lower bound is greater than the upper bound
        rule2_a = (self.lower_bound == "*") and (self.upper_bound != "*")
        rule2_b = (
            (self.lower_bound and self.upper_bound)
            and (self.lower_bound != "*" and self.upper_bound != "*")
            and (int(self.lower_bound) > int(self.upper_bound))
        )

        if rule2_a or rule2_b:
            error_message = format_error_message(
                error_type="Value Error",
                description="Invalid cardinality bounds.",
                cause=f"The cardinality's lower bound ({self.lower_bound}) "
                f"is higher than its upper bound ({self.upper_bound}).",
                solution="Ensure the lower bound is not greater than the upper bound.",
            )
            raise ValueError(error_message)

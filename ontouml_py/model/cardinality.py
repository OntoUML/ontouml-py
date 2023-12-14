from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field


class Cardinality(BaseModel):
    lower_bound: Optional[Union[str, int]] = Field(default=1)
    upper_bound: Optional[Union[str, int]] = Field(default=1)
    is_ordered: bool = Field(default=False)
    is_unique: bool = Field(default=True)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

import time
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional

import icecream
from pydantic import BaseModel, Field

from ontouml_py.classes.datatypes.cardinality import Cardinality

# Initializing icecream's ic function in all modules. Should be removed for the library's release.
icecream.install()

class OntoumlElement(ABC, BaseModel):


    id: str = Field(min_length=1, default_factory=lambda: str(uuid.uuid4()))
    created: datetime = Field(default_factory=datetime.now)
    modified: Optional[datetime] = Field(default=None)

    # Pydantic's configuration settings for the class.
    model_config = {  # noqa (vulture)
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:

        self._validate_subclasses(["NamedElement", "Project", "ProjectElement", "Shape", "View"])

        # Sets attributes
        super().__init__(**data)

        # Additional validations
        if self.modified is not None and self.modified < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")

    def __setattr__(self, key: str, value: Any) -> None:

        if key == "modified" and value is not None and value < self.created:
            raise ValueError("The 'modified' datetime must be later than the 'created' datetime.")
        super().__setattr__(key, value)

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, OntoumlElement):
            return NotImplemented
        return self.id == other.id  # Assuming 'id' is a unique identifier for Project instances

    def __hash__(self) -> int:

        return hash(self.id)  # Hash based on a unique identifier

    @classmethod
    def _validate_subclasses(cls, allowed_subclasses: list[str]) -> None:

        current_class = cls
        while current_class != object:
            if current_class.__name__ in allowed_subclasses:
                return
            current_class = current_class.__bases__[0]
        else:
            allowed = ", ".join(allowed_subclasses)

            raise ValueError(
                f"'{cls.__name__}' is not an allowed subclass. " f"Only these subclasses are permitted: {allowed}."
            )


    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        attrs = kwargs

        # Handle 'id' attribute
        id_input = input("Enter ID or leave blank for auto-generation (str): ")
        attrs['id'] = id_input if id_input else str(uuid.uuid4())

        # Handle 'created' attribute
        created_input = input("Enter creation datetime (YYYY-MM-DD HH:MM:SS) or leave blank for now: ")
        if created_input:
            try:
                attrs['created'] = datetime.strptime(created_input, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Invalid datetime format. Using current datetime.")
                attrs['created'] = datetime.now()
        else:
            attrs['created'] = datetime.now()

        # Handle 'modified' attribute
        modified_input = input("Enter modified datetime (YYYY-MM-DD HH:MM:SS) or leave blank: ")
        if modified_input:
            try:
                modified_datetime = datetime.strptime(modified_input, "%Y-%m-%d %H:%M:%S")
                if modified_datetime < attrs['created']:
                    print("The 'modified' datetime must be later than the 'created' datetime. Using 'created' datetime.")
                    attrs['modified'] = attrs['created']
                else:
                    attrs['modified'] = modified_datetime
            except ValueError:
                print("Invalid datetime format. Leaving 'modified' as None.")
                attrs['modified'] = None
        else:
            attrs['modified'] = None

        return cls(**attrs)

class Shape(OntoumlElement):

    name: str = Field(min_length=1)
    card: object = Field(default=Cardinality())

    def __init__(self, **data: dict[str, Any]) -> None:
        # Sets attributes
        super().__init__(**data)

    @classmethod
    def create(cls):
        # Gather inputs for all attributes
        inputs = {}

        name_input = input("Enter the name for the new Shape (str): ")
        inputs['name'] = name_input

        card_input = Cardinality.create()
        inputs['card'] = card_input

        # Now call the superclass create method with all inputs
        return super(Shape, cls).create(**inputs)

y = Shape(name="test1", card=Cardinality(lower_bound="1"))
ic(y)
time.sleep(1)

x = Shape.create()
ic(x)

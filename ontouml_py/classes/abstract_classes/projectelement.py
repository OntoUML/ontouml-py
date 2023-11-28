"""Module for the ProjectElement class within an OntoUML model.

This module defines the ProjectElement class, an abstract class that represents elements associated with a project in
an OntoUML model. It extends the OntoumlElement class and includes an additional read-only attribute to link the element
to a specific project. The module ensures that the elements are part of valid subclasses and enforces specific
constraints on attribute initialization and management.
"""


from abc import abstractmethod
from typing import Any, Optional

from pydantic import Field

from ontouml_py.classes.abstract_classes.ontoumlelement import OntoumlElement
from ontouml_py.utils import validate_subclasses


class ProjectElement(OntoumlElement):
    """Abstract class representing an element that is part of a project in an OntoUML model.

    This class extends OntoumlElement and includes an additional attribute to link the element to a specific project.
    The `in_project` attribute is read-only and should be managed through the Project class.

    :ivar in_project: Reference to the Project instance this element belongs to. This is a read-only attribute.
    :vartype in_project: Project
    """

    in_project: Optional[object] = Field(default=None)  # The type is ensured by the init restriction

    # Pydantic's configuration settings for the class.
    model_config = {
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, **data: dict[str, Any]) -> None:
        """Initialize a new ProjectElement instance. This method is abstract and should be implemented by subclasses.

        Ensures that the element is part of a valid subclass and sets initial attributes. It also enforces that the
        'in_project' attribute is not directly initialized, as it is a read-only property managed by the Project class.

        :param data: Fields to be set on the model instance, excluding 'in_project'.
        :type data: dict[str, Any]
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created', or if 'in_project' is directly
                            initialized.
        """
        validate_subclasses(self, ["ModelElement", "Diagram", "Shape", "View"])
        super().__init__(**data)

        # Additional validations
        if "in_project" in data:
            raise ValueError(
                "Attribute 'in_project' is a read-only property. This operation should be done via Project class."
            )

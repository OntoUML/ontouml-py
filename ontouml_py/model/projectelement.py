"""Module for the ProjectElement class within an OntoUML model.

This module defines the ProjectElement class, an abstract class representing elements associated with a project in
an OntoUML model. It extends the OntoumlElement class, adding a read-only attribute to link the element to a specific
project. The module ensures elements are part of valid subclasses and enforces constraints on attribute initialization
and management.
"""
from abc import abstractmethod
from typing import Any
from typing import Optional

from pydantic import PrivateAttr

from ontouml_py.model.ontoumlelement import OntoumlElement


class ProjectElement(OntoumlElement):
    """Abstract class representing an element that is part of a project in an OntoUML model.

    This class extends OntoumlElement and includes an additional attribute to link the element to a specific project.
    The `in_project` attribute is read-only and should be managed through the Project class, ensuring that each
    element is correctly associated with the intended project context, thus maintaining the integrity of the OntoUML
    model.

    :ivar in_project: Reference to the Project instance this element belongs to. This is a read-only attribute.
    :vartype in_project: Optional[Project]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    _in_project: Optional["Project"] = PrivateAttr(default=None)  # noqa: F821 (flake8)

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
        self._validate_subclasses(["ModelElement", "Diagram", "Shape", "View"])
        super().__init__(**data)

    @property
    def in_project(self) -> Optional["Project"]:  # noqa: F821 (flake8)
        """Read-only property to access the project this element belongs to.

        :return: The project instance to which this element is associated.
        :rtype: Optional[Project]
        """
        return self._in_project

    def __set_in_project(self, new_project: Optional["Project"]) -> None:  # noqa: F821 (flake8)
        """Protected method to set the project. Not part of the public API.

        This method is used internally by the Project class to establish or break the association between this element
        and a project.

        :param new_project: The project instance to associate with this element.
        :type new_project: Project
        """
        self._in_project = new_project

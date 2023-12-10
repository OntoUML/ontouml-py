"""Module for the ProjectElement class within an OntoUML model.

This module defines the ProjectElement class, an abstract class representing elements associated with a project in
an OntoUML model. It extends the OntoumlElement class, adding a read-only attribute to link the element to a specific
project. The module ensures elements are part of valid subclasses and enforces constraints on attribute initialization
and management.
"""
from abc import abstractmethod
from typing import Any

from icecream import ic
from pydantic import PrivateAttr

from ontouml_py import model
from ontouml_py.model.ontoumlelement import OntoumlElement


class ProjectElement(OntoumlElement):
    """Abstract class representing an element that is part of a project in an OntoUML model.

    This class extends OntoumlElement and includes an additional attribute to link the element to a specific project.
    The `_project` attribute is read-only and should be managed through the Project class, ensuring that each
    element is correctly associated with the intended project context, thus maintaining the integrity of the OntoUML
    model.

    :ivar _project: Reference to the Project instance this element belongs to. This is a read-only attribute.
    :vartype _project: Optional[Project]
    :cvar model_config: Configuration settings for the Pydantic model.
    :vartype model_config: Dict[str, Any]
    """

    _project: "Project" = PrivateAttr()

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    @abstractmethod
    def __init__(self, project: "Project", **data: dict[str, Any]) -> None:
        """Initialize a new ProjectElement instance. This method is abstract and should be implemented by subclasses.

        Ensures that the element is part of a valid subclass and sets initial attributes. It also enforces that the
        'in_project' attribute is not directly initialized, as it is a read-only property managed by the Project class.

        :param data: Fields to be set on the model instance, excluding 'in_project'.
        :type data: dict[str, Any]
        :raises ValueError: If 'modified' is set to a datetime earlier than 'created', or if 'in_project' is directly
                            initialized.
        """

        if not isinstance(project, model.project.Project):
            raise TypeError("unallowed type")

        super().__init__(**data)
        self._project = project
        self._validate_subclasses(["ModelElement", "Diagram", "Shape", "View"])

    @property
    def project(self) -> "Project":
        """Read-only property to access the project this element belongs to.

        :return: The project instance to which this element is associated.
        :rtype: Optional[Project]
        """
        return self._project

    def __repr__(self):
        # Get the default representation from the superclass
        base_repr = super().__repr__()

        # Append the project representation
        project_repr = f", project.id={self.project.id})"
        return base_repr[:-1] + project_repr

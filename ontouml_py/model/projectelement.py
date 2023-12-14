from pydantic import PrivateAttr


class ProjectElement:
    _project: "Project" = PrivateAttr()

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self, project: object, pe_type: str) -> None:
        project._elements[pe_type].add(self)
        self._project = project

        # Ensures abstract
        if type(self) is ProjectElement:
            raise TypeError(f"{type(self).__name__} is an abstract class and cannot be directly instantiated.")

    @property
    def project(self) -> "Project":
        """Read-only property to access the project this element belongs to.

        :return: The project instance to which this element is associated.
        :rtype: Optional[Project]
        """
        return self._project

from icecream import ic
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

    @classmethod
    def __new__(cls):
        if cls is ProjectElement:
            raise TypeError(f"{cls.__name__} is an abstract class and cannot be instantiated.")
        return super().__new__(cls)

    def __init__(self, project: object, pe_type: str) -> None:
        project._elements[pe_type].add(self)
        self._project = project

    @property
    def project(self) -> "Project":
        """Read-only property to access the project this element belongs to.

        :return: The project instance to which this element is associated.
        :rtype: Optional[Project]
        """
        return self._project

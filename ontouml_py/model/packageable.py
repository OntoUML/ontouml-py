from typing import Optional

from pydantic import PrivateAttr


class Packageable:
    _package: Optional["Package"] = PrivateAttr(default=None)  # noqa:F821

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    def __init__(self):
        if type(self) is Packageable:
            raise TypeError(f"{type(self).__name__} is an abstract class and cannot be instantiated.")

    @property
    def package(self) -> Optional["Package"]:  # noqa:F821
        return self._package

    def __set_package(self, owner_package: Optional["Package"]) -> None:  # noqa:F821
        self._package = owner_package

    def _remove_from_package(self):
        owner = self._package
        if owner:
            owner.remove_content(self)

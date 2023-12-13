from typing import Optional

from pydantic import PrivateAttr


class Packageable:
    _package: Optional["Package"] = PrivateAttr(default=None)

    model_config = {
        "arbitrary_types_allowed": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "validate_default": True,
    }

    @property
    def package(self) -> Optional["Package"]:  # noqa: F821 (flake8)
        return self._package

    def __set_package(self, owner_package: Optional["Package"]) -> None:  # noqa: F821 (flake8)
        self._package = owner_package

    def _remove_from_package(self):
        owner = self._package
        if owner:
            owner.remove_content(self)

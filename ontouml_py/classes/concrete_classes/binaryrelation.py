from ontouml_py.classes.abstract_classes.namedelement import NamedElement


class BinaryRelation(NamedElement):
    # Configuration settings for the Project model using Pydantic.
    model_config = {  # noqa (vulture)
        "arbitrary_types_allowed": True,
        "validate_assignment": True,
        "extra": "forbid",
        "str_strip_whitespace": True,
        "validate_default": True,
    }

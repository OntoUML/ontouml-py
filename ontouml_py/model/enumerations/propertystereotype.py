"""This module defines the PropertyStereotype enumeration, a subclass of OntoumlEnum, representing different \
stereotypes applicable to properties in OntoUML."""
from ontouml_py.model.enumerations.ontouml_enum import OntoumlEnum


class PropertyStereotype(OntoumlEnum):
    """An enumeration representing different stereotypes applicable to properties in OntoUML.

    This enum classifies various stereotypes that can be assigned to property elements in an OntoUML model. It extends
    OntoumlEnum.

    Members:
        BEGIN: Represents a 'begin' stereotype, typically used for temporal properties.
        END: Represents an 'end' stereotype, often associated with the termination of temporal properties.
    """

    BEGIN = "begin"
    END = "end"

"""
This module defines the PropertyStereotype enumeration, a subclass of OntoumlEnum, representing different stereotypes
applicable to properties in OntoUML.

Classes:
    PropertyStereotype (OntoumlEnum): Enumerates different stereotypes for properties in OntoUML.
"""

from src.classes.enumerations.ontouml_enum import OntoumlEnum

class PropertyStereotype(OntoumlEnum):
    """
    An enumeration representing different stereotypes applicable to properties in OntoUML.

    This enum classifies various stereotypes that can be assigned to property elements in an OntoUML model. It extends
    OntoumlEnum to leverage automatic CamelCase conversion of member names.

    Members:
        BEGIN: Represents a 'begin' stereotype, typically used for temporal properties.
        END: Represents an 'end' stereotype, often associated with the termination of temporal properties.

    Each member of this enum is automatically converted to CamelCase format upon initialization.

    Methods:
        __init__: Initializes a new member of the PropertyStereotype enum.
    """

    BEGIN = ()
    END = ()

    def __init__(self) -> None:
        """
        Initializes a new member of the PropertyStereotype enum.

        This constructor calls the superclass constructor to ensure the name of the enum member is converted to
        CamelCase format.
        """
        super().__init__()

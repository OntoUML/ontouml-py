"""
This module defines the OntologyRepresentationStyle enumeration, a subclass of OntoumlEnum, for representing different
styles of ontology representation in OntoUML.

Classes:
    OntologyRepresentationStyle (OntoumlEnum): Enumerates different styles of ontology representation.
"""

from src.classes.enumerations.ontouml_enum import OntoumlEnum


class OntologyRepresentationStyle(OntoumlEnum):
    """
    Enumerates different styles of ontology representation in OntoUML.

    This enumeration class inherits from OntoumlEnum and automatically converts its member names to CamelCase format.
    It provides a clear and standardized way to refer to different ontology representation styles.

    Members:
        ONTOUML_STYLE: Represents the OntoUML style of ontology representation.
        UFO_STYLE: Represents the UFO style of ontology representation.
    """

    ONTOUML_STYLE = ()
    UFO_STYLE = ()

    def __init__(self) -> None:
        """
        Initializes a new member of the OntologyRepresentationStyle enum.

        This constructor calls the superclass constructor to ensure the name of the enum member is converted to
        CamelCase format.
        """
        super().__init__()

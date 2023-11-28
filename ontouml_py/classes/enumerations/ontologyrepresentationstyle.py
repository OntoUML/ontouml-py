"""
This module defines the OntologyRepresentationStyle enumeration, a subclass of OntoumlEnum, for representing different
styles of ontology representation in OntoUML.

Classes:
    OntologyRepresentationStyle (OntoumlEnum): Enumerates different styles of ontology representation.
"""

from ontouml_py.classes.enumerations.ontouml_enum import OntoumlEnum


class OntologyRepresentationStyle(OntoumlEnum):
    """
    Enumerates different styles of ontology representation in OntoUML.

    This enumeration class inherits from OntoumlEnum and automatically sets the value of each enum member to a
    CamelCase string corresponding to its name. It provides a clear and standardized way to refer to different ontology
    representation styles.

    :cvar ONTOUML_STYLE: Represents the OntoUML style of ontology representation.
    :vartype ONTOUML_STYLE: str
    :cvar UFO_STYLE: Represents the UFO style of ontology representation.
    :vartype UFO_STYLE: str
    """

    ONTOUML_STYLE = "ontoumlStyle"
    UFO_STYLE = "ufoStyle"

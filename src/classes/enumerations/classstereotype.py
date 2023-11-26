"""
This module defines the ClassStereotype enumeration, a subclass of OntoumlEnum, representing different stereotypes
applicable to classes in OntoUML.

Classes:
    ClassStereotype (OntoumlEnum): Enumerates different stereotypes for classes in OntoUML.
"""

from src.classes.enumerations.ontouml_enum import OntoumlEnum


class ClassStereotype(OntoumlEnum):
    """
    An enumeration representing different stereotypes applicable to classes in OntoUML.

    This enum classifies various stereotypes that can be assigned to class elements in an OntoUML model. It extends
    OntoumlEnum to leverage automatic CamelCase conversion of member names.

    Members:
        ABSTRACT: Represents an abstract stereotype.
        CATEGORY: Represents a category stereotype.
        COLLECTIVE: Represents a collective stereotype.
        DATATYPE: Represents a datatype stereotype.
        ENUMERATION: Represents an enumeration stereotype.
        EVENT: Represents an event stereotype.
        HISTORICAL_ROLE: Represents a historical role stereotype.
        HISTORICAL_ROLE_MIXIN: Represents a historical role mixin stereotype.
        KIND: Represents a kind stereotype.
        MIXIN: Represents a mixin stereotype.
        MODE: Represents a mode stereotype.
        PHASE: Represents a phase stereotype.
        PHASE_MIXIN: Represents a phase mixin stereotype.
        QUALITY: Represents a quality stereotype.
        QUANTITY: Represents a quantity stereotype.
        RELATOR: Represents a relator stereotype.
        ROLE: Represents a role stereotype.
        ROLE_MIXIN: Represents a role mixin stereotype.
        SITUATION: Represents a situation stereotype.
        SUB_KIND: Represents a sub-kind stereotype.
        TYPE: Represents a type stereotype.

    Each member of this enum is automatically converted to CamelCase format upon initialization.

    Methods:
        __init__: Initializes a new member of the ClassStereotype enum.
    """

    ABSTRACT = "abstract"
    CATEGORY = "category"
    COLLECTIVE = "collective"
    DATATYPE = "datatype"
    ENUMERATION = "enumeration"
    EVENT = "event"
    HISTORICAL_ROLE = "historicalRole"
    HISTORICAL_ROLE_MIXIN = "historicalRoleMixin"
    KIND = "kind"
    MIXIN = "mixin"
    MODE = "mode"
    PHASE = "phase"
    PHASE_MIXIN = "phaseMixin"
    QUALITY = "quality"
    QUANTITY = "quantity"
    RELATOR = "relator"
    ROLE = "role"
    ROLE_MIXIN = "roleMixin"
    SITUATION = "situation"
    SUBKIND = "subkind"
    TYPE = "type"

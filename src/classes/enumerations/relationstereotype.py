"""
This module defines the RelationStereotype enumeration, a subclass of OntoumlEnum, representing different stereotypes
applicable to relations in OntoUML.

Classes:
    RelationStereotype (OntoumlEnum): Enumerates different stereotypes for relations in OntoUML.
"""

from src.classes.enumerations.ontouml_enum import OntoumlEnum

class RelationStereotype(OntoumlEnum):
    """
    An enumeration representing different stereotypes applicable to relations in OntoUML.

    This enum classifies various stereotypes that can be assigned to relational elements in an OntoUML model. It extends
    OntoumlEnum to leverage automatic CamelCase conversion of member names.

    Members:
        BRINGS_ABOUT: Represents a 'brings about' stereotype.
        CHARACTERIZATION: Represents a characterization stereotype.
        COMPARATIVE: Represents a comparative stereotype.
        COMPONENT_OF: Represents a 'component of' stereotype.
        CREATION: Represents a creation stereotype.
        DERIVATION: Represents a derivation stereotype.
        EXTERNAL_DEPENDENCE: Represents an 'external dependence' stereotype.
        HISTORICAL_DEPENDENCE: Represents a 'historical dependence' stereotype.
        INSTANTIATION: Represents an instantiation stereotype.
        MANIFESTATION: Represents a manifestation stereotype.
        MATERIAL: Represents a material stereotype.
        MEDIATION: Represents a mediation stereotype.
        MEMBER_OF: Represents a 'member of' stereotype.
        PARTICIPATION: Represents a participation stereotype.
        PARTICIPATIONAL: Represents a participational stereotype.
        SUB_COLLECTION_OF: Represents a 'sub-collection of' stereotype.
        SUB_QUANTITY_OF: Represents a 'sub-quantity of' stereotype.
        TERMINATION: Represents a termination stereotype.
        TRIGGERS: Represents a triggers stereotype.

    Each member of this enum is automatically converted to CamelCase format upon initialization.

    Methods:
        __init__: Initializes a new member of the RelationStereotype enum.
    """

    BRINGS_ABOUT = ()
    CHARACTERIZATION = ()
    COMPARATIVE = ()
    COMPONENT_OF = ()
    CREATION = ()
    DERIVATION = ()
    EXTERNAL_DEPENDENCE = ()
    HISTORICAL_DEPENDENCE = ()
    INSTANTIATION = ()
    MANIFESTATION = ()
    MATERIAL = ()
    MEDIATION = ()
    MEMBER_OF = ()
    PARTICIPATION = ()
    PARTICIPATIONAL = ()
    SUB_COLLECTION_OF = ()
    SUB_QUANTITY_OF = ()
    TERMINATION = ()
    TRIGGERS = ()

    def __init__(self) -> None:
        """
        Initializes a new member of the RelationStereotype enum.

        This constructor calls the superclass constructor to ensure the name of the enum member is converted to
        CamelCase format.
        """
        super().__init__()

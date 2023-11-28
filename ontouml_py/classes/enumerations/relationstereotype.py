"""
This module defines the RelationStereotype enumeration, a subclass of OntoumlEnum, representing different stereotypes
applicable to relations in OntoUML.

Classes:
    RelationStereotype (OntoumlEnum): Enumerates different stereotypes for relations in OntoUML.
"""

from ontouml_py.classes.enumerations.ontouml_enum import OntoumlEnum


class RelationStereotype(OntoumlEnum):
    """An enumeration representing different stereotypes applicable to relations in OntoUML.

    This enum classifies various stereotypes that can be assigned to relational elements in an OntoUML model. It extends
    OntoumlEnum.

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
    """

    BRINGS_ABOUT = "bringsAbout"
    CHARACTERIZATION = "characterization"
    COMPARATIVE = "comparative"
    COMPONENT_OF = "componentOf"
    CREATION = "creation"
    DERIVATION = "derivation"
    EXTERNAL_DEPENDENCE = "externalDependence"
    HISTORICAL_DEPENDENCE = "historicalDependence"
    INSTANTIATION = "instantiation"
    MANIFESTATION = "manifestation"
    MATERIAL = "material"
    MEDIATION = "mediation"
    MEMBER_OF = "memberOf"
    PARTICIPATION = "participation"
    PARTICIPATIONAL = "participational"
    SUB_COLLECTION_OF = "subCollectionOf"
    SUB_QUANTITY_OF = "subQuantityOf"
    TERMINATION = "termination"
    TRIGGERS = "triggers"

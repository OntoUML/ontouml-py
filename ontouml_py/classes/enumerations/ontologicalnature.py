"""This module defines the OntologicalNature enumeration, a subclass of OntoumlEnum, representing different kinds \
of ontological natures in OntoUML."""

from ontouml_py.classes.enumerations.ontouml_enum import OntoumlEnum


class OntologicalNature(OntoumlEnum):
    """An enumeration representing different kinds of ontological natures in OntoUML.

    This enum classifies various ontological natures that can be assigned to elements in an OntoUML model. It extends
    OntoumlEnum.

    Members:
        ABSTRACT_NATURE: Represents an abstract nature.
        COLLECTIVE_NATURE: Represents a collective nature.
        EVENT_NATURE: Represents an event nature.
        EXTRINSIC_MODE_NATURE: Represents an extrinsic mode nature.
        FUNCTIONAL_COMPLEX_NATURE: Represents a functional complex nature.
        INTRINSIC_MODE_NATURE: Represents an intrinsic mode nature.
        QUALITY_NATURE: Represents a quality nature.
        QUANTITY_NATURE: Represents a quantity nature.
        RELATOR_NATURE: Represents a relator nature.
        SITUATION_NATURE: Represents a situation nature.
        TYPE_NATURE: Represents a type nature.
    """

    ABSTRACT_NATURE = "abstractNature"
    COLLECTIVE_NATURE = "collectiveNature"
    EVENT_NATURE = "eventNature"
    EXTRINSIC_MODE_NATURE = "extrinsicModeNature"
    FUNCTIONAL_COMPLEX_NATURE = "functionalComplexNature"
    INTRINSIC_MODE_NATURE = "intrinsicModeNature"
    QUALITY_NATURE = "qualityNature"
    QUANTITY_NATURE = "quantityNature"
    RELATOR_NATURE = "relatorNature"
    SITUATION_NATURE = "situationNature"
    TYPE_NATURE = "typeNature"

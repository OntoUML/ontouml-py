"""
This module defines the OntologicalNature enumeration, a subclass of OntoumlEnum, representing different kinds of
ontological natures in OntoUML.

Classes:
    OntologicalNature (OntoumlEnum): Enumerates different kinds of ontological natures.
"""

from src.classes.enumerations.ontouml_enum import OntoumlEnum


class OntologicalNature(OntoumlEnum):
    """
    An enumeration representing different kinds of ontological natures in OntoUML.

    This enum classifies various ontological natures that can be assigned to elements in an OntoUML model. It extends
    OntoumlEnum to leverage automatic CamelCase conversion of member names.

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

    Each member of this enum is automatically converted to CamelCase format upon initialization.

    Methods:
        __init__: Initializes a new member of the OntologicalNature enum.
    """

    ABSTRACT_NATURE = ()
    COLLECTIVE_NATURE = ()
    EVENT_NATURE = ()
    EXTRINSIC_MODE_NATURE = ()
    FUNCTIONAL_COMPLEX_NATURE = ()
    INTRINSIC_MODE_NATURE = ()
    QUALITY_NATURE = ()
    QUANTITY_NATURE = ()
    RELATOR_NATURE = ()
    SITUATION_NATURE = ()
    TYPE_NATURE = ()

    def __init__(self) -> None:
        """
        Initializes a new member of the OntologicalNature enum.

        This constructor calls the superclass constructor to ensure the name of the enum member is converted to
        CamelCase format.
        """
        super().__init__()

"""
This module defines the AggregationKind enumeration, a subclass of OntoumlEnum, representing different kinds of
aggregation in OntoUML.

Classes:
    AggregationKind (OntoumlEnum): Enumerates different kinds of aggregation.
"""

from src.classes.enumerations.ontouml_enum import OntoumlEnum


class AggregationKind(OntoumlEnum):
    """
    An enumeration representing different kinds of aggregation in OntoUML.

    This enum classifies the kinds of aggregation relationships that can exist in an OntoUML model. It extends
    OntoumlEnum to leverage automatic CamelCase conversion of member names.

    Members:
        NONE: Represents no aggregation.
        COMPOSITE: Represents a composite aggregation.
        SHARED: Represents a shared aggregation.

    Each member of this enum is automatically converted to CamelCase format upon initialization.

    Methods:
        __init__: Initializes a new member of the AggregationKind enum.
    """

    NONE = ()
    COMPOSITE = ()
    SHARED = ()

    def __init__(self) -> None:
        """
        Initializes a new member of the AggregationKind enum.

        This constructor calls the superclass constructor to ensure the name of the enum member is converted to
        CamelCase format.
        """
        super().__init__()

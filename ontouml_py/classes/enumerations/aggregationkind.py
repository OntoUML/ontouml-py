"""
This module defines the AggregationKind enumeration, a subclass of OntoumlEnum, representing different kinds of
aggregation in OntoUML.

Classes:
    AggregationKind (OntoumlEnum): Enumerates different kinds of aggregation.
"""

from ontouml_py.classes.enumerations.ontouml_enum import OntoumlEnum


class AggregationKind(OntoumlEnum):
    """An enumeration representing different kinds of aggregation in OntoUML.

    This enum classifies the kinds of aggregation relationships that can exist in an OntoUML model. It extends
    OntoumlEnum.

    Members:
        NONE: Represents no aggregation.
        COMPOSITE: Represents a composite aggregation.
        SHARED: Represents a shared aggregation.
    """

    NONE = "none"
    COMPOSITE = "composite"
    SHARED = "shared"

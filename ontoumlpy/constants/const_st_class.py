"""This module defines various lists of OntoUML Class Stereotypes used in OntoUML modeling.
Each list represents a specific grouping of stereotypes, providing a convenient way to access.
"""

from ..classes.ontouml import OntoUML

# List of stereotypes that define OntoUML classes as base sortals
OU_CLASS_ST_BASE_SORTALS = [OntoUML.historicalRole, OntoUML.phase, OntoUML.role, OntoUML.subkind]

# List of stereotypes that define OntoUML classes as ultimate sortals
OU_CLASS_ULTIMATE_SORTALS = [
    OntoUML.collective,
    OntoUML.kind,
    OntoUML.mode,
    OntoUML.quality,
    OntoUML.quantity,
    OntoUML.relator,
    OntoUML.type,
]

# List of stereotypes that define OntoUML classes as sortals
OU_CLASS_ST_SORTALS = OU_CLASS_ST_BASE_SORTALS + OU_CLASS_ULTIMATE_SORTALS

# List of stereotypes that define OntoUML classes as non-sortals
OU_CLASS_ST_NON_SORTALS = [
    OntoUML.category,
    OntoUML.historicalRoleMixin,
    OntoUML.mixin,
    OntoUML.phaseMixin,
    OntoUML.roleMixin,
]

# List of stereotypes that define OntoUML classes as abstracts
OU_CLASS_ST_ABSTRACTS = [OntoUML.abstract, OntoUML.datatype, OntoUML.enumeration]

# List of stereotypes that define OntoUML classes as rigids
OU_CLASS_ST_RIGIDS = [
    OntoUML.category,
    OntoUML.collective,
    OntoUML.kind,
    OntoUML.mode,
    OntoUML.quality,
    OntoUML.quantity,
    OntoUML.relator,
    OntoUML.subkind,
]

# List of stereotypes that define OntoUML classes as anti-rigids
OU_CLASS_ST_ANTI_RIGIDS = [
    OntoUML.historicalRole,
    OntoUML.historicalRoleMixin,
    OntoUML.phase,
    OntoUML.phaseMixin,
    OntoUML.role,
    OntoUML.roleMixin,
]

# List of stereotypes that define OntoUML classes as semi-rigids
OU_CLASS_ST_SEMI_RIGIDS = [OntoUML.mixin]

# All OntoUML class's stereotypes defined in the OntoUML profile
OU_CLASS_ST_ALL = (
    OU_CLASS_ST_SORTALS + OU_CLASS_ST_NON_SORTALS + OU_CLASS_ST_ABSTRACTS + [OntoUML.event, OntoUML.situation]
)

"""This module defines various lists of OntoUML Class Stereotypes used in OntoUML modeling.
Each list represents a specific grouping of stereotypes, providing a convenient way to access.
"""

from ..classes.outerm import OUTerm

# List of stereotypes that define OntoUML classes as base sortals
OU_CLASS_ST_BASE_SORTALS = [OUTerm.historicalRole, OUTerm.phase, OUTerm.role, OUTerm.subkind]

# List of stereotypes that define OntoUML classes as ultimate sortals
OU_CLASS_ULTIMATE_SORTALS = [
    OUTerm.collective,
    OUTerm.kind,
    OUTerm.mode,
    OUTerm.quality,
    OUTerm.quantity,
    OUTerm.relator,
    OUTerm.type,
]

# List of stereotypes that define OntoUML classes as sortals
OU_CLASS_ST_SORTALS = OU_CLASS_ST_BASE_SORTALS + OU_CLASS_ULTIMATE_SORTALS

# List of stereotypes that define OntoUML classes as non-sortals
OU_CLASS_ST_NON_SORTALS = [
    OUTerm.category,
    OUTerm.historicalRoleMixin,
    OUTerm.mixin,
    OUTerm.phaseMixin,
    OUTerm.roleMixin,
]

# List of stereotypes that define OntoUML classes as abstracts
OU_CLASS_ST_ABSTRACTS = [OUTerm.abstract, OUTerm.datatype, OUTerm.enumeration]

# List of stereotypes that define OntoUML classes as rigids
OU_CLASS_ST_RIGIDS = [
    OUTerm.category,
    OUTerm.collective,
    OUTerm.kind,
    OUTerm.mode,
    OUTerm.quality,
    OUTerm.quantity,
    OUTerm.relator,
    OUTerm.subkind,
]

# List of stereotypes that define OntoUML classes as anti-rigids
OU_CLASS_ST_ANTI_RIGIDS = [
    OUTerm.historicalRole,
    OUTerm.historicalRoleMixin,
    OUTerm.phase,
    OUTerm.phaseMixin,
    OUTerm.role,
    OUTerm.roleMixin,
]

# List of stereotypes that define OntoUML classes as semi-rigids
OU_CLASS_ST_SEMI_RIGIDS = [OUTerm.mixin]

# All OntoUML class's stereotypes defined in the OntoUML profile
OU_CLASS_ST_ALL = (
        OU_CLASS_ST_SORTALS + OU_CLASS_ST_NON_SORTALS + OU_CLASS_ST_ABSTRACTS + [OUTerm.event, OUTerm.situation]
)

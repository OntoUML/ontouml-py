from ..classes.class_term import OUTerm

OU_CLASS_ST_BASE_SORTALS = [OUTerm.historicalRole, OUTerm.phase, OUTerm.role, OUTerm.subkind]

OU_CLASS_ULTIMATE_SORTALS = [
    OUTerm.collective,
    OUTerm.kind,
    OUTerm.mode,
    OUTerm.quality,
    OUTerm.quantity,
    OUTerm.relator,
    OUTerm.type,
]

OU_CLASS_ST_SORTALS = OU_CLASS_ST_BASE_SORTALS + OU_CLASS_ULTIMATE_SORTALS

OU_CLASS_ST_NON_SORTALS = [
    OUTerm.category,
    OUTerm.historicalRoleMixin,
    OUTerm.mixin,
    OUTerm.phaseMixin,
    OUTerm.roleMixin,
]

OU_CLASS_ST_ABSTRACTS = [OUTerm.abstract, OUTerm.datatype, OUTerm.enumeration]

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

OU_CLASS_ST_ANTI_RIGIDS = [
    OUTerm.historicalRole,
    OUTerm.historicalRoleMixin,
    OUTerm.phase,
    OUTerm.phaseMixin,
    OUTerm.role,
    OUTerm.roleMixin,
]

OU_CLASS_ST_SEMI_RIGIDS = [OUTerm.mixin]

OU_CLASS_ST_ALL = (
        OU_CLASS_ST_SORTALS + OU_CLASS_ST_NON_SORTALS + OU_CLASS_ST_ABSTRACTS + [OUTerm.event, OUTerm.situation]
)

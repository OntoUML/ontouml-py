"""This module defines various OntoUML Class Stereotypes used in OntoUML modeling.

Each enumeration represents a specific grouping of stereotypes, providing a convenient and
semantically meaningful way to access and utilize the stereotypes in OntoUML modeling.
"""

from ontoumlpy.classes.ontouml import OntoUML
from ontoumlpy.classes.ouenumeration._ouenumeration import _OUEnumeration


class OUBaseSortalClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as base sortals."""

    historicalRole = OntoUML.historicalRole
    phase = OntoUML.phase
    role = OntoUML.role
    subkind = OntoUML.subkind


class OUUltimateSortalClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as ultimate sortals."""

    collective = OntoUML.collective
    kind = OntoUML.kind
    mode = OntoUML.mode
    quality = OntoUML.quality
    quantity = OntoUML.quantity
    relator = OntoUML.relator
    type = OntoUML.type


class OUSortalClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as sortals.
    Combines base sortals and ultimate sortals.
    """

    historicalRole = OntoUML.historicalRole
    phase = OntoUML.phase
    role = OntoUML.role
    subkind = OntoUML.subkind
    collective = OntoUML.collective
    kind = OntoUML.kind
    mode = OntoUML.mode
    quality = OntoUML.quality
    quantity = OntoUML.quantity
    relator = OntoUML.relator
    type = OntoUML.type


class OUNonSortalClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as non-sortals."""

    category = OntoUML.category
    historicalRoleMixin = OntoUML.historicalRoleMixin
    mixin = OntoUML.mixin
    phaseMixin = OntoUML.phaseMixin
    roleMixin = OntoUML.roleMixin


class OUAbstractClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as abstracts."""

    abstract = OntoUML.abstract
    datatype = OntoUML.datatype
    enumeration = OntoUML.enumeration


class OURigidClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as rigids."""

    category = OntoUML.category
    collective = OntoUML.collective
    kind = OntoUML.kind
    mode = OntoUML.mode
    quality = OntoUML.quality
    quantity = OntoUML.quantity
    relator = OntoUML.relator
    subkind = OntoUML.subkind


class OUAntiRigidClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as anti-rigids."""

    historicalRole = OntoUML.historicalRole
    historicalRoleMixin = OntoUML.historicalRoleMixin
    phase = OntoUML.phase
    phaseMixin = OntoUML.phaseMixin
    role = OntoUML.role
    roleMixin = OntoUML.roleMixin


class OUSemiRigidClass(_OUEnumeration):
    """An enumeration representing OntoUML class stereotypes defined as semi-rigids."""

    mixin = OntoUML.mixin


class OUClassStereotype(_OUEnumeration):
    """An enumeration representing all OntoUML class stereotypes defined in the OntoUML profile.
    Combines sortals, non-sortals, and abstracts, and also adds event and situation stereotypes.
    """

    abstract = OntoUML.abstract
    category = OntoUML.category
    collective = OntoUML.collective
    datatype = OntoUML.datatype
    enumeration = OntoUML.enumeration
    event = OntoUML.event
    historicalRole = OntoUML.historicalRole
    historicalRoleMixin = OntoUML.historicalRoleMixin
    kind = OntoUML.kind
    mixin = OntoUML.mixin
    mode = OntoUML.mode
    phase = OntoUML.phase
    phaseMixin = OntoUML.phaseMixin
    quality = OntoUML.quality
    quantity = OntoUML.quantity
    relator = OntoUML.relator
    role = OntoUML.role
    roleMixin = OntoUML.roleMixin
    situation = OntoUML.situation
    subkind = OntoUML.subkind
    type = OntoUML.type

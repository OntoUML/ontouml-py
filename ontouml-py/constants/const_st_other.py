"""The `class_st_other` module defines lists of OntoUML Stereotypes that categorize relations and properties.
"""

from ontoumlpy.classes.outerm import OUTerm

# List of OntoUML stereotypes associated with relations.
OU_RELATION_STS = [
    OUTerm.bringsAbout,
    OUTerm.characterization,
    OUTerm.comparative,
    OUTerm.componentOf,
    OUTerm.creation,
    OUTerm.derivation,
    OUTerm.externalDependence,
    OUTerm.historicalDependence,
    OUTerm.instantiation,
    OUTerm.manifestation,
    OUTerm.material,
    OUTerm.mediation,
    OUTerm.memberOf,
    OUTerm.participation,
    OUTerm.participational,
    OUTerm.subCollectionOf,
    OUTerm.subQuantityOf,
    OUTerm.termination,
    OUTerm.triggers,
]

# List of OntoUML stereotypes associated with properties.
OU_PROPERTY_STS = [OUTerm.begin, OUTerm.end]

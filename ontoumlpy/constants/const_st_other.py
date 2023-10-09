"""The `class_st_other` module defines lists of OntoUML Stereotypes that categorize relations and properties.
"""

from ontoumlpy.classes.ontouml import OntoUML

# List of OntoUML stereotypes associated with relations.
OU_RELATION_STS = [
    OntoUML.bringsAbout,
    OntoUML.characterization,
    OntoUML.comparative,
    OntoUML.componentOf,
    OntoUML.creation,
    OntoUML.derivation,
    OntoUML.externalDependence,
    OntoUML.historicalDependence,
    OntoUML.instantiation,
    OntoUML.manifestation,
    OntoUML.material,
    OntoUML.mediation,
    OntoUML.memberOf,
    OntoUML.participation,
    OntoUML.participational,
    OntoUML.subCollectionOf,
    OntoUML.subQuantityOf,
    OntoUML.termination,
    OntoUML.triggers,
]

# List of OntoUML stereotypes associated with properties.
OU_PROPERTY_STS = [OntoUML.begin, OntoUML.end]

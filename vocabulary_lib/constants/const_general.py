from ..classes.class_term import OUTerm

ONTOUML_NAMESPACE = "https://w3id.org/ontouml#"
ONTOUML_SPARQL_PREFIX = "PREFIX ontouml: <https://w3id.org/ontouml#> "

OU_AGGREGATION_KINDS = [OUTerm.composite, OUTerm.none, OUTerm.shared]

OU_ONTOLOGICAL_NATURES = [
    OUTerm.abstractNature,
    OUTerm.collectiveNature,
    OUTerm.eventNature,
    OUTerm.extrinsicModeNature,
    OUTerm.functionalComplexNature,
    OUTerm.intrinsicModeNature,
    OUTerm.qualityNature,
    OUTerm.quantityNature,
    OUTerm.relatorNature,
    OUTerm.situationNature,
    OUTerm.typeNature,
]

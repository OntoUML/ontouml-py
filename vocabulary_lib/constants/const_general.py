"""This module contains general Python constants related to the OntoUML vocabulary and concepts.
These constants are designed to facilitate working with OntoUML terms and concepts in Python code.
"""

from ..classes.class_term import OUTerm

# The OntoUML namespace URI. This constant defines the URI for the OntoUML namespace used in RDF triples.
ONTOUML_NAMESPACE = "https://w3id.org/ontouml#"

# Prefix to be included in SPARQL queries to access OntoUML concepts via 'ontouml:'.
ONTOUML_SPARQL_PREFIX = "PREFIX ontouml: <https://w3id.org/ontouml#> "

# List of OntoUML Aggregation Kinds.
OU_AGGREGATION_KINDS = [OUTerm.composite, OUTerm.none, OUTerm.shared]

# List of OntoUML Ontological Natures.
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

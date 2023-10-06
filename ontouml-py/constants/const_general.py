"""This module contains general Python constants related to the OntoUML vocabulary and concepts.
These constants are designed to facilitate working with OntoUML terms and concepts in Python code.
"""
from ..classes.outerm import OUTerm

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

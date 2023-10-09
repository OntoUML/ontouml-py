"""This module contains general Python constants related to the OntoUML vocabulary and concepts.
These constants are designed to facilitate working with OntoUML terms and concepts in Python code.
"""
from ..classes.ontouml import OntoUML

# List of OntoUML Aggregation Kinds.
OU_AGGREGATION_KINDS = [OntoUML.composite, OntoUML.none, OntoUML.shared]

# List of OntoUML Ontological Natures.
OU_ONTOLOGICAL_NATURES = [
    OntoUML.abstractNature,
    OntoUML.collectiveNature,
    OntoUML.eventNature,
    OntoUML.extrinsicModeNature,
    OntoUML.functionalComplexNature,
    OntoUML.intrinsicModeNature,
    OntoUML.qualityNature,
    OntoUML.quantityNature,
    OntoUML.relatorNature,
    OntoUML.situationNature,
    OntoUML.typeNature,
]

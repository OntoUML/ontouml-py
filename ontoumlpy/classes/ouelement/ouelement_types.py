"""This module provides Python classes that represent concepts defined in the OntoUML Vocabulary.
This module provides Python classes for representing and manipulating concepts from the OntoUML Vocabulary.
These Python classes facilitate working with OntoUML concepts and enable you to interact with OntoUML-based data.
Usage:
# Instantiate a class concept from the OntoUML model
person_class = OUClass(ontouml_graph, URIRef("https://example.org/Person"))
# Access attributes of the class
print(f"Class Name: {person_class.name}")
print(f"Description: {person_class.description}")
print(f"Attributes: {person_class.attribute}")
You can perform similar operations for other OntoUML concepts using their respective classes.
"""

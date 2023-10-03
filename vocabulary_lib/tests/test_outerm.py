"""This module contains a series of tests to validate the mapping and type correctness of the OUTerm class
which represents OntoUML vocabulary terms as URI references.
"""

import rdflib

from ..classes.outerm import OUTerm


def test_class_outerm_mapping_pos() -> None:
    """Tests the correct URI mapping of selected OUTerm instances."""
    assert str(OUTerm.aggregationKind) == "https://w3id.org/ontouml#aggregationKind"
    assert str(OUTerm.AggregationKind) == "https://w3id.org/ontouml#AggregationKind"
    assert str(OUTerm.yCoordinate) == "https://w3id.org/ontouml#yCoordinate"


def test_class_outerm_mapping_neg() -> None:
    """Ensures incorrect URI mappings are not validated for selected OUTerm instances."""
    assert str(OUTerm.abstract) != "http://w3id.org/ontouml#abstract"
    assert str(OUTerm.collective) != "https://3id.org/ontouml#collective"
    assert str(OUTerm.yCoordinate) != "https://w3id.org/ontouml#ycoordinate"


def test_class_outerm_type_pos() -> None:
    """Tests the type correctness of selected OUTerm instances."""
    assert isinstance(OUTerm.memberOf, str)
    assert isinstance(OUTerm.yCoordinate, rdflib.term.URIRef)
    assert isinstance(OUTerm.typeNature, rdflib.term.URIRef)


def test_class_outerm_type_neg() -> None:
    """Ensures incorrect type assignments are not validated for selected OUTerm instances."""
    assert not (isinstance(OUTerm.memberOf, float))
    assert not (isinstance(OUTerm.yCoordinate, bool))
    assert not (isinstance(OUTerm.typeNature, int))

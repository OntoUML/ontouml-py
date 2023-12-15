import pytest
from icecream import ic

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.cardinality import Cardinality
from ontouml_py.model.class_ontouml import Class
from ontouml_py.model.generalization import Generalization
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.literal import Literal
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.package import Package
from ontouml_py.model.project import Project
from ontouml_py.model.property import Property


@pytest.fixture
def valid_project():
    return Project()


@pytest.fixture
def valid_anchor(valid_project, valid_note):
    return Anchor(valid_project, note=valid_note, target=valid_note)


@pytest.fixture
def valid_binary_relation(valid_project):
    return BinaryRelation(valid_project)


@pytest.fixture
def valid_cardinality():
    return Cardinality()


@pytest.fixture
def valid_class(valid_project):
    return Class(project=valid_project)


@pytest.fixture
def valid_generalization(valid_project, valid_class):
    return Generalization(project=valid_project, general=valid_class, specific=valid_class)


@pytest.fixture
def valid_generalization_set(valid_project):
    return GeneralizationSet(project=valid_project)


@pytest.fixture
def valid_literal(valid_class):
    return Literal(enumeration=valid_class)


@pytest.fixture
def valid_nary_relation(valid_project):
    return NaryRelation(project=valid_project)


@pytest.fixture
def valid_note(valid_project):
    return Note(valid_project)


@pytest.fixture
def valid_package(valid_project):
    return Package(valid_project)


@pytest.fixture
def valid_property(valid_class):
    return Property(valid_class)


def test_fixtures_instantiations(
    valid_project,
    valid_note,
    valid_anchor,
    valid_binary_relation,
    valid_cardinality,
    valid_class,
    valid_generalization,
    valid_generalization_set,
    valid_literal,
    valid_nary_relation,
    valid_package,
    valid_property,
):
    assert valid_anchor
    assert valid_binary_relation
    assert valid_cardinality
    assert valid_class
    assert valid_generalization
    assert valid_generalization_set
    assert valid_literal
    assert valid_nary_relation
    assert valid_note
    assert valid_project
    assert valid_package
    assert valid_property

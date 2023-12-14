import pytest

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.note import Note
from ontouml_py.model.project import Project


@pytest.fixture
def project():
    return Project()

@pytest.fixture
def valid_note(project):
    return Note(project)

@pytest.fixture
def valid_anchor(project, valid_note):
    return Anchor(project, note=valid_note, target=valid_note)
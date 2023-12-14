import pytest
from pydantic import ValidationError

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.class_py import Class
from ontouml_py.model.enumerations.classstereotype import ClassStereotype
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.package import Package


@pytest.mark.parametrize(
    "target_type, create_target",
    [
        (Class, lambda project: Class(project, stereotype=ClassStereotype.KIND)),
        (BinaryRelation, lambda project: BinaryRelation(project)),
        (NaryRelation, lambda project: NaryRelation(project)),
        (GeneralizationSet, lambda project: GeneralizationSet(project)),
        (Package, lambda project: Package(project)),
    ]
)
def test_anchor_initialization_with_various_model_elements(project, valid_note, target_type, create_target):
    target = create_target(project)
    anchor = Anchor(project, note=valid_note, target=target)
    assert anchor.note == valid_note and anchor.target == target, "Anchor should be initialized with the correct note and target"

@pytest.mark.parametrize("missing_param", ["note", "target"])
def test_anchor_initialization_without_mandatory_params(project, valid_note, missing_param):
    params = {"note": valid_note, "target": valid_note}
    params.pop(missing_param)
    with pytest.raises(ValidationError, match=f"Field required"):
        Anchor(project, **params)

def test_anchor_attribute_assignment_post_initialization(project, valid_note):
    anchor = Anchor(project, note=valid_note, target=valid_note)
    new_note = Note(project)
    new_target = Class(project)
    anchor.note = new_note
    anchor.target = new_target
    assert anchor.note == new_note, "Anchor attribute 'note' should be assignable post initialization"
    assert anchor.target == new_target, "Anchor attribute 'target' should be assignable post initialization"


def test_anchor_initialization_with_invalid_types(project, valid_note):
    with pytest.raises(ValidationError, match="Input should be a valid"):
        Anchor(project, note="not_a_note", target=valid_note)

    with pytest.raises(ValidationError, match="Input should be a valid"):
        Anchor(project, note=valid_note, target="not_a_model_element")

def test_anchor_initialization_with_extra_fields(project, valid_note):
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        Anchor(project, note=valid_note, target=valid_note, extra_field="extra_value")

def test_anchor_retrieval_by_id(project, valid_note):
    anchor = Anchor(project, note=valid_note, target=valid_note)
    retrieved_anchor = project.get_element_by_id("Anchor", anchor.id)
    assert retrieved_anchor == anchor, "Should retrieve the same Anchor instance from the project"

import pytest
from pydantic import ValidationError

from ontouml_py.model.anchor import Anchor
from ontouml_py.model.binaryrelation import BinaryRelation
from ontouml_py.model.class_ontouml import Class
from ontouml_py.model.enumerations.classstereotype import ClassStereotype
from ontouml_py.model.generalizationset import GeneralizationSet
from ontouml_py.model.naryrelation import NaryRelation
from ontouml_py.model.note import Note
from ontouml_py.model.package import Package


@pytest.mark.parametrize(
    "target_type, create_target",
    [
        (Class, lambda valid_project: Class(valid_project, stereotype=ClassStereotype.KIND)),
        (BinaryRelation, lambda valid_project: BinaryRelation(valid_project)),
        (NaryRelation, lambda valid_project: NaryRelation(valid_project)),
        (GeneralizationSet, lambda valid_project: GeneralizationSet(valid_project)),
        (Package, lambda valid_project: Package(valid_project)),
    ],
)
def test_anchor_initialization_with_various_model_elements(valid_project, valid_note, target_type, create_target):
    target = create_target(valid_project)
    anchor = Anchor(valid_project, note=valid_note, target=target)
    assert (
        anchor.note == valid_note and anchor.target == target
    ), "Anchor should be initialized with the correct note and target"


@pytest.mark.parametrize("missing_param", ["note", "target"])
def test_anchor_initialization_without_mandatory_params(valid_project, valid_note, missing_param):
    params = {"note": valid_note, "target": valid_note}
    params.pop(missing_param)
    with pytest.raises(ValidationError, match=f"Field required"):
        Anchor(valid_project, **params)


def test_anchor_attribute_assignment_post_initialization(valid_project, valid_note):
    anchor = Anchor(valid_project, note=valid_note, target=valid_note)
    new_note = Note(valid_project)
    new_target = Class(valid_project)
    anchor.note = new_note
    anchor.target = new_target
    assert anchor.note == new_note, "Anchor attribute 'note' should be assignable post initialization"
    assert anchor.target == new_target, "Anchor attribute 'target' should be assignable post initialization"


def test_anchor_initialization_with_invalid_types(valid_project, valid_note):
    with pytest.raises(ValidationError, match="Input should be a valid"):
        Anchor(valid_project, note="not_a_note", target=valid_note)

    with pytest.raises(ValidationError, match="Input should be a valid"):
        Anchor(valid_project, note=valid_note, target="not_a_model_element")


def test_anchor_initialization_with_extra_fields(valid_project, valid_note):
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        Anchor(valid_project, note=valid_note, target=valid_note, extra_field="extra_value")


def test_anchor_retrieval_by_id(valid_project, valid_note):
    anchor = Anchor(valid_project, note=valid_note, target=valid_note)
    retrieved_anchor = valid_project.get_element_by_id("Anchor", anchor.id)
    assert retrieved_anchor == anchor, "Should retrieve the same Anchor instance from the project"

from ontouml_py.model.generalization import Generalization
from ontouml_py.model.modelelement import ModelElement


def test_model_element_initialization_through_subclass(valid_project, valid_class):
    """Test the initialization of a ModelElement subclass.

    :param valid_project: A fixture for a valid Project instance.
    :param valid_class: A fixture for a valid Class instance.
    """
    generalization = Generalization(project=valid_project, general=valid_class, specific=valid_class)
    assert isinstance(generalization, ModelElement)
    assert generalization.custom_properties == set()


def test_custom_properties_in_model_element_subclass(valid_project, valid_class):
    """Test handling custom properties in a ModelElement subclass.

    :param valid_project: A fixture for a valid Project instance.
    :param valid_class: A fixture for a valid Class instance.
    """
    generalization = Generalization(project=valid_project, general=valid_class, specific=valid_class)
    generalization.custom_properties.add(("key1", "value1"))
    generalization.custom_properties.add(("key2", "value2"))

    assert ("key1", "value1") in generalization.custom_properties
    assert ("key2", "value2") in generalization.custom_properties

    # Modify a custom property
    generalization.custom_properties.remove(("key1", "value1"))
    generalization.custom_properties.add(("key1", "new_value1"))
    assert ("key1", "new_value1") in generalization.custom_properties

    # Remove a custom property
    generalization.custom_properties.remove(("key2", "value2"))
    assert ("key2", "value2") not in generalization.custom_properties

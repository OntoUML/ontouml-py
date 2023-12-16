from ontouml_py.model.generalization import Generalization


def test_generalization_initialization(valid_project, valid_class):
    """Test the initialization of a Generalization instance with valid classifiers.

    :param valid_project: A fixture for a valid Project instance.
    :param valid_class: A fixture for a valid Class instance.
    """
    generalization = Generalization(project=valid_project, general=valid_class, specific=valid_class)
    assert generalization.general == valid_class
    assert generalization.specific == valid_class
    assert generalization.project == valid_project


def test_assignment_of_classifiers_to_generalization(valid_project, valid_class, another_valid_class):
    """Test the assignment of different classifiers to a Generalization instance.

    :param valid_project: A fixture for a valid Project instance.
    :param valid_class: A fixture for a valid Class instance.
    :param another_valid_class: Another fixture for a valid Class instance.
    """
    generalization = Generalization(project=valid_project, general=valid_class, specific=another_valid_class)
    assert generalization.general == valid_class
    assert generalization.specific == another_valid_class


def test_modifying_classifiers_in_generalization(valid_project, valid_class, another_valid_class):
    """Test modifying the classifiers of a Generalization instance after initialization.

    :param valid_project: A fixture for a valid Project instance.
    :param valid_class: A fixture for a valid Class instance.
    :param another_valid_class: Another fixture for a valid Class instance.
    """
    generalization = Generalization(project=valid_project, general=valid_class, specific=valid_class)
    generalization.general = another_valid_class
    generalization.specific = valid_class
    assert generalization.general == another_valid_class
    assert generalization.specific == valid_class

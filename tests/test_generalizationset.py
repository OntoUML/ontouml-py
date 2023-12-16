from ontouml_py.model.generalizationset import GeneralizationSet


def test_generalization_set_initialization(valid_project):
    """Test the initialization of a GeneralizationSet instance with default values.

    :param valid_project: A fixture for a valid Project instance.
    """
    gen_set = GeneralizationSet(project=valid_project)
    assert not gen_set.is_disjoint
    assert not gen_set.is_complete
    assert gen_set.generalizations == set()
    assert gen_set.categorizer is None
    assert gen_set.project == valid_project


def test_generalization_set_initialization_with_parameters(valid_project):
    """Test the initialization of a GeneralizationSet instance with specified values.

    :param valid_project: A fixture for a valid Project instance.
    """
    gen_set = GeneralizationSet(project=valid_project, is_disjoint=True, is_complete=True)
    assert gen_set.is_disjoint
    assert gen_set.is_complete


def test_assignment_of_attributes_to_generalization_set(valid_project, valid_class, valid_generalization):
    """Test the assignment of different attributes to a GeneralizationSet instance.

    :param valid_project: A fixture for a valid Project instance.
    :param valid_class: A fixture for a valid Class instance.
    :param valid_generalization: A fixture for a valid Generalization instance.
    """
    gen_set = GeneralizationSet(project=valid_project)
    gen_set.is_disjoint = True
    gen_set.is_complete = True
    gen_set.generalizations.add(valid_generalization)
    gen_set.categorizer = valid_class

    assert gen_set.is_disjoint
    assert gen_set.is_complete
    assert valid_generalization in gen_set.generalizations
    assert gen_set.categorizer == valid_class

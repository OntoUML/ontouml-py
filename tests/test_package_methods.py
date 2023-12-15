import pytest


@pytest.mark.parametrize(
    "content_type, add_method, getter_method, fixture_name",
    [
        ("Anchor", "add_anchor", "get_anchors", "valid_anchor"),
        ("BinaryRelation", "add_binary_relation", "get_binary_relations", "valid_binary_relation"),
        ("Class", "add_class", "get_classes", "valid_class"),
        ("Generalization", "add_generalization", "get_generalizations", "valid_generalization"),
        ("GeneralizationSet", "add_generalization_set", "get_generalization_sets", "valid_generalization_set"),
        ("NaryRelation", "add_nary_relation", "get_nary_relations", "valid_nary_relation"),
        ("Note", "add_note", "get_notes", "valid_note"),
        ("Package", "add_package", "get_packages", "valid_package"),
    ],
)
def test_add_content_methods(valid_package, content_type, add_method, getter_method, fixture_name, request):
    """
    Test adding content using methods defined in PackageMethodsMixin.

    :param valid_package: A valid Package instance.
    :param content_type: The type of content to be tested.
    :param add_method: The method name for adding content.
    :param getter_method: The method name for getting content.
    :param fixture_name: The name of the fixture representing the content instance.
    :param request: Pytest fixture request object for accessing other fixtures.
    :return: None
    """
    content_instance = request.getfixturevalue(fixture_name)
    getattr(valid_package, add_method)(content_instance)
    assert (
        content_instance in getattr(valid_package, getter_method)()
    ), f"{content_type} should be added to the package."


@pytest.mark.parametrize(
    "content_type, get_by_id_method, fixture_name",
    [
        ("Anchor", "get_anchor_by_id", "valid_anchor"),
        ("BinaryRelation", "get_binary_relation_by_id", "valid_binary_relation"),
        ("Class", "get_class_by_id", "valid_class"),
        ("Generalization", "get_generalization_by_id", "valid_generalization"),
        ("GeneralizationSet", "get_generalization_set_by_id", "valid_generalization_set"),
        ("NaryRelation", "get_nary_relation_by_id", "valid_nary_relation"),
        ("Note", "get_note_by_id", "valid_note"),
        ("Package", "get_package_by_id", "valid_package"),
    ],
)
def test_get_content_by_id_methods(valid_package, content_type, get_by_id_method, request, fixture_name):
    """
    Test retrieving content by ID using methods defined in PackageMethodsMixin.

    :param valid_package: A valid Package instance.
    :param content_type: The type of content to be tested.
    :param get_by_id_method: The method name for retrieving content by ID.
    :param request: Pytest fixture request object for accessing other fixtures.
    :param fixture_name: The name of the fixture for the content instance.
    :return: None
    """
    content_instance = request.getfixturevalue(fixture_name)
    valid_package._contents[content_type].add(content_instance)
    retrieved_content = getattr(valid_package, get_by_id_method)(content_instance.id)
    assert retrieved_content == content_instance, f"Should retrieve the correct {content_type} instance by ID."


@pytest.mark.parametrize(
    "content_type, add_method, fixture_name",
    [
        ("Anchor", "add_anchor", "valid_anchor"),
        ("BinaryRelation", "add_binary_relation", "valid_binary_relation"),
        ("Class", "add_class", "valid_class"),
        ("Generalization", "add_generalization", "valid_generalization"),
        ("GeneralizationSet", "add_generalization_set", "valid_generalization_set"),
        ("NaryRelation", "add_nary_relation", "valid_nary_relation"),
        ("Note", "add_note", "valid_note"),
        ("Package", "add_package", "valid_package"),
    ],
)
def test_add_duplicate_content_methods(valid_package, content_type, add_method, fixture_name, request):
    """
    Test adding duplicate content using methods defined in PackageMethodsMixin.
    """
    content_instance = request.getfixturevalue(fixture_name)
    getattr(valid_package, add_method)(content_instance)

    # Construct the correct getter method name

    if content_type in ["BinaryRelation", "NaryRelation"]:
        lower_content_type = content_type.lower()
        new_content = lower_content_type.replace("relation", "_relations")
        getter_method = f"get_{new_content}"
    elif content_type == "GeneralizationSet":
        lower_content_type = content_type.lower()
        new_content = lower_content_type.replace("set", "_sets")
        getter_method = f"get_{new_content}"
    elif content_type == "Class":
        getter_method = "get_classes"
    else:
        getter_method = f"get_{content_type.lower()}s"

    # Get the size of the set before attempting to add the duplicate
    initial_size = len(getattr(valid_package, getter_method)())

    # Attempt to add the same instance again
    getattr(valid_package, add_method)(content_instance)

    # Check if the size of the set remains the same
    final_size = len(getattr(valid_package, getter_method)())
    assert initial_size == final_size, "Adding a duplicate should not increase the size of the set."


@pytest.mark.parametrize(
    "get_by_id_method, invalid_id",
    [
        ("get_anchor_by_id", "invalid_id"),
        # ... other content types with their respective get_by_id methods
    ],
)
def test_get_nonexistent_content_by_id_methods(valid_package, get_by_id_method, invalid_id):
    """
    Test retrieving non-existent content by ID using methods defined in PackageMethodsMixin.

    :param valid_package: A valid Package instance.
    :param get_by_id_method: The method name for retrieving content by ID.
    :param invalid_id: An invalid ID to test with.
    :return: None
    """
    retrieved_content = getattr(valid_package, get_by_id_method)(invalid_id)
    assert retrieved_content is None, "Should not retrieve any content with a non-existent ID."


# Additional tests for invalid content type and null/invalid ID can be added similarly

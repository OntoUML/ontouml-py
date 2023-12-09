from typing import Optional

import pytest
from pydantic import ValidationError

from ontouml_py.model.enumerations.ontologyrepresentationstyle import OntologyRepresentationStyle
from ontouml_py.model.project import Project


@pytest.mark.parametrize(
    "namespace, representation_style, expected_values",
    [
        (
            None,
            OntologyRepresentationStyle.ONTOUML_STYLE,
            {"namespace": None, "representation_style": OntologyRepresentationStyle.ONTOUML_STYLE},
        ),
        (
            "http://example.com",
            OntologyRepresentationStyle.UFO_STYLE,
            {"namespace": "http://example.com", "representation_style": OntologyRepresentationStyle.UFO_STYLE},
        ),
    ],
)
def test_project_initialization(
    namespace: str, representation_style: OntologyRepresentationStyle, expected_values: dict
) -> None:
    """Test the initialization of a Project with both default and custom values."""
    project = Project(namespace=namespace, representation_style=representation_style)
    assert all(
        getattr(project, attr) == value for attr, value in expected_values.items()
    ), "Project attributes should match the expected values"


def test_project_invalid_namespace() -> None:
    """Test the Project initialization with an invalid namespace."""
    with pytest.raises(ValidationError, match="Input should be a valid string"):
        Project(namespace=123)  # Namespace should be a string


def test_project_invalid_representation_style() -> None:
    """Test the Project initialization with an invalid representation style."""
    with pytest.raises(ValidationError, match="Input should be 'ontoumlStyle' or 'ufoStyle'"):
        Project(representation_style="invalid_style")  # Invalid enum member


@pytest.mark.parametrize(
    "acronyms, expected_acronyms",
    [
        ({"AI", "ML"}, {"AI", "ML"}),
        (set(), set()),
    ],
)
def test_project_acronyms_initialization(acronyms: set[str], expected_acronyms: set[str]) -> None:
    """Test the initialization of a Project with different sets of acronyms.

    :param acronyms: Set of acronyms to initialize the Project with.
    :param expected_acronyms: Expected set of acronyms in the Project.
    """
    project = Project(acronyms=acronyms)
    assert project.acronyms == expected_acronyms, "Project acronyms should match the expected values"


@pytest.mark.parametrize(
    "keywords, expected_keywords",
    [
        ({"ontology", "modeling"}, {"ontology", "modeling"}),
        (set(), set()),
    ],
)
def test_project_keywords_initialization(keywords: set[str], expected_keywords: set[str]) -> None:
    """Test the initialization of a Project with different sets of keywords.

    :param keywords: Set of keywords to initialize the Project with.
    :param expected_keywords: Expected set of keywords in the Project.
    """
    project = Project(keywords=keywords)
    assert project.keywords == expected_keywords, "Project keywords should match the expected values"


@pytest.mark.parametrize(
    "languages, expected_languages",
    [
        ({"en", "pt"}, {"en", "pt"}),
        (set(), set()),
    ],
)
def test_project_languages_initialization(languages: set[str], expected_languages: set[str]) -> None:
    """Test the initialization of a Project with different sets of languages.

    :param languages: Set of languages to initialize the Project with.
    :param expected_languages: Expected set of languages in the Project.
    """
    project = Project(languages=languages)
    assert project.languages == expected_languages, "Project languages should match the expected values"


@pytest.mark.parametrize(
    "license, expected_license",
    [
        ("MIT", "MIT"),
        (None, None),
    ],
)
def test_project_license_initialization(license: Optional[str], expected_license: Optional[str]) -> None:
    """Test the initialization of a Project with different license values.

    :param license: License string to initialize the Project with.
    :param expected_license: Expected license string in the Project.
    """
    project = Project(license=license)
    assert project.license == expected_license, "Project license should match the expected value"


@pytest.mark.parametrize(
    "publisher, expected_publisher",
    [
        ("OpenAI", "OpenAI"),
        (None, None),
    ],
)
def test_project_publisher_initialization(publisher: Optional[str], expected_publisher: Optional[str]) -> None:
    """Test the initialization of a Project with different publisher values.

    :param publisher: Publisher string to initialize the Project with.
    :param expected_publisher: Expected publisher string in the Project.
    """
    project = Project(publisher=publisher)
    assert project.publisher == expected_publisher, "Project publisher should match the expected value"


def test_project_invalid_acronyms_type() -> None:
    """Test the Project initialization with an invalid acronyms type."""
    with pytest.raises(ValidationError, match="Input should be a valid set"):
        Project(acronyms="invalid_type")  # Acronyms should be a set


def test_project_invalid_keywords_type() -> None:
    """Test the Project initialization with an invalid keywords type."""
    with pytest.raises(ValidationError, match="Input should be a valid set"):
        Project(keywords="invalid_type")  # Keywords should be a set


def test_project_invalid_languages_type() -> None:
    """Test the Project initialization with an invalid languages type."""
    with pytest.raises(ValidationError, match="Input should be a valid set"):
        Project(languages="invalid_type")  # Languages should be a set


def test_project_invalid_license_type() -> None:
    """Test the Project initialization with an invalid license type."""
    with pytest.raises(ValidationError, match="Input should be a valid string"):
        Project(license=123)  # License should be a string


def test_project_invalid_publisher_type() -> None:
    """Test the Project initialization with an invalid publisher type."""
    with pytest.raises(ValidationError, match="Input should be a valid string"):
        Project(publisher=123)  # Publisher should be a string


@pytest.mark.parametrize(
    "bibliographic_citations, expected_citations",
    [
        ({"citation1", "citation2"}, {"citation1", "citation2"}),
        (set(), set()),
    ],
)
def test_project_bibliographic_citations_initialization(
    bibliographic_citations: set[str], expected_citations: set[str]
) -> None:
    """Test the initialization of a Project with different sets of bibliographic citations.

    :param bibliographic_citations: Set of bibliographic citations to initialize the Project with.
    :param expected_citations: Expected set of bibliographic citations in the Project.
    """
    project = Project(bibliographic_citations=bibliographic_citations)
    assert (
        project.bibliographic_citations == expected_citations
    ), "Project bibliographic citations should match the expected values"


@pytest.mark.parametrize(
    "landing_pages, expected_landing_pages",
    [
        ({"http://example.com", "http://example.org"}, {"http://example.com", "http://example.org"}),
        (set(), set()),
    ],
)
def test_project_landing_pages_initialization(landing_pages: set[str], expected_landing_pages: set[str]) -> None:
    """Test the initialization of a Project with different sets of landing pages.

    :param landing_pages: Set of landing pages to initialize the Project with.
    :param expected_landing_pages: Expected set of landing pages in the Project.
    """
    project = Project(landing_pages=landing_pages)
    assert project.landing_pages == expected_landing_pages, "Project landing pages should match the expected values"


def test_project_invalid_bibliographic_citations_type() -> None:
    """Test the Project initialization with an invalid bibliographic citations type."""
    with pytest.raises(ValidationError, match="Input should be a valid set"):
        Project(bibliographic_citations="invalid_type")  # Bibliographic citations should be a set


def test_project_invalid_landing_pages_type() -> None:
    """Test the Project initialization with an invalid landing pages type."""
    with pytest.raises(ValidationError, match="Input should be a valid set"):
        Project(landing_pages="invalid_type")  # Landing pages should be a set

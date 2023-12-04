[![Project Status - Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![GitHub - Release Date - PublishedAt](https://img.shields.io/github/release-date/ontouml/ontouml-py)
![GitHub - Last Commit - Branch](https://img.shields.io/github/last-commit/ontouml/ontouml-py/main)
![PyPI - Project](https://img.shields.io/pypi/v/ontouml-py)
![Language - Top](https://img.shields.io/github/languages/top/ontouml/ontouml-py)
![Language - Version](https://img.shields.io/pypi/pyversions/ontouml-py)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/ontouml/ontouml-py)
![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/OntoUML/ontouml-py/badge)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License - GitHub](https://img.shields.io/github/license/ontouml/ontouml-py)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/OntoUML/ontouml-py/main.svg)](https://results.pre-commit.ci/latest/github/OntoUML/ontouml-py/main)
![Website](https://img.shields.io/website/http/ontouml.github.io/ontouml-py.svg)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/ontouml/ontouml-py/code_testing.yml)

# ontouml-py

**WORK IN PROGRESS**

<p align="center"><img src="https://raw.githubusercontent.com/OntoUML/ontouml-py/main/ontouml-py/resources/logo-ontouml-py.png" width="740"></p>

**📦 PyPI Package:**
The transformation is conveniently [available as a PyPI package](https://pypi.org/project/ontouml-py/), which
allows users to use it as an executable script or import it as a library into other Python projects.

**📚 Documentation:**
For inquiries and further information, please refer to the [comprehensive docstring-generated documentation](https://w3id.org/ontouml/ontouml-py/docs) available for this project.

## Contents

<!-- TOC -->
* [ontouml-py](#ontouml-py)
  * [Contents](#contents)
  * [Installation and Use](#installation-and-use)
    * [Prerequisites](#prerequisites)
    * [Instructions for Users](#instructions-for-users)
    * [Instructions for Contributors](#instructions-for-contributors)
  * [Development Stage:](#development-stage)
  * [The OntoUML-JS](#the-ontouml-js)
  * [How to Contribute](#how-to-contribute)
    * [Report Issues](#report-issues)
    * [Code Contribution](#code-contribution)
    * [Test Contribution](#test-contribution)
    * [General Guidelines](#general-guidelines)
  * [Author](#author)
<!-- TOC -->

## Installation and Use

### Prerequisites

Ensure you have Python installed on your system before utilizing `ontouml-py`. It has been tested with Python versions 3.9 to 3.12 on Mac, Windows, and Linux. If not installed, [download and install Python](https://www.python.org/downloads/).

### Instructions for Users

1. Install ontouml-py: Execute the following command to install the library:

```shell
pip install ontouml-py
```

All dependencies will be installed automatically.

2. Usage: To use ontouml-py, import the necessary functionalities in your Python code. Example:

```python
from ontouml_py import AnOntoumlClass
```

Note: Replace `AnOntoumlClass` with the actual class you intend to use.

### Instructions for Contributors

1. **Fork the Project:**
   Fork the `ontouml-py` repository to your own GitHub account.

2. **Clone and Setup:**
   Clone your forked repository and navigate to the project directory.

3. **Install Dependencies:**
   Use [Poetry](https://python-poetry.org/) for dependency management. If not installed, refer to Poetry’s [documentation](https://python-poetry.org/docs/#installation) for installation instructions. Then, install all dependencies with:
   ```shell
   poetry install
   ```

Now, you're ready to make enhancements or fixes and contribute back to ontouml-py!

## Development Stage:

ontouml-py is still under active development.

Your contributions and feedback are valuable in enhancing ontouml-py and expanding its capabilities!

## The OntoUML-JS

[OntoUML JS](https://github.com/OntoUML/ontouml-js) is a versatile JavaScript library tailored for effortlessly handling OntoUML models. It streamlines the process of manipulating OntoUML models and serializing them into [`ontouml-schema`](https://github.com/OntoUML/ontouml-schema) compliant JSON files. With OntoUML JS, developers can efficiently create and manage OntoUML elements, construct models, and perform various model-related tasks programmatically. This library introduces constructor methods for creating OntoUML elements, provides support for container elements like projects and packages, and facilitates element serialization and deserialization. Additionally, OntoUML JS is continually updated with useful methods to simplify the development of OntoUML models. Whether you are working on ontology-driven conceptual modeling or require a tool for handling complex domain ontologies, OntoUML JS offers a valuable utility to streamline your workflow.

## How to Contribute

### Report Issues

- Report bugs or suggest features by [opening an issue](https://github.com/OntoUML/ontouml-py/issues/new).
- Point out any discrepancies in the AI-generated documentation by [opening an issue](https://github.com/OntoUML/ontouml-py/issues/new).

### Code Contribution

1. Fork the Repository: Fork the project repository and create your feature branch: `git checkout -b feature/YourFeatureName`.
2. Commit Changes: Make and commit your changes with meaningful commit messages.
3. Push to Branch: Push your work back up to your fork: `git push origin feature/YourFeatureName`.
4. Submit a Pull Request: Open a pull request to merge your feature branch into the main project repository.

### Test Contribution

- Improve reliability by adding or enhancing tests.

### General Guidelines

- Ensure your code adheres to our coding standards.
- Update documentation as needed.
- Ensure that your code does not introduce additional issues.

Thank you for investing your time and expertise into this project!

## Author

This project is maintained by the [Semantics, Cybersecurity & Services (SCS) Group](https://www.utwente.nl/en/eemcs/scs/) of the [University of Twente](https://www.utwente.nl/), The Netherlands. Its developer is:

- [Pedro Paulo Favato Barcelos](https://orcid.org/0000-0003-2736-7817) [[GitHub](https://github.com/pedropaulofb)] [[LinkedIn](https://www.linkedin.com/in/pedro-paulo-favato-barcelos/)]

Feel free to get in touch using the provided links. For questions, contributions, or to report any problem, you can **[open an issue](https://github.com/OntoUML/ontouml-py/issues/new)** at this repository.

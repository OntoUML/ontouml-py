"""This module provides functionality for managing documentation within the project.

It includes functions for generating, cleaning, and copying Sphinx documentation.

The module is designed for software developers and maintainers to streamline documentation tasks.
"""
import os
import shutil
import subprocess
import sys

from loguru import logger


def execute_documentation_commands() -> None:
    """Execute a sequence of documentation-related commands.

    This function orchestrates a series of commands to generate and manage Sphinx documentation:
        1. Remove the 'docs' directory and its contents.
        2. Create a new 'docs' directory.
        3. Clean the Sphinx documentation build.
        4. Build the Sphinx HTML documentation.
        5. Copy the HTML documentation to the 'docs' directory.
        6. Clean the Sphinx documentation build again.

    If any command fails, the function raises an exception and stops the execution.
    """
    # Define the base directory
    base_dir = os.getcwd()  # Use the current working directory

    # Define paths to directories and commands
    sphinx_dir = os.path.join(base_dir, "sphinx")
    docs_dir = os.path.join(base_dir, "docs")

    logger.info("Deleting and creating again the existing docs/ directory")
    try:
        # Use shutil.rmtree to remove the directory and its contents
        if os.path.exists(docs_dir):
            shutil.rmtree(docs_dir)
            logger.info(f"Directory '{docs_dir}' and its contents have been successfully removed.")
        os.makedirs(docs_dir, exist_ok=True)
        logger.info(f"Empty directory '{docs_dir}' has been successfully created.")
    except OSError as e:
        logger.exception(f"Error: {e}")

    logger.info("Executing commands 'make clean' and 'make html' sequentially")
    try:
        subprocess.run(["make", "clean"], cwd=sphinx_dir, shell=True, check=True)
        subprocess.run(["make", "html"], cwd=sphinx_dir, shell=True, check=True)
        logger.info("Commands 'make clean' and 'make html' successfully executed.")
    except subprocess.CalledProcessError as e:
        logger.exception(f"Commands 'make clean' and 'make html' failed with return code {e.returncode}: {e.cmd}")
        sys.exit(1)
    except Exception as e:  # pylint: disable=W0718
        logger.exception(f"An error occurred: {e}")
        sys.exit(1)

    try:
        sphinx_dir_html = os.path.join(sphinx_dir, "_build", "html")
        # Copy the contents of the source directory to the destination directory
        shutil.copytree(sphinx_dir_html, docs_dir, dirs_exist_ok=True)
        logger.info(f"Contents of '{sphinx_dir_html}' copied to '{docs_dir}' successfully.")
    except Exception as e:  # pylint: disable=W0718
        logger.exception(f"Error: {e}")

    logger.info("Executing command 'make clean'")
    try:
        subprocess.run(["make", "clean"], cwd=sphinx_dir, shell=True, check=True)
        logger.info("Commands 'make clean' and 'make html' successfully executed.")
    except subprocess.CalledProcessError as e:
        logger.exception(f"Commands 'make clean' and 'make html' failed with return code {e.returncode}: {e.cmd}")
        sys.exit(1)
    except Exception as e:  # pylint: disable=W0718
        logger.exception(f"An error occurred: {e}")
        sys.exit(1)

    logger.info("Documentation commands executed successfully.")


if __name__ == "__main__":
    execute_documentation_commands()

"""This module provides utilities for formatting and displaying error messages in applications.

The primary functionality is centered around the `format_error_message` function, which is designed to create clear, \
informative, and actionable error messages. This function takes details about an error (such as its type, a detailed \
description, its cause, and suggested solutions) and formats them into a user-friendly message. This can be \
particularly useful for logging errors in a consistent format or providing users with helpful feedback when exceptions \
occur.

Functions:
    format_error_message(error_type: str, description: str, cause: str, solution: str) -> str
        Formats a detailed error message based on provided parameters.

Example:
    format_error_message(
        description="The application failed to connect to the database.",
        cause="Invalid database credentials provided.",
        solution="Check and update the database credentials in the configuration file."
    )

Note:
    This module is intended for use in both development and production environments to enhance error reporting \
    and handling.
"""


def format_error_message(description: str = "undefined", cause: str = "undefined", solution: str = "undefined") -> str:
    """Format a detailed error message.

    This function takes four string parameters describing various aspects of an error and prints a formatted error
    message to the console. It is designed to provide clear and actionable information to the user about errors
    that occur within the application.

    :param description: A detailed description of what the error is. This should provide specific \
    information about the nature of the error.
    :type description: str
    :param cause: The cause of the error. This should explain why the error occurred, to the best of the \
    function's knowledge.
    :type cause: str
    :param solution: Suggested steps to resolve the error. This should offer clear guidance on how to fix the \
    issue or mitigate its effects.
    :type solution: str
    :return: Formatted error message.
    """
    return f"""
            \n* Description: {description}
            \n* Cause: {cause}
            \n* Solution: {solution}\n
            """

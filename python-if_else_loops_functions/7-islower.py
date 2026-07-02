#!/usr/bin/python3
"""Module that checks if a character is lowercase."""


def islower(c):
    """Check if a character is lowercase.

    Args:
        c (str): the character to check.

    Returns:
        True if c is lowercase, False otherwise.
    """
    return ord(c) >= ord('a') and ord(c) <= ord('z')

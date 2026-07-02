#!/usr/bin/python3
"""Module that prints a string in uppercase."""


def uppercase(str):
    """Print a string in uppercase followed by a new line.

    Args:
        str (str): the string to print in uppercase.
    """
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()

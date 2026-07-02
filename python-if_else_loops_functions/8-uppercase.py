#!/usr/bin/python3
"""Module that prints a string in uppercase."""


def uppercase(str):
    """Print a string in uppercase followed by a new line.

    Args:
        str (str): the string to print in uppercase.
    """
    ustr = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            ustr += chr(ord(c) - 32)
        else:
            ustr += c
    print("{}".format(ustr))

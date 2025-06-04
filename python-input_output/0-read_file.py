#!/usr/bin/python3
"""
This module defines a function that reads a text file (UTF8)
and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

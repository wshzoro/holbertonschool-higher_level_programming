#!/usr/bin/python3
"""
Module 0-lookup
Contains the function lookup which returns the list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: List of strings representing attributes and methods of obj.
    """
    return dir(obj)

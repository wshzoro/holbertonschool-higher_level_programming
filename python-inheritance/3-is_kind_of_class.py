#!/usr/bin/python3

"""
Contains function is_kind_of_class that check if
an object is an instance of a class or a class
that inherited from it
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of a_class or a subclass of it
    Otherwhise, returns False
    """
    return isinstance(obj, a_class)

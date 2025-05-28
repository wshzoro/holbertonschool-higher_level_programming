#!/usr/bin/python3

"""
Contains the function inherits_from that checkif the object
is an instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    from the specified class
    Otherwise, return False.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class

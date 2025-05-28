#!/usr/bin/python3
"""
Contains function is_same_class that check if an object
is exactly  an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly
    an instance of a_class
    Otherwise, returns False
    """
    return type(obj) is a_class

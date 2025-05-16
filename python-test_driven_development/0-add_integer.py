#!/usr/bin/python3
"""
Module 0-add_integer
Provides a function that adds two integers.

Functions:
    add_integer(a, b=98): Adds two integers or floats (casted to int),
    raises TypeError if arguments are not int or float.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (casts floats to int before addition).

    Args:
        a (int or float): First number to add.
        b (int or float, optional): Second number to add (default is 98).

    Raises:
        TypeError: If either a or b is not an int or float.

    Returns:
        int: The sum of a and b casted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

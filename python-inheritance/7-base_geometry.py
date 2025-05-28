#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with validation method.
"""

class BaseGeometry:
    """
    BaseGeometry class with area() and integer_validator() methods.
    """

    def area(self):
        """
        Raises an exception since area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

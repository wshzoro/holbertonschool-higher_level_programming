#!/usr/bin/python3
"""
Module 8-rectangle
Defines class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height

        Args:
            width (int): width of rectangle (validated)
            height (int): height of rectangle (validated)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        String representation of the Rectangle instance
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

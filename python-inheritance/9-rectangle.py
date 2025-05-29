#!/usr/bin/python3
"""
Module 9-rectangle
Defines class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height (validated)

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

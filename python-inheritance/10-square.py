#!/usr/bin/python3
"""
Module 10-square
Defines class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with size, validated as a positive integer

        Args:
            size (int): size of the square sides
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

#!/usr/bin/python3
"""
Module 11-square
Defines class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize a new Square instance

        Args:
            size (int): The size of the square's sides
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the square description: [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"

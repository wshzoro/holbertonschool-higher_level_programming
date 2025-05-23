#!/usr/bin/python3
"""Define a Square class with size as a number and comparison operators."""


class Square:
    """Represents a square with a numeric size."""

    def __init__(self, size=0):
        """Initialize the square with size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, validating it's a number and >= 0."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    # Comparison operators based on area
    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

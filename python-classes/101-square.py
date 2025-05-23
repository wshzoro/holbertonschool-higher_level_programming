#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): The size of the square sides.
            position (tuple): The position of the square (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, validating it is an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, validating it is a tuple of 2 positive integers."""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character # respecting the position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the print behavior: same as my_print."""
        if self.__size == 0:
            return ""
        lines = []
        lines.extend(["" for _ in range(self.__position[1])])
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
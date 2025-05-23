#!/usr/bin/python3
"""Module that defines a Square class with size,
area computation, and printing capability using '#' characters.
"""


class Square:
    """Represents a square with a controllable size."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): Size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: Current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): New size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

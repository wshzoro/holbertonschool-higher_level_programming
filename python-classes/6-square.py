#!/usr/bin/python3
"""Module that defines a Square class with size, position,
area computation, and printing capability using '#' characters.
"""


class Square:
    """Represents a square with a controllable size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position.

        Args:
            size (int): Size of the square (default is 0).
            position (tuple): Position offset (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square as a tuple (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character and position offset.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

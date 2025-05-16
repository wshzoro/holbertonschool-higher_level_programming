#!/usr/bin/python3
"""
Module 2-matrix_divided
Provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): Matrix of integers/floats.
        div (int or float): Number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of int/float.
        TypeError: If rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: New matrix with elements divided and rounded to 2 decimals.

    Examples:
        >>> matrix = [[1, 2], [3, 4]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0], [1.5, 2.0]]
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]

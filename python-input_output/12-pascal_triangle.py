#!/usr/bin/python3
"""Pascal's Triangle implementation."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start with 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])  # Sum of two numbers above
        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle

#!/usr/bin/env python3
"""Gets the transpose of a matrix"""


def matrix_transpose(matrix):
    """
    Calculates the transpose of a 2D matrix.

    Args:
        matrix (list): A 2D list representing a matrix.

    Returns:
        list: A new 2D list representing the transpose of the input matrix.

    Example:
        >>> matrix_transpose([[1, 2], [3, 4]])
        [[1, 3], [2, 4]]
    """
    return [list(col) for col in zip(*matrix)]

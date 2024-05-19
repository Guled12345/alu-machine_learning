
#!/usr/bin/env python3
"""A function calculating shape of a matrix"""


def matrix_shape(matrix):
    """
    Args:
        matrix (list): A nested list representing a matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.

    Example:
        >>> matrix_shape([[1, 2], [3, 4]])
        [2, 2]
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape

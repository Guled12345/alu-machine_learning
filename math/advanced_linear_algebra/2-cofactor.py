#!/usr/bin/env python3

"""
This module has the function cofactor(matrix)
"""

minor = __import__('1-minor').minor


def cofactor(matrix):
    """
    Calculate the cofactor of a matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError('matrix must be a list of lists')

    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError('matrix must be a non-empty square matrix')

    if len(matrix) == 1:
        return [[1]]
    elif len(matrix) == 2:
        return [[matrix[1][1], -matrix[1][0]], [-matrix[0][1], matrix[0][0]]]
    elif len(matrix) == 3:
        a = (matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])
        b = (matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])
        c = (matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])
        d = (matrix[0][1] * matrix[2][2]) - (matrix[0][2] * matrix[2][1])
        e = (matrix[0][0] * matrix[2][2]) - (matrix[0][2] * matrix[2][0])
        f = (matrix[0][0] * matrix[2][1]) - (matrix[0][1] * matrix[2][0])
        g = (matrix[0][1] * matrix[1][2]) - (matrix[0][2] * matrix[1][1])
        h = (matrix[0][0] * matrix[1][2]) - (matrix[0][2] * matrix[1][0])
        i = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        result = [[a, -b, c], [-d, e, -f], [g, -h, i]]
        return result
    else:
        num_rows = len(matrix)
        minor_mat = minor(matrix)  # Calculate the minor matrix first
        cofactor_mat = []

        for i in range(num_rows):
            cofactor_row = []
            for j in range(num_rows):
                # Determine the sign based on the position (even/odd)
                sign = (-1) ** (i + j)
                # Multiply sign by the corresponding minor
                cofactor_element = sign * minor_mat[i][j]
                cofactor_row.append(cofactor_element)
            cofactor_mat.append(cofactor_row)

        return cofactor_mat

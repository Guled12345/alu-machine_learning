#!/usr/bin/env python3
"""function minor(matrix)"""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """
    Calculate the minor of a matrix
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
        return [[matrix[1][1], matrix[1][0]], [matrix[0][1], matrix[0][0]]]
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
        result = [[a, b, c], [d, e, f], [g, h, i]]
        return result
    else:
        minor_mat = []
        for i in range(len(matrix)):
            minor_row = []
            for j in range(len(matrix)):
                submatrix = [row[:j] + row[j + 1:]
                             for row in (matrix[:i] + matrix[i + 1:])]
                minor_row.append(determinant(submatrix))
            minor_mat.append(minor_row)
        return minor_mat

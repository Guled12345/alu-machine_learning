#!/usr/bin/env python3
"""Determinant of a matrix"""


def determinant(matrix):
    """
    Find the determinant of a (0,0) matrix
    Arg:
    matrix
    Returns:
        Determinant of the matrix
    """
    if matrix == [[]]:
        return 1
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError('matrix must be a list of lists')
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError('matrix must be a square matrix')

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3:
        val1 = matrix[0][0] * matrix[1][1] * matrix[2][2]
        val2 = matrix[0][1] * matrix[1][2] * matrix[2][0]
        val3 = matrix[0][2] * matrix[1][0] * matrix[2][1]

        val4 = matrix[0][2] * matrix[1][1] * matrix[2][0]
        val5 = matrix[0][1] * matrix[1][0] * matrix[2][2]
        val6 = matrix[0][0] * matrix[1][2] * matrix[2][1]

        result = (val1 + val2 + val3) - (val4 + val5 + val6)
        return result
    else:
        det = 0
        for i in range(len(matrix)):
            cofactor = matrix[0][i] * determinant(get_minor(matrix, 0, i))
            if i % 2 == 0:
                det += cofactor
            else:
                det -= cofactor
        return det


def get_minor(matrix, row, col):
    """
    calculating minor of a matrix
    """
    return [[matrix[i][j] for j in range(len(matrix))
             if j != col] for i in range(len(matrix)) if i != row]

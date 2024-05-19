#!/usr/bin/env python3
"""Adds matrices element wise"""


def add_matrices2D(mat1, mat2):
    """
    Adds two matrices  element wise

    Args:
        mat1, mat2

    Returns:
        list: A new 2D list representing the sum of two matrices.

    """
    if len(mat1[0]) != len(mat2[0]):
        return None
    else:
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[0])):
                row.append(mat1[i][j] + mat2[i][j])
            result.append(row)
        return result
    
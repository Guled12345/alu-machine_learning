#!/usr/bin/env python3
"""Concat along axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1: 2D matrix containing ints/floats.
        mat2: 2D matrix containing ints/floats.
        axis (int): Axis along which to concatenate the matrices. Default is 0.

    Returns:
        list: A new matrix containing elements of mat1 concatenated
    with mat2 along the specified axis.
              Returns None if the matrices cannot be concatenated.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
    
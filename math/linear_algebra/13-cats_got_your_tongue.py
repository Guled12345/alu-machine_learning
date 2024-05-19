#!/usr/bin/env python3
"""Concate"""
import numpy as np
def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray.
        axis (int): Axis along which to concatenate.
    Returns:
        numpy.ndarray: A new matrix containing the concatenated matrices.
    """
    return np.concatenate((mat1, mat2), axis=axis)



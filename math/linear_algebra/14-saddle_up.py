#!/usr/bin/env python3
"""np_mult"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication.

    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray.

    Returns:
        numpy.ndarray: The result of multiplying mat1 with mat2.
    """
    return np.dot(mat1, mat2)

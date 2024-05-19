#!/usr/bin/env python3
"""Adds two arrays element wise"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element wise

    Args:
        arr1, arr2

    Returns:
        list: A new 2D list representing the sum of two arrays.

    """
    if len(arr1) != len(arr2):
        return None
    else:
        result = []
        for i in range(len(arr1)):
            result.append(arr1[i] + arr2[i])
        return result
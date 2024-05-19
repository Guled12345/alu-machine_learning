
#!/usr/bin/env python3
"""Elementwise perform"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise sums

    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray.

    Returns:
    sum, mult, div, diff
    """
    sums = mat1 + mat2
    diff = mat1 - mat2
    product = mat1 * mat2
    quotient = mat1 / mat2
    return sums, diff, product, quotient

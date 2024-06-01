#!/usr/bin/env python3
"""Sigma summation"""


def summation_i_squared(n):
    """
    Calculates the sigma(sum)
    Arg: n(integer)
    Returns:
    integer value of sum
    """
    if type(n) != int or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6

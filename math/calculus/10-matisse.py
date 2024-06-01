#!/usr/bin/env python3
"""Derivatives of polynomials"""


def poly_derivative(poly):
    """
    calculates the derivative of a polynomial
    poly is a list of coefficients representing a polynomial
    the index of the list represents the power of x
    that the coefficient belongs to

    Example:
    if f(x) = x^3 + 3x +5, poly is equal to [5, 3, 0, 1]

    Returns:
    None: if poly is not valid
    [0]: If the derivative is 0
    new list of coefficients representing the derivative
    """
    derivative = []
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    for i in range(len(poly)-1, 0, -1):

        derivative.append(poly[i]*i)
    return derivative[::-1]

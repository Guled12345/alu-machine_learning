#!/usr/bin/env python3
"""Importing numpy"""
import numpy as np
"""Function to calculate likelihood of data"""


def likelihood(x, n, P):
    """
    x is the number of patients that develop severe side effects
    n is the total number of patients observed
    P is a 1D numpy.ndarray containing the various hypothetical
    probabilities of developing severe side effects
    Raises:
        ValueError: n is not positive integer
        If x is not an integer that is greater than or equal to 0
        If x is greater than n
        If any value in P is not in the range [0, 1]
        TypeError: If P is not a 1D numpy.ndarray
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is "
                         "greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    # Calculate likelihood for each probability in P
    fact_n = 1
    for i in range(1, n + 1):
        fact_n *= i

    fact_x = 1
    for i in range(1, x + 1):
        fact_x *= i

    fact_nx = 1
    for i in range(1, n - x + 1):
        fact_nx *= i

    likelihood = (fact_n / (fact_x * fact_nx)) * (P ** x) *\
        ((1 - P) ** (n - x))

    return likelihood

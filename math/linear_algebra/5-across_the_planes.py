#!/usr/bin/env python3
'''This script contains a function that adds matrices element wise.
'''
def add_matrices2D(mat1, mat2):
    ''' This function adds matrices element wise.
        mat1: The first matrix
        mat2: The second matrix
        Returns: A new matrix and
        None if the matrices are not of the same shape.
    '''
    if len(mat1) != len(mat2):
        return None
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
# Creating a new matrix with the element wise sums.
    return[[a + b for a, b in zip(row1, row2)]
           for row1, row2 in zip(mat1, mat2)]
    
    
    
    
    

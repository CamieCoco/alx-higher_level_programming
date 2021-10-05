#!/usr/bin/python3
"""
This module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Returns a new matrix.
    The new matrix will be all the elements of matrix divided by div.
    """
    new_matrix = []
    flinterr = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(flinterr)
    for i in range(0, len(matrix)):
        matrix_nums = []
        if type(matrix[i]) is not list:
            raise TypeError(flinterr)
        for nums in matrix[i]:
            if type(nums) is not int and type(nums) is not float:
                raise TypeError(flinterr)
            matrix_nums.append(round(nums / div, 2))
        if i > 0 and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(matrix_nums)
    return new_matrix

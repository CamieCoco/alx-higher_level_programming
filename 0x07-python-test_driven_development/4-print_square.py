#!/usr/bin/python3
"""
This module contains a function that prints a square.
"""


def print_square(size):
    """
    This function prints a square with the octothorpe character.
    The size of the square depends on the size passed to the function.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")
    for row in range(0, size):
        print("#" * size)

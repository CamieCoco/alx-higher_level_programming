#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
If one or both arguments passed are floats, they will be first cast into ints.
"""


def add_integer(a, b=98):
    """
    This function returns the sum of arguments a and b.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

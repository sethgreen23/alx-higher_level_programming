#!/usr/bin/python3
"""Module that adds 2 integers"""


def add_integer(a, b=98):
    """
    Adding two numbers a and b

    Parameters:
        a (int, float): first variable
        b (int, float): second variable

    Return:
        int: The sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

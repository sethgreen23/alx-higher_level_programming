#!/usr/bin/python3
"""Print square Module"""


def print_square(size):
    """
    Print a square with size 'size' using #

    Parameters:
        size (int): size of the square

    Return:
        Nothing
    """

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + '\n') * size, end="")

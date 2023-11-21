#!/usr/bin/python3
"""Module squre"""


class Square:
    """
    Class defining a square.

    Attributes:
        size (float): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initilizes a square object.

        Parameters:
            size (float): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Return:
            float: current square area.
        """
        return (self.__size**2)

    @property
    def size(self):
        """Return the value of the instance size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a value the the instance variable size"""
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        self.__size = value

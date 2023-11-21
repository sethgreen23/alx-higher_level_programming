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
        """Provide the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        self.__size = value

    def my_print(self):
        """Print the square"""
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()

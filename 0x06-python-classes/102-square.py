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
        self.size = size

    def area(self):
        """
        Calculate the area of the square.

        Return:
            float: current square area.
        """
        return (self.size * self.size)

    @property
    def size(self):
        """Return the value of the instance size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a value the the instance variable size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Compare two objects"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __lt__(self, other):
        """Compare two objects"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Compare two objects"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __ne__(self, other):
        """Compare two objects"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare two objects"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare two objects"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

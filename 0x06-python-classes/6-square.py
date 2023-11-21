#!/usr/bin/python3
"""Module squre"""


class Square:
    """
    Class defining a square.

    Attributes:
        size (float): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initilizes a square object.

        Parameters:
            size (float): The size of the square.
            position (float, float): The square position.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not Square.is_positive_tuple(position):
            print(position)
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @staticmethod
    def is_positive_tuple(value):
        """check if the tuple is positive two tuple"""
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and value[0] >= 0 \
                   and isinstance(value[1], int) and value[1] >= 0:
                    return True
        return False

    def area(self):
        """
        Calculate the area of the square.

        Return:
            float: current square area.
        """
        return self.__size**2

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

    @property
    def position(self):
        """Provide the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not Square.is_positive_tuple(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square"""
        if self.size == 0:
            print()
            return

        for _ in range(self.size):
            if self.position[1] >= 0:
                print(" "*self.position[0], end="")
            for _ in range(self.size):
                print("#", end="")
            print()

#!/usr/bin/python3
"""Square Module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        Initialise Square Object

        Parameters:
            size (int): size of a square
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate area of a square"""
        return self.__size * self.__size

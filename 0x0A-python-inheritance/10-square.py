#!/usr/bin/python3
"""Square Module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Rectangle
    """

    def init(self, size):
        """
        Initialise Square Object

        Parameters:
            size (int): size of a square
        """

        super().__init__(size, size)

#!/usr/bin/python3
"""Module related to class rectagles and its functions"""


class Rectangle:
    """
    This is a class rectagle

    Attributes:
        width (int): with of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Init function of the class Rectangle

        Parameter:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function for the width

        Parameters:
            value (int): width of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter function for the height

        Parameters:
            value (int): height of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def height(self):
        """getter function for height"""

        return self.__height

#!/usr/bin/python3
"""Rectagle Module"""


class BaseGeometry:
    """
    Class BaseGeometry

    """

    def area(self):
        """Calculate the area of BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value

        Parameters:
            name (string): name of the value
            value (integer): value

        Return:
            Nothing
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class Rectanle

    Parameters:
        width (integer): width
        height (integer): height
    """

    def __init__(self, width, height):
        """
        Init function for Rectangle Class

        Parameters:
            width (integer): width
            height (integer): height

        Return: Nothing
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

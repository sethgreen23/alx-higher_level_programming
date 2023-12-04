#!/usr/bin/python3
"""Rectagle Module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

#!/usr/bin/python3
"""Geometry Modul"""


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

        if value.__class__ != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

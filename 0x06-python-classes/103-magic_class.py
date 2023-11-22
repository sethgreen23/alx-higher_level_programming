#!/usr/bin/python3
"""Module MagicClass"""


import math


class MagicClass:
    """
    A class representing a magic

    Attributes:
        radius (float): The radius of the circle
    """

    def __init__(self, radius):
        """
        Initilizes a Cicle object.

        Parameters:
            radius (float): The radius of the circle
        """

        self._MagicClass__radius = 0
        if type(radius) is not int:
            raise TypeError("radius must be a number")
        if type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate the area of a circle"""
        return self._MagicClass__radius**2 * math.pi

    def circumference(self):
        """Calculate circonference of a circle"""
        return 2 * math.pi * self._MagicClass__radius

#!/usr/bin/python3
"""Class inherit from int"""


class MyInt(int):
    """
    Class that inherit from int
    """

    def __eq__(self, other):
        """Equal method"""
        return not str(self) == str(other)

    def __ne__(self, other):
        """Different method"""
        return not str(self) != str(other)

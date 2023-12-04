#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """
    Class the inherit from list class
    """

    def print_sorted(self):
        """Print elements of the list"""
        sorted_list = sorted(self)
        print(sorted_list)

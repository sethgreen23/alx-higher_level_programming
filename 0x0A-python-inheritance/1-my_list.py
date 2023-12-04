#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """
    Class the inherit from list class
    """

    def print_sorted(self):
        self.sort()

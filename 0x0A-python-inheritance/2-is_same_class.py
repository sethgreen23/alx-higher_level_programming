#!/usr/bin/python3
"""Same Class Module"""


def is_same_class(obj, a_class):
    """Test if obj same class of a_class"""
    if isinstance(obj, a_class):
        return True;
    return False

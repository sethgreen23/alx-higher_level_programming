#!/usr/bin/python3
"""Module to determine subclass"""


def inherits_from(obj, a_class):
    """Is object is subclass"""
    return issubclass(obj.__class__, a_class) and type(obj) != a_class

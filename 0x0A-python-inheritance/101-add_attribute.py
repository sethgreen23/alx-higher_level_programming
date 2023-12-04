#!/usr/bin/python3
"""Add attributes"""

def add_attribute(obj, attribute, value):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)

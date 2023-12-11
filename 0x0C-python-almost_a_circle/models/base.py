#!/usr/bin/python3
"""Base class Module"""

import json


class Base:
    """
    Class Base

    Parameters:
        id (int): instance attribute integer
        nb_objects (int): class attribute integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init function"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def set_nb_objects(cls):
        """Class method to set the value of nb_objest to zero"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that return string representation
        of list_dictonaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

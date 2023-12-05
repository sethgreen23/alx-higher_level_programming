#!/usr/bin/python3
"""Student class Module"""


class Student:
    """
    Class Student

    Instances:
        first_name (string): first name
        last_name (string): last name
        age (int): age
    """

    def __init__(self, first_name, last_name, age):
        """
        Method that instantiate objects

        Parameters:
            first_name (string): string
            last_name (string): string
            age (int): int
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """from class to json"""

        if attrs is None:
            return self.__dict__
        all_str = all(isinstance(element, str) for element in attrs)
        if not all_str:
            return self.__dict__
        dictionary = {}
        for key in attrs:
            if key in self.__dict__:
                dictionary[key] = self.__dict__[key]
        return dictionary

    def reload_from_json(self, json):
        """reload object from json"""
        if not json:
            return

        for key, value in self.__dict__.items():
            if key in self.__dict__:
                self.__dict__[key] = json[key]

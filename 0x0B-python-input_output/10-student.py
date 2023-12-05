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
        contain_str = any(type(element) == str for element in attrs)
        if not contain_str:
            return self.__dict__
        dictionary = {}
        for key in attrs:
            if key in self.__dict__:
                dictionary[key] = self.__dict__[key]
        return dictionary

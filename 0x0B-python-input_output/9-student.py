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

    def to_json(self):
        """from class to json"""

        return self.__dict__

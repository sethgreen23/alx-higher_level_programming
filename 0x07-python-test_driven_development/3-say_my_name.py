#!/usr/bin/python3
"""Say my name module"""


def say_my_name(first_name, last_name=""):
    """
    Print a person presentation

    Parameters:
        first_name (str): first name
        last_name (str): last name

    Return:
        Nothing
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {:s}".format(first_name))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))

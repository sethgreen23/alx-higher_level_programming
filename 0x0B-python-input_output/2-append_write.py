#!/usr/bin/python3
"""Append Module"""


def append_write(filename="", text=""):
    """
    Append to a file

    Parameters:
        filename (string): filename
        text (string): text

    Return: Nothing
    """

    char_numbers = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        char_numbers = f.write(text)
    return char_numbers

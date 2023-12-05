#!/usr/bin/python3
"""Write Module"""


def write_file(filename="", text=""):
    """
    Write into a file

    Parameters:
        filename (string): filename
        text (string): string to write in the file

    Return: Nothing
    """

    char_numbers = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        char_numbers = f.write(text)
    return char_numbers

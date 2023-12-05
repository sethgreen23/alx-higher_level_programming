#!/usr/bin/python3
"""Print text in stdout Module"""


def read_file(filename=""):
    """
    Read a file

    Parameters:
        filename (string): name of the file

    Return: Nothing
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line, end="")

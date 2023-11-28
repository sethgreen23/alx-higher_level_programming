#!/usr/bin/python3
"""Module to print without white space"""


def text_indentation(text):
    """
    Print without indentation

    Parameters:
        text(str): text to work with

    Return:
        Nothing
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) > 0:
        start = 0
        end = 0
        count = 0
        for i, letter in enumerate(text):
            if letter in ".?:" or i + 1 == len(text):
                end = i + 1
                line = text[start: end].lstrip()
                if i + 1 == len(text):
                    print(line, end="")
                else:
                    print(line)
                    print("")
                    start = end

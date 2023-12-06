#!/usr/bin/python3
"""Append After"""


def append_after(filename="", search_string="", new_string=""):
    """Append After"""

    new_list = []
    with open(filename, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_list)

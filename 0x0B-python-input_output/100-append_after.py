#!/usr/bin/python3
"""Append After"""


def append_after(filename="", search_string="", new_string=""):
    """Append After"""

    if not search_string or not new_string or not filename:
        return
    lines_count = []
    with open(filename, "r", encoding="utf-8") as f:
        lst = list(f)
    new_list = []
    for line in lst:
        new_list.append(line)
        words = line.split(" ")
        for word in words:
            if search_string in word:
                new_list.append(new_string)
                break
    with open(filename, "w", encoding="utf-8") as f:
        for line in new_list:
            f.write(line)

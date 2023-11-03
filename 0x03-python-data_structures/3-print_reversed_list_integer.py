#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    while idx >= 0:
        format_str = "{0:d}".format(my_list[idx])
        print(format_str)
        idx -= 1

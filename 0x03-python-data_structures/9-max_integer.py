#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    max_val = my_list[0]
    for idx in range(1, len(my_list)):
        if my_list[idx] > max_val:
            max_val = my_list[idx]
    return (max_val)

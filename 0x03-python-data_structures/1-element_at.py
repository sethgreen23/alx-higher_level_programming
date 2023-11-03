#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list)
    if idx >= len_list or idx < 0:
        return (None)
    return (my_list[idx])

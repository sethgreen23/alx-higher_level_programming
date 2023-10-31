#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return (str)
    str_list = list(str)
    return ("".join(str_list[:n]+str_list[n+1:]))

#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for value in my_string:
        if (ord(value) not in [67, 99]):
            new_string.append(value)
    return ("".join(new_string))

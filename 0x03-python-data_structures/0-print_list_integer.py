#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        for value in my_list:
            print("{:d}".format(value))

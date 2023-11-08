#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    summation = 0
    for x in list(new_list):
        summation += x
    return (summation)

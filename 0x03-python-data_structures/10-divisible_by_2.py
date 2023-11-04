#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for value in my_list:
        if not value % 2 == 0:
            new_list.append(False)
        else:
            new_list.append(True)
    return (new_list)

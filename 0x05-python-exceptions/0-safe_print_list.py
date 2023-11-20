#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for num in my_list[:x]:
            print(str(num))
            printed = printed + 1;
    except IndexError as e:
        return (printed)
    return (printed)


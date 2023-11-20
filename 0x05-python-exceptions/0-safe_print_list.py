#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        if x > 0:
            for num in my_list[:x]:
                print(str(num), end='')
                printed = printed + 1
    except IndexError as e:
        print("")
        return (printed)
    print("")
    return (printed)

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            if (not isinstance(my_list[i], int)):
                continue
            print("{:d}".format(my_list[i]), end="")
            printed += 1
    except Exception:
        raise Exception
    print("")
    return (printed)

#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError, NameError) as ex:
        print("Exception: {}".format(ex))
        return (False)
    return (True)

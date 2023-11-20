#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not isinstance(value, int):
            raise Exception("{value} is not and integer".format(value))
        print("{:d}".format())
    except Exception:
        print("")
        return (False)
    else:
        print("")
        return (True)

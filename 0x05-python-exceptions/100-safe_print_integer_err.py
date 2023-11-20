#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError, NameError) as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return (False)
    print()
    return (True)

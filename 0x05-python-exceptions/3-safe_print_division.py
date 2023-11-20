#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        result = None
        return (result)
    else:
        return (result)
    finally:
        if result is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(result))

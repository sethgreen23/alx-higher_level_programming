#!/usr/bin/python3

if __name__ == '__main__':
    from add_0 import add

    a = 1
    b = 2
    result = add(a, b)

    print("{a:d} + {b:d} = {result:d}".format(a = a, b = b, result = result))

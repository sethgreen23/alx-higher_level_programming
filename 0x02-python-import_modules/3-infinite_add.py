#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    arguments = sys.argv[1:]
    argv_len = len(arguments)
    if argv_len == 0:
        print("{0:d}".format(0))
    else:
        sum_args = 0
        for value in arguments:
            sum_args += int(value)
        print("{0:d}".format(sum_args))

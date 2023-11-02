#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv_length = len(sys.argv) - 1
    argv_or_s = "arguments" if not argv_length == 1 else "argument"
    argv_print = "{0:d} {1}:".format(argv_length, argv_or_s)
    print(argv_print)
    if argv_length > 0:
        values = sys.argv[1:]
        for index, value in enumerate(values):
            value_p = "{0:d}: {1}".format(index + 1, value)
            print(value_p)

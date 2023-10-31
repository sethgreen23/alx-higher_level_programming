#!/usr/bin/python3
i = 97
while i < 123:
    if not chr(i) in 'qe':
        print("{}".format(chr(i)), end='')
    i += 1

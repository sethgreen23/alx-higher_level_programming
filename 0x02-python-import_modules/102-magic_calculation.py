#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(2, 4):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))

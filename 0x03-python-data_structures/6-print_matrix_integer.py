#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = []
    for i in range(0, 2):
        value_a = 0
        if i < len(tuple_a):
            value_a = tuple_a[i]
        value_b = 0
        if i < len(tuple_b):
            value_b = tuple_b[i]
        tup.append(value_a + value_b)
    return (tuple(tup))

#!/usr/bin/python3
i = 90
while i >= 65:
    output = chr(i + 32) if i % 2 == 0 else chr(i)
    print("{}".format(output), end="")
    i -= 1

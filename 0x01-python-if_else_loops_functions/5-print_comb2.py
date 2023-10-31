#!/usr/bin/python3
i = 0
while i < 100:
    end = ', ' if i < 99 else "\n"
    print("{a:02d}".format(a=i), end=end)
    i += 1

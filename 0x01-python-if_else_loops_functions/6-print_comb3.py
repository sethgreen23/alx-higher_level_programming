#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j or i > j:
            continue
        end = '' if (i * 10 + j) >= 89 else ', '
        print("{}{}".format(i, j), end=end)
print()

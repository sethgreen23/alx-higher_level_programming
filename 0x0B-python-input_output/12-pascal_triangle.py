#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Triangle Pascal"""

    matrix = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                if i >= 3:
                    row.append(matrix[i - 2][j - 1] + matrix[i - 2][j])
        matrix.append(row)
    return matrix

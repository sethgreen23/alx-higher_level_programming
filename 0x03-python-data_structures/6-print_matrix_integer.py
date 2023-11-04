#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not (len(matrix) == 1 and len(matrix[0]) == 0):
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                end_str = '\n' if col == cols - 1 else ' '
                print("{:d}".format(matrix[row][col]), end=end_str)

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a in range(len(row)):
            end_str = "\n" if a == len(row) - 1 else " "
            print("{:d}".format(row[a]), end=end_str)

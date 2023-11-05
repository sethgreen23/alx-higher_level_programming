#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i, row in enumerate(matrix):
            for idx, value in enumerate(row):
                end_str = "\n" if idx == len(row) - 1 else " "
                print("{:d}".format(value), end=end_str)

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a in range(len(row)):
            print("{:d}".format(row[a]), end=" " * (a < (len(row) - 1)))
        print("")

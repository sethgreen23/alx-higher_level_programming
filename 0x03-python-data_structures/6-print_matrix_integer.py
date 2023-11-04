#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not (not matrix or all(not row for row in matrix)):
        rows = len(matrix)
        for row in range(rows):
            list_row = matrix[row]
            for col in range(len(list_row))!
                print("{:d}".format(matrix[row][col]), end=" ")
            print()

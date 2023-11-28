#!/usr/bin/python3
"""Matrix module"""


def full_copy(m):
    """
    Copy the original matrix

    Parameters:
        m (list(list)): matrix to copy

    Return:
        list(list): copy of a matrix
    """

    matrix = []
    for row in m:
        matrix.append(list(row))
    return matrix


def is_same_length(matrix):
    """
    Check if the size of all lists are equal

    Parameters:
        matrix (list(list)): matrix to copy

    Return:
        boolean: True if same or False
    """

    row_size = len(matrix[0])
    return all(len(row) == row_size for row in matrix)


def is_list(matrix):
    """
    Check if is list

    Parameters:
        matrix (list(list)): matrix to copy

    Return:
        boolean: True if same or False
    """

    return isinstance(matrix, list) and len(matrix) > 0


def is_list_of_lists(matrix):
    """
    Check if is matrix is list or lists

    Parameters:
        matrix (list(list)): matrix to copy

    Return:
        boolean: True if same or False
    """

    return all(is_list(row) for row in matrix)


def is_int_or_float(matrix):
    """
    Check if is the matrix contains
    floats and integers

    Parameters:
        matrix (list(list)): matrix to copy

    Return:
        boolean: True if same or False
    """

    for row in matrix:
        for el in row:
            if not isinstance(el, int) and not isinstance(el, float):
                return False
    return True


def check_list_float_int(matrix):
    """
    Check if Matrix is list of list and
    the elements of the matrix composed of
    ints and floats

    Parameters:
        matrix (list(list)): matrix to copy

    Return:
        boolean: True if same or False
    """

    if is_list(matrix):
        if is_list_of_lists(matrix):
            if is_int_or_float(matrix):
                return True
    return False


def matrix_divided(matrix, div):
    """
    Do the matrix division

    Parameters:
        matrix (list(list)): matrix to copy
        div (int): dividor

    Return:
        list(lists): matrix divided
    """

    if not check_list_float_int(matrix):
        message = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(message)
    if not is_same_length(matrix):
        message = "Each row of the matrix must have the same size"
        raise TypeError(message)
    if not isinstance(div, int) and not isinstance(div, float):
        message = "div must be a number"
        raise TypeError(message)
    if div == 0:
        message = "division by zero"
        raise ZeroDivisionError(message)
    m = full_copy(matrix)
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = round(m[i][j] / div, 2)
    return m

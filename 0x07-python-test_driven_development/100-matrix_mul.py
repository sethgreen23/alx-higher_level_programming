#!/usr/bin/python3
"""Mul Matricess Module"""


def is_list(ls):
    """
    check if is list

    Parameters:
        ls (list): list to check

    Return:
        boolean: True or false
    """

    return isinstance(ls, list)


def is_float(num):
    """
    check if is float

    Parameters:
        num: variable to check

    Return:
        boolean: True or False
    """

    return isinstance(num, float)


def is_int(num):
    """
    check if is int

    Parameters:
        num: variable to check

    Return:
        boolean: True or False
    """

    return isinstance(num, int)


def is_float_int(ls):
    """
    check is list if made of float or integer

    Parameters:
        ls (list): list to check

    Return:
        boolean: True or False
    """

    return all(is_float(num) or is_int(num) for num in ls)


def is_all_float_int(matrix):
    """
    check if matrix is made of float and integers

    Parameters:
        matrix (list(lists)): matrix to check

    Return:
        boolean: True or False
    """

    return all(is_float_int(ls) for ls in matrix)


def is_list_of_list(matrix):
    """
    check is matrix is list of lists

    Parameters:
        matrix (list(list)): matrix os matrix

    Return:
        boolean: True or False
    """

    return all(is_list(sub_list) for sub_list in matrix)


def is_empty(matrix):
    """
    check is an empty matrix or not

    Parameters:
        matrix (list(list)): matrix to check

    Return:
        boolean: True or False
    """

    return len(matrix) == 0 or all(len(el) == 0 for el in matrix)


def is_rectangle(matrix):
    """
    check if a matrix is a rectangle

    Parameters:
        matrix (list(list)): matrix to check

    Return:
        boolean: True or False
    """

    all_len = [len(ls) for ls in matrix]
    return len(set(all_len)) == 1


def is_multiplied(m_a, m_b):
    """
    check if two matrix are multipliable

    Parameters:
        m_a (list(list)): matrix one
        m_b (list(list)): matrix two

    Return:
        boolean: True or False
    """

    return len(m_a[0]) == len(m_b)


def createEmptyMatrix(m_a, m_b):
    """
    create an empty result matrix

    Parameters:
        m_a (list(list)): matrix one
        m_b (list(list)): matrix two

    Return:
        list(list): matrix
    """

    rows = len(m_a)
    columns = len(m_b[0])
    res_matrix = []
    for _ in range(rows):
        res_matrix.append([])
    for i in range(rows):
        for _ in range(columns):
            res_matrix[i].append(0)
    return res_matrix


def matrix_mul(m_a, m_b):
    """
    function to multiply two matrix

    Parameters:
        m_a (list(list)): matrix one
        m_b (list(list)): matrix two

    Return:
        list(list): matrix
    """

    if not is_list(m_a):
        raise TypeError("m_a must be a list")
    if not is_list(m_b):
        raise TypeError("m_b must be a list")
    if not is_list_of_list(m_a):
        raise TypeError("m_a must be a list of lists")
    if not is_list_of_list(m_b):
        raise TypeError("m_b must be a list of lists")
    if is_empty(m_a):
        raise ValueError("m_a can't be empty")
    if is_empty(m_b):
        raise ValueError("m_b can't be empty")
    if not is_all_float_int(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not is_all_float_int(m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not is_rectangle(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not is_rectangle(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not is_multiplied(m_a, m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = createEmptyMatrix(m_a, m_b)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return (result)

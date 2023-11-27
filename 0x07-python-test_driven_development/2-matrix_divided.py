#!/usr/bin/python3
"""
Module Name: matrix_divided
The module Divides each item in a given matrix a 2D list with a given number
"""


def matrix_divided(matrix, div):
    """Tehe module Returns a new matrix a 2D list.
    with the result of the division of given matrix by a number.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len_rows = []
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        len_rows.append(len(row))
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_mat = [[round(x / div, 2) for x in row] for row in matrix]

    return result_mat

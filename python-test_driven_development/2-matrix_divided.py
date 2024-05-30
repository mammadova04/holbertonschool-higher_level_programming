#!/usr/bin/python3
"""matrix division and test"""


def matrix_divided(matrix, div):
    """matrix division"""
    divisionerror = "division by zero"
    typeerror = "div must be a number"
    itemerror = "matrix must be a matrix (list of lists) of integers/floats"
    sizeerror = "Each row of the matrix must have the same size"

    def itemerrorfunc():
        raise TypeError(itemerror)

    def sizeerrorfunc():
        raise TypeError(sizeerror)

    if not isinstance(div, (int, float)):
        raise TypeError(typeerror)
    if div == 0 or div == 0.0:
        raise ZeroDivisionError(divisionerror)

    length = len(matrix[0])
    return list(map(
        lambda x: list(map(
            lambda y: round(y / div, 2) if isinstance(
                y, (float, int)
                ) else itemerrorfunc(), x
            )) if len(x) == length else sizeerrorfunc(), matrix
        ))

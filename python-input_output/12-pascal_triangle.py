#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Function Document"""
    if n <= 0:
        return []

    matrix = []
    array = []

    for i in range(n):
        if i >= 2:
            arr = array[:]
            for j in range(i - 1):
                array[j + 1] = arr[j] + arr[j + 1]
        array.append(1)
        matrix.append(array[:])
    return matrix

#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row_nums, list) for row_nums in matrix) or
            not all((isinstance(elements_num, int) or isinstance(elements_num, float))
                    for elements_num in [num for row_nums in matrix for num in row_nums])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row_nums) == len(matrix[0]) for row_nums in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row_nums)) for row_nums in matrix])



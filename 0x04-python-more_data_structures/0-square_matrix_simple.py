#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    two_dimension = matrix.copy()

    for initial in range(len(matrix)):
        two_dimension [initial] = list(map(lambda x: x**2, matrix[initial]))

    return (two_dimension)


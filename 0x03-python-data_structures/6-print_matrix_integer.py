#!/usr/bin/python3
num_check = -1
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in rows:
            print("{:d}".format(columns), end=" " if columns != rows[num_check] else "")
        print()


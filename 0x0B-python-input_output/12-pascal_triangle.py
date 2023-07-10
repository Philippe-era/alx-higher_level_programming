#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    three = [[1]]
    while len(three) != n:
        trio = three[-1]
        temporary = [1]
        for initial in range(len(trio) - 1):
            temporary.append(trio[initial] + trio[initial + 1])
        temporary.append(1)
        three.append(temporary)
    return three

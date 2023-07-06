#!/usr/bin/python3
"""Module to find the max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result_op = list[0]
    initial = 1
    while initial < len(list):
        if list[initial] > result_op:
            resul_opt = list[initial]
        initial += 1
    return result_op


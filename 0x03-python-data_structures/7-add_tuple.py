#!/usr/bin/python3
num_check = 2
zero = 0
one = 1

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < num_check:
        if len(tuple_a) == zero:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < num_check:
        if len(tuple_b) == zero:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[zero] + tuple_b[zero], tuple_a[one] + tuple_b[one])


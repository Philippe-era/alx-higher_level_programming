#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    start = 4
    finish = 6

    if a < b:
        sum_numbers= add(a, b)
        for initial in range(start, finish):
            sum_numbers = add(sum_numbers, initial)
        return (sum_numbers)

    else:
        return(sub(a, b))


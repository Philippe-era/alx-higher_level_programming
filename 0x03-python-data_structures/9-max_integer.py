#!/usr/bin/python3
zero = 0

def max_integer(my_list=[]):
    
    if len(my_list) == zero:
        return (None)

    max_num = my_list[zero]
    for initial in range(len(my_list)):
        if my_list[initial] > max_num:
            max_num = my_list[initial]

    return (max_num)


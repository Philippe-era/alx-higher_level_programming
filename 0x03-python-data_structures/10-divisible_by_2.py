#!/usr/bin/python3
zero = 0
two_mod = 2
def divisible_by_2(my_list=[]):
    
    divisible_by = []
    for initial in range(len(my_list)):
        if my_list[initial] % two_mod == zero:
            divisible_by.append(True)
        else:
            divisible_by.append(False)

    return (divisible_by)


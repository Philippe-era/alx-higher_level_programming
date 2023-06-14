#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num_check = 0
    different_num = 0
    stable = 1

    for check in my_list:
        num_check += check[0] * check[stable]
        different_num += check[stable]

    return (num_check / different_num)


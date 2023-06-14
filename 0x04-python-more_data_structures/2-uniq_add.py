#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    number_check = 0

    for initial in new_list:
        number_check += initial

    return (number_check)


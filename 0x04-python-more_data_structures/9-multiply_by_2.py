#!/usr/bin/python3
two = 2
def multiply_by_2(a_dictionary):
    multiplied_nums = a_dictionary.copy()
    sorted_list = list(multiplied_nums.keys())

    for initial in sorted_list:
        multiplied_nums[initial] *= two

    return (multiplied_nums)


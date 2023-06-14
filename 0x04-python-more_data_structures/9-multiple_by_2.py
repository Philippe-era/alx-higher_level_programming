#!/usr/bin/python3
two = 2
def multiply_by_2(a_dictionary):
    multiplied_nums = a_dictionary.copy()
    sorted_list = list(multipled_nums.keys())

    for initial in sorted_list:
        multipled_nums[initial] *= two

    return (multiplied_nums)


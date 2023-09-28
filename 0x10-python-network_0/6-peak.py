#!/usr/bin/python3
"""algorithm to find the peak number"""


def find_peak(list_of_integers):
    """ this will return the peak number """
    if list_of_integers == []:
        return None

    length_integers = len(list_of_integers)
    max_number = int(length_integers / 2)
    list_check = list_of_integers

    if max_number - 1 < 0 and max_number + 1 >= length_integers:
        return list_check[max_number]
    elif max_number - 1 < 0:
        return list_check[max_number] if list_check[max_number] > list_check[max_number + 1] else list_check[max_number + 1]
    elif max_number + 1 >= length_integers:
        return list_check[max_number] if list_check[max_number] > list_check[max_number - 1] else list_check[max_number - 1]

    if list_check[max_number - 1] < list_check[max_number] > list_check[max_number + 1]:
        return list_check[max_number]

    if list_check[max_number + 1] > list_check[max_number - 1]:
        return find_peak(list_check[max_number:])
    return find_peak(list_check[:max_number])


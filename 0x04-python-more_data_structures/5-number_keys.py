#!/usr/bin/python3
def number_keys(a_dictionary):
    number_check = 0
    keys_listed = list(a_dictionary.keys())

    for initial in keys_listed:
        number_check += 1

    return (number_check)


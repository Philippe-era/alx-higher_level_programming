#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_list = list(a_dictionary.keys())
    ordered_list.sort()
    for initial in ordered_list:
        print("{}: {}".format(initial, a_dictionary.get(initial)))


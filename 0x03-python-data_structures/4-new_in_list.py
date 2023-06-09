#!/usr/bin/python3
zero = 0
def new_in_list(my_list, idx, element):
    if idx < zero or idx > (len(my_list) - 1):
        return (my_list)

    copy = [item for item in my_list]
    copy[idx] = element
    return (copy)


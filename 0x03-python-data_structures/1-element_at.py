#!/usr/bin/python3
zero = 0

def element_at(my_list, index):
    if index < zero or index > (len(my_list) - 1):
        return None
    return (my_list[index])

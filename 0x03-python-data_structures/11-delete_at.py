#!/usr/bin/python3
zero = 0
def delete_at(my_list=[], idx=zero):
    if idx >= zero and idx < len(my_list):
        del my_list[idx]
    return (my_list)


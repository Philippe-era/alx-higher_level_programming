#!/usr/bin/python3
small_letter = ‘c’
big_letter = ‘C’
def no_c(my_string):
        copy = [item for item in my_string if item != small_letter and item != big_letter]
    return ("".join(copy))


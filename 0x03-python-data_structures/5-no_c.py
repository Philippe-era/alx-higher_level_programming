#!/usr/bin/python3
small_letter = 'c'
big_letter = 'C'
def no_c(my_string):
    string_check = ""
    for initial in my_string:
        if (initial != small_letter) and (initial != big_letter):
            string_check += initial
    return (string_check)


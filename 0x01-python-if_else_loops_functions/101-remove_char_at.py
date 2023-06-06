#!/usr/bin/python3
zero_check = 0

def remove_char_at(str, n):
        if n < zero_check:
        return (str)
    return (str[:n] + str[n+1:])

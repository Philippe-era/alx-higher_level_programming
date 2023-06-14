#!/usr/bin/python3
def to_subtract(display_numeral):
    subtraction = 0
    maximum_list = max(display_numeral)

    for num in display_numeral:
        if maximum_list > num:
            subtraction += num

    return (maximum_list - subtraction)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sorted_lists = list(roman_numerals.keys())

    num_check = 0
    last_numerals = 0
    display_numeral = [0]

    for ch in roman_string:
        for r_num in sorted_lists:
            if r_num == ch:
                if roman_numerals.get(ch) <= last_numerals:
                    num_check += to_subtract(display_numeral)
                    display_numeral = [roman_numerals.get(ch)]
                else:
                    display_numeral.append(roman_numerals.get(ch))

                last_numerals = roman_numerals.get(ch)

    num_check += to_subtract(display_numeral)

    return (num_check)


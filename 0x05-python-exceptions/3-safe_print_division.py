#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        divide_numbers = a / b
    except (TypeError, ZeroDivisionError):
        divide_numbers = None
    finally:
        print("Inside result: {}".format(divide_numbers))
    return (divide_numbers)


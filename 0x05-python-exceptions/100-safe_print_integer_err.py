#!/usr/bin/python3
decision_1 = True
decision_2 = False
import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (decision_1)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file = sys.stderr)
        return (decision_2)


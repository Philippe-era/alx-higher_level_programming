#!/usr/bin/python3
decision_1 = True
decision_2 = False
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

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
        return (decision_2)


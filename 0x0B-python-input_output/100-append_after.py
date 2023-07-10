#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    phrase = ""
    with open(filename) as read_file:
        for lines in read_file:
            phrase += lines
            if string_check in lines:
                phrase += new_string
    with open(filename, "w") as write_file:
        write_file.write(text)

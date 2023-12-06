#!/usr/bin/python3
"""Mod creates text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    txt = ""
    with open(filename) as hr:
        for line in hr:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as hw:
        hw.write(txt)

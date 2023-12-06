#!/usr/bin/python3
"""Module defines text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """func Inserts text after each
    line containing given string in a file.
    """
    txt = ""
    with open(filename) as hr:
        for line in hr:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as hw:
        hw.write(txt)

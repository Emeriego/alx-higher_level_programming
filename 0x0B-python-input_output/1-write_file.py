#!/usr/bin/python3
"""Module defines a file-writing method."""


def write_file(filename="", text=""):
    """func Writes to a text file and returns
    the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as h:
        return h.write(text)

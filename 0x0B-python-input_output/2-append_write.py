#!/usr/bin/python3
"""Module defines file appending function."""


def append_write(filename="", text=""):
    """func appends string to the end file
    the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as h:
        return h.write(text)

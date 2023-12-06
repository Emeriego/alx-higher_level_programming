#!/usr/bin/python3
"""Module Name: 0-read_file"""


def read_file(filename=""):
    """func Prints the contents of file to stdout."""
    with open(filename, encoding="utf-8") as h:
        print(h.read(), end="")

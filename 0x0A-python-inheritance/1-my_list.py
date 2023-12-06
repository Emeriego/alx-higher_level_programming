#!/usr/bin/python3
"""Func creates an inherited list class"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints in ascending order."""
        print(sorted(self))

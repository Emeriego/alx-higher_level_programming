#!/usr/bin/python3

"""Module sorts list"""


class MyList(list):
    """Subclass of the global list"""
    def __init__(self):
        """initialize object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))

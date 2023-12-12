#!/usr/bin/python3
"""Module Name: 1-my_list"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))

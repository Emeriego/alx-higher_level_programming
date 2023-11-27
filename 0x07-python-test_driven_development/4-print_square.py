#!/usr/bin/python3
"""
Module Name: print_square
This module Prints a square with '#'.
"""


def print_square(size):
    """Prints a square, size is
    the length and width.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for item in range(size):
        for j in range(size):
            print('#', end='')
        print()

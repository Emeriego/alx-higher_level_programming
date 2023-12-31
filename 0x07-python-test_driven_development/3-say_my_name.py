#!/usr/bin/python3
"""
Module Name:  say_my_name
This module Prints a given names.
"""


def say_my_name(first_name, last_name=""):
    """Prints a string with first_name and last_name.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

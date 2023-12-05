#!/usr/bin/python3
"""Module to check if obj is an instance of a_class"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class
    """
    return type(obj) is a_class

#!/usr/bin/python3
"""Module defines a Python class-to-JSON function."""


def class_to_json(obj):
    """func returns the dictionary represntation of a simple data structure."""
    return obj.__dict__

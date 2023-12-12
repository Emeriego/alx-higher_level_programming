#!/usr/bin/python3
"""Function returns a list of all
available attributes and methods"""


def lookup(obj):
    """Returns list of methods & attributes that are available"""
    return dir(obj)

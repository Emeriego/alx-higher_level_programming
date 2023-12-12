#!/usr/bin/python3
"""Module Name: 101-add_attribute"""


def add_attribute(obj, name, value):
    """if possible, adds new attribute to an object"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

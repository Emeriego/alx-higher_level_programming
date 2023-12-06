#!/usr/bin/python3
"""Module defines func that converts
a string to JSON"""
import json


def to_json_string(my_obj):
    """func returns the JSON representation of a string object."""
    return json.dumps(my_obj)

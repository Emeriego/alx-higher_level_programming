#!/usr/bin/python3
"""Module Defines funct that converts
a JSON-to-object"""
import json


def from_json_string(my_str):
    """func returns the Python object representation of a JSON string."""
    return json.loads(my_str)

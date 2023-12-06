#!/usr/bin/python3
"""Module defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """func Writes an object to a text file using JSON representation."""
    with open(filename, "w") as h:
        json.dump(my_obj, h)

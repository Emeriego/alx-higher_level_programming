#!/usr/bin/python3
"""Module defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """func Creates Python object from a JSON file."""
    with open(filename) as h:
        return json.load(h)

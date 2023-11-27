#!/usr/bin/python3
"""
Module Name: text_indentation
This module Adds two new lines after some given chars.
"""


def text_indentation(text):
    """Adds two newlines after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in ".:?":
        text = (c + "\n\n").join([line.strip(" ") for line in text.split(c)])

    print("{}".format(text), end="")

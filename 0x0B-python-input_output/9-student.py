#!/usr/bin/python3
"""Module defines class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """func gets a dictionary representation
        of the Student object."""
        return self.__dict__

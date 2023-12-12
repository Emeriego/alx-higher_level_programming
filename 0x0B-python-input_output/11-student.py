#!/usr/bin/python3
"""Module creates class Student."""


class Student:
    """Class represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """method replaces all attributes of the Student.
        """
        for i, c in json.items():
            setattr(self, i, c)

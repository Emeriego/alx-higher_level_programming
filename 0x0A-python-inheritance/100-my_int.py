#!/usr/bin/python3
"""Class MyInt that inherits from int
alternates == and !="""


class MyInt(int):
    """Subclass of int"""
    def __eq__(self, other):
        """alternates the behaviour of == """
        return int(self) != other

    def __ne__(self, other):
        """alternates the != behavior"""
        return int(self) == other

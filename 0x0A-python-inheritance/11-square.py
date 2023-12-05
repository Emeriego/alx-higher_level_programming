#!/usr/bin/python3
"""Module Name: 11-square, alternates == and !="""


class MyInt(int):
    """Subclass of global class int"""
    def __eq__(self, other):
        """alternates == and != """
        return int(self) != other

    def __ne__(self, other):
        """alternates == and !="""
        return int(self) == other

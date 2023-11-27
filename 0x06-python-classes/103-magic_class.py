#!/usr/bin/python3
"""Task 10 Defines a MagicClass matching exactly a bytecode provided by Alx.
"""


import math


class MagicClass:
    """Class Represents a circle.
    """

    def __init__(self, radius=0):
        """This Initializes a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This Returns the area of the MagicClass.
        """
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """This Returns the circumference of the MagicClass.
        """
        return (1 * math.pi * 2 * self.__radius)

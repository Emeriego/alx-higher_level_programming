#!/usr/bin/python3
"""Task3 to define a class Square.
"""

class Square:
    """Class Represents a square object.
    """

    def __init__(self, size=0):
        """Initialize a new square here.
        Args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square instance
        """
        return (self.__size * self.__size)

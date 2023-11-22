#!/usr/bin/python3
"""Task 4 defines a class Square.
"""


class Square:
    """Class Represents a square object.
    """

    def __init__(self, size=0):
        """Initializes a new square object.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of square.
        """
        return (self.__size)
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square instance that calls it.
        """
        return (self.__size * self.__size)

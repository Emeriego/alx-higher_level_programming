#!/usr/bin/python3
"""Square Module"""


class Square:
    """Class defines a square"""

    def __init__(self, size=0):
        """Creates a Square
        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """"gets The property of size as the len of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """"Sets The property of size as the len of Square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Gets the area of a Square
        Returns: The sqr of size
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

#!/usr/bin/python3
"""Task Defines a class Square.
"""

class Square:
    """Class Represents a square object.
    """

    def __init__(self, size):
        """Initializes a square.
        Args:
            size (int): This is the size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square.
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
        """Returns the area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with a # character.
        """

        if self.__size == 0:
            print("")
        for item in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")

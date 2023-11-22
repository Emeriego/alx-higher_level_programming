#!/usr/bin/python3
"""Task 2 to define class Square.
"""

class Square:
    """This class Represents a square object.
    """


    def __init__(self, size=0):
        """Initialize a new Square here.
        Args:
            size (int): This is the size of  new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

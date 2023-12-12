#!/usr/bin/python3
"""imports class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle
"""Class square that inherites from rectangle"""


class Square(Rectangle):
    """Subclass of Rectangle"""
    def __init__(self, size):
        """initializes private attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Prints the square description"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))

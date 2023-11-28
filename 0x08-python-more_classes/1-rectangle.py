#!/usr/bin/python3
"""Module Name: 1-rectangle
The class represents a Rectangle.
"""


class Rectangle:
    """This class is defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance.

        Args:
            width: breadth of rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method retrieves the width of the new instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """method Sets the width of instance

        Args:
            value: value of the width, is only valid
            if it is a +ve integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method gets the height of new instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """method Sets the height of new instance

        Args:
            value: value of the width, is only valid
            if it is a +ve integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

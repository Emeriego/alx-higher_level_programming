#!/usr/bin/python3
"""Module Name: 3-rectangle
The class reprrsents a Rectangle.
"""


class Rectangle:
    """This class is defined by width and height.

    Attributes:
        number_of_instances: number of Rectangle instances,
        increments on every instance creation,
        decrements with every deletion
        print_symbol: used to print rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance.

        Args:
            width: breadth of rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Method Returns an informal and nicely printable
        string representation
        of a Rectangle instance usin '#'."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """A string representation of a Rectangle instance
        that is able to recreate a new instance by using eval() is returned
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method Deletes an instance. using 'Del instance()'"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """Uses the params to find the area of Rectangle instance

        Returns: The area of rectangle, given by height * width
        """
        result = self.__width * self.__height
        return result

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance

        Returns: perimeter given by
        2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area

        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1

        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

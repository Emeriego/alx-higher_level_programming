#!/usr/bin/python3
'''Module creates Class Rectangle from a base Base class
'''
from models.base import Base


class Rectangle(Base):
    '''Creates Rectangle from base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''This is a getter method
        private attribute is returned
        '''
        return self.__width

    @property
    def height(self):
        '''This is a getter method
        private attribute is returned
        '''
        return self.__height

    @property
    def x(self):
        '''This is a getter method
        private attribute is returned
        '''
        return self.__x

    @property
    def y(self):
        '''This is a getter method
        private attribute is returned
        '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' This is a setter method
        Sets private attribute
        '''
        self.validate_attr("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        ''' This is a setter method
        Sets private attribute
        '''
        self.validate_attr("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        ''' This is a setter method
        Sets private attribute
        '''
        self.validate_attr("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        ''' This is a setter method
        Sets private attribute
        '''
        self.validate_attr("y", value)
        self.__y = value

    @staticmethod
    def validate_attr(attribute, value):
        ''' This validates the attributes before setting is done
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def display(self):
        '''This prints the image of itself using #
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        '''using varying arguments
            the arguments in the class is updated
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def area(self):
        '''This calculates and returns area of rec
            Returns the area of the rectangle
        '''
        return (self.height * self.width)

    def to_dictionary(self):
        '''Returns a dictionary representation of this class
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    def __str__(self):
        '''Overiding the str method with a custom __str__
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

def __str__(self):
        """Method Returns an informal and nicely printable string representation
        of a Rectangle instance usin '#'.

        Returns:
        returns the official string
        """

        if self.__height == 0 or self.__width == 0:
            return ''
        f_str = ''
        for idx in range(self.__height):
            for j in range(self.__width):
                f_str += '#'
            f_str += '\n'
        return f_str[:-1]

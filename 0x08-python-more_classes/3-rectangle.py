#!/usr/bin/python3

"""
Define a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print the rectangle with the character '#'"""
        rect_str = ""
        if self.__width != 0 and self.__height != 0:
            rect_str += '\n'.join('#' * self.__width
                                 for j in range(self.__height))
        return rect_str

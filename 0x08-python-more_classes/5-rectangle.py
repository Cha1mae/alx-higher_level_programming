#!/usr/bin/python3

"""
Define a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Rectangle class lol"""

    def __init__(self, width=0, height=0):
        """lets initialize Rectangle

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """we fetsh the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sett the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """fetsh the height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sett the height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Cal the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Cal the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """pwwint the rectangle with the character '#'"""
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return rect_str
        for i in range(self.__height):
            rect_str += '#' * self.__width + '\n'
        return rect_str[:-1]

    def __repr__(self):
        """let return a string rep of the rectgl for rec"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """pwint the mesg Bye rectangle... when an instance is del"""
        print("Bye rectangle...")

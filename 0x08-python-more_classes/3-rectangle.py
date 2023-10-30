#!/usr/bin/python3
"""
Define a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    rectangle class again
    """

    def __init__(self, width=0, height=0):
        """
        Sets the necessary attributes for the Rectangle object.

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Sets the print behavior of the Rectangle object.
        """
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'

        return rectangle[:-1]

    @property
    def width(self):
        """Get or sett the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sett the width of the rectangle.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """def height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sett the height of the rectangle.

        Args:
            value (int): The height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns the area of current rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns permter of the current rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

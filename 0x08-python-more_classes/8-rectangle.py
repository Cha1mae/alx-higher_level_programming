#!/usr/bin/python3
"""
Define a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Rectangle class plz work"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """fetsh the width of Rectangle"""
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
        """calc the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calc the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Pwint the rectangle with the char(s) stored in print_symbol"""
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return rect_str
        for i in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + '\n'
        return rect_str[:-1]

    def __repr__(self):
        """Ret a string representation of the rectangle for rec"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Pwint the message Bye rectangle... when an instance is del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2


if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 1)

    if Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

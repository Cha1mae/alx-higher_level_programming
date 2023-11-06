#!/usr/bin/python3
"""Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Sttarts private size atribute"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)

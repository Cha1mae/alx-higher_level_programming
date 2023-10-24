#!/usr/bin/python3
"""scare mod"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the data"""
        self.size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method to retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Prints the square with '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

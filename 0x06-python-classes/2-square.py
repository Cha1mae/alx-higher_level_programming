#!/usr/bin/python3
"""THE SQUARE MODULE"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the data
	
	Args:
	    size: lenght of square side

	Raises:
	    TypeError: is size not int
	    ValueError: if size less dan 0
	"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3
""" Base Geometry mod"""


class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value as an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

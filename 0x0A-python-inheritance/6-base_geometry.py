#!/usr/bin/python3
"""Geometry base module"""


class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception('area() is not implemented')

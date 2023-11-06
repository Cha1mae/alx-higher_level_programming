#!/usr/bin/python3
"""
Exact same object module
"""


def is_same_class(obj, a_class):
    """Returns True if the obj is of the specified class;
    otherwise False."""
    return type(obj) is a_class

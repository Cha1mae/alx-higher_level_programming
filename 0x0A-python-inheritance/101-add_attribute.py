#!/usr/bin/python3
"""Add attribute module to obj"""


def add_attribute(obj, attr, value):
    """Adds a new att to an object if possible, otherwise raises a
    TypeError with the message 'can't add new attribute'"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

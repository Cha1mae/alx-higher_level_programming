#!/usr/bin/python3
"""Mod for inherits_from method"""


def inherits_from(obj, a_class):
    """det if the obj is an inst of a class that inherited"""
    return isinstance(obj, a_class) and type(obj) is not a_class
